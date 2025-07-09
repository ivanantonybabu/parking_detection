
# 🚗 Parking Slot Detection and Occupancy Estimation System

This project presents a comprehensive deep learning and computer vision-based solution for detecting parking slots and identifying their occupancy status from an aerial/static image of a parking area.

## 📌 Overview

The system is capable of:
- Automatically detecting **parking slots** using **line marking analysis**, **geometric heuristics**, and **visual cues**.
- Identifying **occupied vs available** slots using **YOLOv8-based vehicle detection**.
- Ignoring **non-drivable** regions and **striped yellow no-parking zones** through advanced **color and feature-based filtering**.
- Generating annotated results as an image and a CSV report summarizing slot statistics.

---

## ⚙️ Techniques Used

### 🔍 Preprocessing
- **HSV Color Filtering**: Used to isolate asphalt areas and filter out yellow-striped zones.
- **Canny Edge Detection & Hough Transform**: To detect line markings and infer parking slot boundaries.
- **Contour Approximation & Bounding Box Estimation**: Applied on line-detected regions to extract rectangular slot candidates.
- **Slot Grid Mapping**: All slots are mapped to a structured `row-column` format for indexing and analysis.

### 🚘 Vehicle Detection
- YOLOv8 (Nano model) was used to detect vehicles.
- Only vehicles located **within identified slot regions** were considered to determine occupancy.
- High overlap thresholding was used to minimize false positives.

### 📏 Slot Filtering
- **Geometric tuning** was performed to reject small or irregular boxes.
- **Color signature filtering** was used to exclude striped or marked-out slots.

---

## 📁 Project Structure

📦 parking-slot-detection/
├── parking_detection.py # Main detection script
├── preprocessing1.txt # Available slot coordinates (YOLO format)
├── preprocessing2.txt # Occupied slot coordinates (YOLO format)
├── P2.png # Input parking lot image
├── annotated_output.jpg # Output image with annotations
├── output.csv # Summary statistics of slots
└── requirements.txt # Python dependencies



## 📊 Output

- **Annotated Image** (`annotated_output.jpg`): Highlights available slots in green and occupied ones in red.
- **CSV Report** (`output.csv`): Contains a summary:
  - Total number of slots
  - Number of occupied and available slots

---

## 🧪 Tuning & Optimization

- Multiple experiments were conducted to adjust thresholds for edge detection, HSV masks, and slot-to-vehicle IoU alignment.
- Parameters were hand-tuned to match real-world parking constraints and ensure robustness across various lighting and marking conditions.

---

## 🔧 Dependencies

Install dependencies with:

```bash
pip install -r requirements.txt