# This Python file uses the following encoding: utf-8
# UNIVPM
import sys
import os
import cv2
import numpy as np
import pandas as pd
import math
from PIL import Image

from skimage.transform import resize
from skimage.morphology import binary_erosion, binary_dilation
from skimage.measure import label, regionprops
from skimage.transform import resize
from skimage.morphology import binary_erosion, binary_dilation
from skimage.measure import label, regionprops

import matplotlib.patches as patches
import pydicom

from tensorflow.keras.models import model_from_json

from pydicom.pixel_data_handlers.util import convert_color_space
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog,  QGraphicsScene, QGraphicsEllipseItem, QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator ,QIcon, QPixmap, QImage, QPen, QColor
from PySide6.QtCore import QRectF, Qt, Signal

from ui_form import Ui_MainWindow
from info import Ui_Form

def set_dark_theme():
    app.setStyleSheet("""
        QWidget {
            background-color: #F2F2F2;
            color: black;
        }
        QPushButton {
            background-color: #A00000;
            color: white;
            border: 1px solid #777;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #730d0d;
        }
    """)

class MainWindow(QMainWindow):

    def create_DB(self):
        if not os.path.exists('training_set_pixel_size_and_HC.csv') or not os.path.exists('test_set_pixel_size.csv'):
                self.pixelSizesDB = pd.DataFrame()
                return
        df1 = pd.read_csv('training_set_pixel_size_and_HC.csv')
        df1.drop(columns=['head circumference (mm)'], inplace=True)
        df2 = pd.read_csv('test_set_pixel_size.csv')
        self.pixelSizesDB = pd.concat([df1, df2], ignore_index=True)


    def showImage(self, numpyImage, GraphicalScene=None ,ellipse_params=None, LOGO = False):
        """
        Displays the image in the graphics view and optionally draws an ellipse.

        :param numpyImage: Grayscale image as a NumPy array
        :param ellipse_params: Tuple containing ellipse parameters:
                               ((center_x, center_y), (width, height), angle)
        """

        # Convert the NumPy image to QImage

        shape = numpyImage.shape
        height, width = shape[0], shape[1]

        bytes_per_line = width

        if len(shape) == 2:
            qimage = QImage(numpyImage.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        elif len(shape) == 3:
            qimage = QImage(numpyImage.data, numpyImage.shape[1], numpyImage.shape[0],
                            numpyImage.strides[0], QImage.Format_RGB888)

        # Convert QImage to QPixmap and display in the QGraphicsView
        pixmap = QPixmap.fromImage(qimage)
        if LOGO:
            scene = QGraphicsScene()
            GraphicalScene.setScene(scene)
            scene.clear()  # Clear any existing items in the scene
            scene.addPixmap(pixmap)
            return

        scene = self.ui.graphicsView.scene()

        if scene is None:
            scene = QGraphicsScene()
            self.ui.graphicsView.setScene(scene)

        scene.clear()  # Clear any existing items in the scene
        scene.addPixmap(pixmap)

        # Draw the ellipse if parameters are provided
        if self.ellipse_params is not None:
            center = self.ellipse_params[0]  # (center_x, center_y)
            size = self.ellipse_params[1]    # (width, height)
            angle = self.ellipse_params[2]   # Rotation angle

            # Calculate the rectangle bounding the ellipse
            rect = QRectF(
                center[0] - size[0] / 2,  # Top-left x
                center[1] - size[1] / 2,  # Top-left y
                size[0],                 # Width
                size[1]                  # Height
            )

            # Create and configure the QGraphicsEllipseItem
            ellipse_item = QGraphicsEllipseItem(rect)
            ellipse_item.setPen(QPen(QColor('#2ecc71'), 1.5, Qt.SolidLine))
            ellipse_item.setTransformOriginPoint(rect.center())
            ellipse_item.setRotation(angle)

            # Add the ellipse to the scene
            scene.addItem(ellipse_item)


    def select_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Use Qt dialog instead of native dialog
        # Set file filters to allow only PNG and DCM files
        filters = "PNG Files (*.png);;DCM Files (*.dcm)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Select image file (PNG or DCM)", "", filters, options=options)
        if file_path:
            if (os.path.basename(file_path)[-3:].lower() == "dcm"): #Dicom Files
                self.fileName = os.path.basename(file_path)
                # Load the DICOM file
                ds = pydicom.dcmread(file_path)
                # Extract image data
                self.imageNumpy = ds.pixel_array
                self.showImage(self.imageNumpy)
                if self.modelFlag:
                    self.ui.predict_Button.setEnabled(True)
                    self.ui.save_Button.setEnabled(False)
                    if 'PixelSpacing' in ds:  # (0028,0030)
                        pixel_size = ds.PixelSpacing[0]*ds.PixelSpacing[1]  # [row spacing, column spacing] in mm
                        print(f"Pixel Spacing (0028,0030): {pixel_size} mm")

                    elif 'ImagerPixelSpacing' in ds:  # (0018,1164)
                        pixel_size = ds.ImagerPixelSpacing[0] * ds.ImagerPixelSpacing[1]  # [row spacing, column spacing] in mm
                        print(f"Imager Pixel Spacing (0018,1164): {pixel_size} mm")

                    elif hasattr(ds, 'SequenceOfUltrasoundRegions') and ds.SequenceOfUltrasoundRegions:
                        # Ultrasound calibration regions
                        for region in ds.SequenceOfUltrasoundRegions:
                            if hasattr(region, 'PhysicalDeltaX') and hasattr(region, 'PhysicalDeltaY'):
                                pixel_size = region.PhysicalDeltaY* region.PhysicalDeltaX  # [row spacing, column spacing]
                                self.ui.pixelSizeText.setText(str(f"{pixel_size:.3f}"))
                                break  # Use first valid region
                    #else:
                        #print("No pixel size information available in this DICOM file.")

            else: #PNG
                self.fileName = os.path.basename(file_path)
                self.imageNumpy = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                self.showImage(self.imageNumpy)
                if self.modelFlag:
                    self.ui.predict_Button.setEnabled(True)
                    self.ui.save_Button.setEnabled(False)
                self.reset()

                filtered_df = self.pixelSizesDB[self.pixelSizesDB['filename'] == self.fileName]
                if not filtered_df.empty:
                    pixel_size = filtered_df.loc[:, 'pixel size(mm)'].iloc[0]
                    self.ui.pixelSizeText.setText(str(f"{pixel_size:.3f}"))

    def load_the_network(self):
        try:
            # Load architecture from JSON
            with open("model_architecture.json", "r") as json_file:
                self.model = json_file.read()
                self.model = model_from_json(self.model)

            # Load weights into the new model
            self.model.load_weights("model_weights.h5")
            self.modelFlag = True
        except:
            self.modelFlag = False
            #print("NO MODEL IS LOADED!")

    def reset(self):
        self.ui.HCtextLabel.setText(f"HC: {0.00:.2f}")
        self.ui.OFDtextLabel.setText(f"OFD: {0.00:.2f}")
        self.ui.BPDtextLabel.setText(f"BPD: {0.00:.2f}")

    def make_prediction(self):
        self.reset()

        try:
            imageNumpyRes = np.array(resize(self.imageNumpy.squeeze(), (256,256), mode="reflect"))
            predictions = self.model.predict(np.expand_dims(imageNumpyRes, axis=0))
            # print(f"prediction_shape: {predictions.shape}")

            predicted_image_array = (predictions[0] * 255).astype(np.uint8).reshape(256, 256)

            original_height = np.shape(self.imageNumpy)[0]
            original_width = np.shape(self.imageNumpy)[1]

            resized_predictions = np.array(resize(predicted_image_array.squeeze(), (original_height, original_width), mode='reflect'))

            threshold_value = 0.5
            binary_predictions = (resized_predictions > threshold_value).astype(np.uint8)

            def apply_morphological_operations(binary_mask):
                # Erosion followed by dilation
                eroded_mask = binary_erosion(binary_mask)
                refined_mask = binary_dilation(eroded_mask)
                return refined_mask

            refined_predictions = np.array(apply_morphological_operations(binary_predictions))

            def keep_largest_connected_component(binary_mask):
                labeled_mask, _ = label(binary_mask, connectivity=2, return_num=True)
                props = regionprops(labeled_mask)
                largest_area = 0
                largest_label = 0
                for prop in props:
                    if prop.area > largest_area:
                        largest_area = prop.area
                        largest_label = prop.label
                largest_component_mask = (labeled_mask == largest_label).astype(np.uint8)
                return largest_component_mask

            largest_component_predictions = np.array(keep_largest_connected_component(refined_predictions))

            contours, _ = cv2.findContours(largest_component_predictions.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                self.ellipse_params = cv2.fitEllipse(contours[0])
                # display_image_with_ellipse(resized_test_images, ellipse_params)
                pixel_size_input = self.ui.pixelSizeText.text()

                if pixel_size_input and pixel_size_input.replace('.', '', 1).isdigit():
                    pixel_size_value = float(pixel_size_input)

                else:
                    pixel_size_value = 1.0

                semi_major_axis = self.ellipse_params[1][0] / 2.0
                semi_minor_axis = self.ellipse_params[1][1] / 2.0

                BPD = semi_major_axis * pixel_size_value * 2
                OFD = semi_minor_axis * pixel_size_value * 2
                HC = math.pi * (BPD + OFD) / 2

                self.ui.HCtextLabel.setText(f"HC: {HC:.2f} mm")
                self.ui.OFDtextLabel.setText(f"OFD: {OFD:.2f} mm")
                self.ui.BPDtextLabel.setText(f"BPD: {BPD:.2f} mm")

                self.showImage(self.imageNumpy, self.ellipse_params)
                self.ui.save_Button.setEnabled(True)


        except Exception as e:
            print("Error making prediction:", str(e))

    def savePrediction(self):

        HC = self.ui.HCtextLabel.text()
        OFD = self.ui.OFDtextLabel.text()
        BPD = self.ui.BPDtextLabel.text()

        # Clean the input strings to remove unnecessary prefixes
        HC = HC.replace("HC: ", "")
        OFD = OFD.replace("OFD: ", "")
        BPD = BPD.replace("BPD: ", "")

        data = {
            "HC": HC + "mm",
            "OFD": OFD + "mm",
            "BPD": BPD + "mm"
        }
        data.update(self.metaData)
        # Save the dictionary as a text file
        with open(self.fileName + "_metaData.txt", "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")

        # Draw the ellipse on the image
        cv2.ellipse(self.imageNumpy, self.ellipse_params, (0, 255, 0), 2)  # Green ellipse with thickness of 2

        # Save the image as a JPEG file
        cv2.imwrite(self.fileName + "annotation.jpeg",  self.imageNumpy)



    def __init__(self, parent=None):
        self.infoWindow = None
        self.modelFlag = False
        self.imageNumpy = np.array([])
        self.pixelSize = 0
        self.model = None
        self.pixelSizesDB = pd.DataFrame()
        self.fileName = None
        self.ellipse_params = None
        self.metaData = None

        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Reset
        self.reset()

        #Set UNIVPM LOGO
        self.LOGOscene = QGraphicsScene()
        self.ui.logoUNIVPM.setScene(self.LOGOscene)
        self.ui.logoUNIVPM.setStyleSheet("border: 0px")
        try:
            LOGO = cv2.imread("univpmLogo.png", cv2.IMREAD_GRAYSCALE)
            self.showImage(LOGO, self.ui.logoUNIVPM,None, True)
        except Exception as e:
            print(str(e))

        #Set DII LOGO
        self.DIILOGO = QGraphicsScene()
        self.ui.DIILOGO.setScene(self.DIILOGO)
        self.ui.DIILOGO.setStyleSheet("border: 0px")
        try:
            LOGO = cv2.imread("DIILOGO.png", cv2.COLOR_BGR2RGB)
            LOGO[:,:,[0,-1]] = LOGO[:,:,[-1,0]]
            self.showImage(LOGO, self.ui.DIILOGO,None, True)
        except Exception as e:
            print(str(e))

        #
        #Set br3in LOGO
        self.Br3inLOGO = QGraphicsScene()
        self.ui.Br3inLOGO.setScene(self.Br3inLOGO)
        self.ui.Br3inLOGO.setStyleSheet("border: 0px")
        try:
            LOGO = cv2.imread("br3inLOGO.png", cv2.COLOR_BGR2RGB)
            LOGO[:,:,[0,-1]] = LOGO[:,:,[-1,0]]
            self.showImage(LOGO, self.ui.Br3inLOGO,None, True)
        except Exception as e:
            print(str(e))

        # Create a QGraphicsScene and set it for the QGraphicsView
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        # Set the window title
        self.setWindowTitle("FetalBio-AI")

        # Set window icon
        self.setWindowIcon(QIcon('3.png'))

        # Load csv files
        self.create_DB()

        # load the model
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        self.load_the_network()

        self.ui.exit_Button.clicked.connect(self.close)
        self.ui.predict_Button.clicked.connect(self.make_prediction)
        self.ui.loadImage_Button.clicked.connect(self.select_files)
        self.ui.save_Button.clicked.connect(self.savePrediction)
        self.ui.newSub_Button.clicked.connect(self.newSub)
        self.ui.pixelSizeText.setPlaceholderText("Pixel Size")

        # Validator to constrain input
        validator = QRegularExpressionValidator("[0-9.]+")
        self.ui.pixelSizeText.setValidator(validator)


    def show_new_window(self):
        if not self.infoWindow or not self.infoWindow.isVisible():
            self.infoWindow = AnotherWindow()  # Store the instance in an attribute

            self.infoWindow.done_signal.connect(self.handle_done_signal)
            self.infoWindow.cancel_signal.connect(self.handle_cancel_signal)
            self.infoWindow.show()

    def handle_done_signal(self, returned_value):
        self.metaData = returned_value
        self.setEnabled(True)

        self.ui.IDtext.setText(f"Subject ID: {self.metaData['ID']}")
        self.ui.MOTHERAGEtext.setText(f"Mother's Age: {self.metaData['Age']}")
        self.ui.GAtext.setText(f"GA: {self.metaData['GAWeeks']} W, {self.metaData['GADays']} D")
        self.ui.EDDtext.setText(f"EDD: {self.metaData['EDD']}")

        self.ui.loadImage_Button.setEnabled(True)


    def newSub(self):
        self.show_new_window()
        self.setEnabled(False)

    def handle_cancel_signal(self, returned_value):
        self.setEnabled(True)

class AnotherWindow(QWidget):
    done_signal = Signal(dict)
    cancel_signal = Signal(bool)

    def __init__(self):
        self.metaData = None
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Set the window title
        self.setWindowTitle("Mother & Fetus Information")

        # Set window icon
        self.setWindowIcon(QIcon('3.png'))

        # Connect the textChanged signal to the BMI calculation method
        self.ui.WeightInput.textChanged.connect(self.calculate_bmi)
        self.ui.HeightInput.textChanged.connect(self.calculate_bmi)

        self.ui.done_Button.clicked.connect(self.done)
        self.ui.cancel_button.clicked.connect(self.cancel)

    def calculate_bmi(self):
        """Calculate BMI based on the entered weight and height."""
        try:
            weight = float(self.ui.WeightInput.text())
            height = float(self.ui.HeightInput.text())

            # Make sure height is not zero to avoid division by zero error
            if height > 0:
                bmi = weight / ((height / 100) ** 2)  # height is assumed in cm, so divided by 100
                self.ui.BmiInput.setText(f"{bmi:.2f}")  # Display BMI with 2 decimal places
            else:
                self.ui.BmiInput.clear()  # If height is invalid, clear the BMI input field
        except ValueError:
            # If the user inputs non-numeric values, just clear the BMI field
            self.ui.BmiInput.clear()

    def show_error_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Missing Fields")
        msg.setText("Please enter all mandatory fields")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def done(self):
        result = {}
        ID = self.ui.IdInput.text()
        if ID:
            result['ID'] = ID
        else:
            self.show_error_message()
            return None

        Age = self.ui.AgeInput.text()
        if Age.isdigit():
            result['Age'] = int(Age)
        else:
            self.show_error_message()
            return None

        Weight = self.ui.WeightInput.text()
        if Weight.isdigit():
            result['Weight'] = int(Weight)

        Height = self.ui.HeightInput.text()
        if Height.isdigit():
            result['Height'] = int(Height)

        BMI = self.ui.BmiInput.text()
        if BMI:  # Check if BMI is not empty
            result['BMI'] = float(BMI)  # Ensure BMI is passed as a float

        Gravidity = self.ui.GravidityBox.currentText()
        if Gravidity.lower() != "unknown":
            result['Gravidity'] = Gravidity

        Parity = self.ui.ParityBox.currentText()
        if Parity.lower() != "unknown":
            result['Parity'] = Parity

        if self.ui.DiabetesBool.isChecked():
            result['Diabetes'] = True
        else:
            result['Diabetes'] = False

        if self.ui.HypertensionBool.isChecked():
            result['Hypertension'] = True
        else:
            result['Hypertension'] = False


        if self.ui.PreeclampsiaBool.isChecked():
            result['Preeclampsia'] = True
        else:
            result['Preeclampsia'] = False

        GADays = self.ui.GaInputDays.text()
        if GADays.isdigit():
            result['GADays'] = int(GADays)
        else:
            self.show_error_message()
            return None

        GAWeeks = self.ui.GaInputWeeks.text()
        if GAWeeks.isdigit():
            result['GAWeeks'] = int(GAWeeks)
        else:
            self.show_error_message()
            return None

        sex = self.ui.sexBox.currentText()
        if sex.lower() != "unknown":
            result['sex'] = sex

        EDD = self.ui.EDDInput.dateTime().toString(self.ui.EDDInput.displayFormat())
        if EDD:
            result['EDD'] = EDD
        else:
            self.show_error_message()
            return None

        self.setEnabled(True)
        self.done_signal.emit(result)

        # Close the second window
        self.close()

    def cancel(self):
        self.cancel_signal.emit(False)
        self.close()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Set dark theme
    set_dark_theme()

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


