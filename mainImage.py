# CPCS331 - Artificial Intelligence
# Students: Moayad Batwa - Hossam Amasha

from ultralytics import YOLO
import cv2

# Load a model
model = YOLO('YOLOv11n.torchscript')  # load a pretrained model
#model = YOLO('YOLOv11m.torchscript')  # load a pretrained model


# Use the model
results = model('images/3.jpg', show=True)  # show an image


cv2.waitKey(0)