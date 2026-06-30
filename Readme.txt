# 🚗 Parking Slot Detection and Occupancy Estimation System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

## 📖 Overview

The **Parking Slot Detection and Occupancy Estimation System** is a computer vision and deep learning-based solution designed to automatically detect parking spaces and determine their occupancy status from aerial or static parking lot images.

The system combines **traditional computer vision techniques** with **YOLOv8 object detection** to accurately identify parking slots, classify them as **occupied** or **vacant**, and generate both visual and statistical outputs.

---

## ✨ Features

- 🚗 Automatic parking slot detection
- 🤖 YOLOv8-based vehicle detection
- 📍 Occupancy estimation (Occupied / Available)
- 🟡 Automatic removal of yellow-striped no-parking zones
- 📊 CSV report generation
- 🖼️ Annotated output image generation
- ⚡ Fast and lightweight processing pipeline

---

## 🛠 Methodology

### 1️⃣ Image Preprocessing

The input parking lot image undergoes several preprocessing steps to improve feature extraction.

- HSV Color Space Filtering
- Noise Reduction
- Asphalt Region Extraction
- Yellow No-Parking Zone Removal

---

### 2️⃣ Parking Slot Detection

Parking slots are identified using classical computer vision techniques.

Techniques used include:

- Canny Edge Detection
- Hough Line Transform
- Contour Detection
- Polygon Approximation
- Bounding Box Generation
- Geometric Validation

The detected slots are indexed using a structured **Row–Column Mapping** for easier analysis.

---

### 3️⃣ Vehicle Detection

Vehicle detection is performed using the **YOLOv8 Nano** object detection model.

The detected vehicle bounding boxes are compared with the detected parking slots.

Only vehicles whose bounding boxes significantly overlap a parking slot are considered valid occupants.

---

### 4️⃣ Occupancy Estimation

Each parking slot is classified as:

- 🟥 Occupied
- 🟩 Available

based on the overlap between parking slot regions and detected vehicles.

---

### 5️⃣ Slot Filtering

To improve detection accuracy, several filtering strategies were applied.

- Geometric filtering
- Minimum area thresholding
- Aspect ratio validation
- Color-based filtering
- False-positive suppression

These techniques remove invalid parking slot candidates and improve robustness under different lighting conditions.

---

## 🧠 Technologies Used

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Deep Learning | YOLOv8 (Ultralytics) |
| Computer Vision | OpenCV |
| Image Processing | HSV Filtering, Canny Edge Detection |
| Feature Detection | Hough Transform |
| Data Processing | NumPy, Pandas |

---

## 📂 Project Structure

```text
📦 parking-slot-detection
│
├── parking_detection.py          # Main detection pipeline
├── preprocessing1.txt            # Available slot coordinates
├── preprocessing2.txt            # Occupied slot coordinates
├── P2.png                        # Input parking lot image
├── annotated_output.jpg          # Annotated output image
├── output.csv                    # Slot statistics
├── requirements.txt              # Required Python packages
└── README.md
```

---

## 📊 Output

### 🖼 Annotated Image

The generated image contains:

- 🟩 Green Bounding Boxes → Available Parking Slots
- 🟥 Red Bounding Boxes → Occupied Parking Slots

---

### 📈 CSV Report

The generated CSV file contains

| Parameter | Description |
|-----------|-------------|
| Total Slots | Total parking slots detected |
| Occupied Slots | Number of occupied slots |
| Available Slots | Number of available slots |
| Occupancy Percentage | Percentage occupancy |

---

## ⚙ Parameter Optimization

Multiple experiments were conducted to determine the optimal values for:

- HSV Thresholds
- Canny Edge Thresholds
- Hough Transform Parameters
- Contour Area Threshold
- Bounding Box Dimensions
- Vehicle-to-Slot IoU Threshold

The parameters were manually optimized to improve detection performance under varying parking layouts and illumination conditions.

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/parking-slot-detection.git
```

Move into the project directory

```bash
cd parking-slot-detection
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

Run the detection pipeline using

```bash
python parking_detection.py
```

The script will automatically:

- Detect parking slots
- Detect vehicles
- Estimate occupancy
- Save the annotated image
- Export parking statistics to a CSV file

---

## 📌 Future Improvements

- 🎥 Real-time video support
- 📹 CCTV camera integration
- 🌐 Web dashboard
- 📱 Mobile application
- 🚙 Multi-class vehicle detection
- ☁ Cloud deployment
- 🛰 Drone-based parking monitoring

---

## 👨‍💻 Author

**Ivan Antony Babu**

Robotics & Embedded Systems Engineer

- GitHub: https://github.com/ivanantonybabu
- Portfolio: https://ivanantonybabu.github.io/My.personal.website/
- LinkedIn: https://www.linkedin.com/in/ivan-antony-babu

---

## 📄 License

This project is intended for academic and research purposes.
