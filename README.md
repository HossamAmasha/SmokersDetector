# 🚭 Smokers Detector using YOLOv11

A computer vision project built with YOLOv11 to detect **smokers and smoking-related objects** in public spaces. Developed for the **CPCS331 course** at **King Abdulaziz University**.

---

## 📌 Project Summary

This system identifies:
- Person  
- Cigarette  
- Vape  
- Smoke

It is intended to help monitor **restricted or anti-smoking areas** like hospitals, shopping malls, and public transport by automatically identifying smoking-related activity in images or video feeds.

---

## 📊 Model Details

- **Model Architecture**: YOLOv11 (Ultralytics)
- **Framework**: Python, PyTorch, Ultralytics
- **Training Platform**: Google Colab
- **Dataset Source**: [Roboflow - Smoking Person Detection v2](https://universe.roboflow.com/visionwork/smoking_person/dataset/2)

### 🔧 Training Setup

- Input Image Size: `640x640`
- Epochs: `20`
- Data Augmentation: Flipping, rotation, resizing
- Train/Val/Test Split: 1446 / 156 / 52 images
- Annotation Format: YOLO `.txt` files

### 🧪 Evaluation Metrics

| Metric              | Score  |
|---------------------|--------|
| **mAP@0.5**         | 0.659  |
| **mAP@0.5:0.95**    | 0.404  |
| AP (Person)         | 0.975  |
| AP (Cigarette)      | 0.761  |
| AP (Vape)           | 0.524  |
| AP (Smoke)          | 0.376  |

### 🔍 Key Libraries Used

- `ultralytics`
- `torch`
- `numpy`
- `opencv-python`
- `matplotlib`

---

## 🚀 Getting Started
### 1. Unzip the Trained Models
```bash
Select the TrainedModels Files and use Extract Here
```
### 2. Install Dependencies
```bash
pip install ultralytics opencv-python matplotlib numpy
```
### 3. Testing it on a Video

```bash
Put the video you want to test in the video file
(SmokersDetector/video)
```
---

## 🧠 Challenges Faced

- Detecting **small objects** like cigarettes and vapes
- Handling **class imbalance**
- Ensuring **annotation consistency**
- Model struggling with **smoke detection** due to its vague appearance

---

## 🎯 Future Work

- Improve model performance on `smoke` and `vape` classes
- Add real-time video inference
- Collect more balanced and diverse data
- Optimize the model for deployment on edge devices

---

## 👥 Authors

- **Hossam Amasha**  
- **Moayad Batwa**

