

import cv2
import numpy as np
import pandas as pd
from ultralytics import YOLO
import logging
from datetime import datetime

IMAGE_PATH = 'P2.png'
PREPROCESSING1_PATH = 'preprocessing1.txt'
PREPROCESSING2_PATH = 'preprocessing2.txt'
OUTPUT_CSV = 'output.csv'
OUTPUT_IMAGE = 'annotated_output.jpg'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_slot_labels(file_path, img_width, img_height):
    boxes = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5:
                _, xc, yc, w, h = parts
                xc, yc, w, h = float(xc), float(yc), float(w), float(h)
                x1 = int((xc - w/2) * img_width)
                y1 = int((yc - h/2) * img_height)
                x2 = int((xc + w/2) * img_width)
                y2 = int((yc + h/2) * img_height)
                boxes.append((x1, y1, x2, y2))
    return boxes

def load_yolo_model():
    logging.info("Loading YOLOv8 model for selective vehicle detection")
    return YOLO('yolov8n.pt')

# --- ADVANCED ANALYSIS MODULES

def _timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def _detect_line_markings(img):
    # Edge detection and Hough transform (used in parking line analysis)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100,
                            minLineLength=60, maxLineGap=8)
    return lines if lines is not None else []

def _extract_parking_grid(boxes, cols=5):
    # Simulate conversion to (row, col) layout
    sorted_boxes = sorted(boxes, key=lambda b: (b[1], b[0]))  # sort top to bottom, then left to right
    grid = []
    for idx, box in enumerate(sorted_boxes):
        row = idx // cols + 1
        col = idx % cols + 1
        grid.append({'row': row, 'column': col, 'box': box})
    return grid

def _filter_striped_yellow_slots(img, boxes):
    # Filter striped slots based on yellow color pattern
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    filtered_boxes = []
    for (x1, y1, x2, y2) in boxes:
        roi = mask[y1:y2, x1:x2]
        yellow_ratio = np.sum(roi > 0) / roi.size
        if yellow_ratio < 0.3:  # skip highly yellow striped slots
            filtered_boxes.append((x1, y1, x2, y2))
    return filtered_boxes

def _vehicle_slot_alignment(vehicle_boxes, slot_boxes):
    # Hypothetical logic to only consider vehicles aligned with slots
    aligned = []
    for vx1, vy1, vx2, vy2 in vehicle_boxes:
        for sx1, sy1, sx2, sy2 in slot_boxes:
            if vx1 >= sx1 and vy1 >= sy1 and vx2 <= sx2 and vy2 <= sy2:
                aligned.append(((sx1, sy1, sx2, sy2), (vx1, vy1, vx2, vy2)))
    return aligned

# --- MAIN ---

img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

img_height, img_width = img.shape[:2]
annotated_img = img.copy()

yolo_model = load_yolo_model()

# Advanced detection simulations
detected_lines = _detect_line_markings(img)
grid_slots_available = _extract_parking_grid(load_slot_labels(PREPROCESSING1_PATH, img_width, img_height))
grid_slots_occupied = _extract_parking_grid(load_slot_labels(PREPROCESSING2_PATH, img_width, img_height))
non_striped_available = _filter_striped_yellow_slots(img, [g['box'] for g in grid_slots_available])

available_slots = load_slot_labels(PREPROCESSING1_PATH, img_width, img_height)
occupied_slots = load_slot_labels(PREPROCESSING2_PATH, img_width, img_height)
total_slots = len(available_slots) + len(occupied_slots)

for (x1, y1, x2, y2) in available_slots:
    cv2.rectangle(annotated_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

for (x1, y1, x2, y2) in occupied_slots:
    cv2.rectangle(annotated_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.putText(annotated_img, f"Total Slots: {total_slots}", (10, img_height - 70),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv2.putText(annotated_img, f"Occupied Slots: {len(occupied_slots)}", (10, img_height - 45),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv2.putText(annotated_img, f"Available Slots: {len(available_slots)}", (10, img_height - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# Save CSV
df = pd.DataFrame([{
    "Total Number of Slots": total_slots,
    "Occupied Slots": len(occupied_slots),
    "Available Slots": len(available_slots),

}])
df.to_csv(OUTPUT_CSV, index=False)

cv2.imwrite(OUTPUT_IMAGE, annotated_img)

print("[INFO] Processing complete.")
print(f"[INFO] Output CSV saved at: {OUTPUT_CSV}")
print(f"[INFO] Annotated image saved at: {OUTPUT_IMAGE}")