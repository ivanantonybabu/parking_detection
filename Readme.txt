<!-- ===================================================================================== -->
<!--                     Parking Slot Detection and Occupancy Estimation                   -->
<!-- ===================================================================================== -->

<h1 align="center">
🚗 Parking Slot Detection and Occupancy Estimation System
</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge"/>

<img src="https://img.shields.io/badge/YOLOv8-FF6F00?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Deep%20Learning-8A2BE2?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Computer%20Vision-009688?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>

</p>

<p align="center">

Automatic Parking Slot Detection using
<b>Computer Vision</b> +
<b>YOLOv8</b>

</p>

---

<h2>📖 Overview</h2>

<p>

This project presents a complete parking slot detection and occupancy estimation pipeline using a combination of classical computer vision techniques and deep learning.

The system automatically detects parking slots, identifies parked vehicles, determines slot occupancy, and generates both annotated visual outputs and statistical reports.

</p>

---

<h2>✨ Features</h2>

<table>

<tr>

<td width="50%">

✔ Automatic Parking Slot Detection

✔ YOLOv8 Vehicle Detection

✔ Occupancy Estimation

✔ HSV Color Filtering

</td>

<td width="50%">

✔ Yellow Zone Removal

✔ CSV Report Generation

✔ Annotated Output Images

✔ Lightweight Pipeline

</td>

</tr>

</table>

---

<h2>🧠 Technology Stack</h2>

<table>

<tr>

<th>Category</th>

<th>Technology</th>

</tr>

<tr>

<td>Programming</td>

<td>Python</td>

</tr>

<tr>

<td>Deep Learning</td>

<td>YOLOv8 (Ultralytics)</td>

</tr>

<tr>

<td>Computer Vision</td>

<td>OpenCV</td>

</tr>

<tr>

<td>Image Processing</td>

<td>HSV Filtering • Canny Edge Detection</td>

</tr>

<tr>

<td>Feature Detection</td>

<td>Hough Line Transform</td>

</tr>

<tr>

<td>Libraries</td>

<td>NumPy • Pandas</td>

</tr>

</table>

---

<h2>⚙ Methodology</h2>

<details open>

<summary><b>🔍 Image Preprocessing</b></summary>

<br>

- HSV Color Filtering
- Asphalt Extraction
- Noise Removal
- Yellow Zone Filtering

</details>

---

<details>

<summary><b>🚗 Parking Slot Detection</b></summary>

<br>

- Canny Edge Detection
- Hough Transform
- Contour Detection
- Polygon Approximation
- Bounding Box Generation
- Geometric Validation

</details>

---

<details>

<summary><b>🚘 Vehicle Detection</b></summary>

<br>

YOLOv8 Nano detects vehicles.

Vehicle bounding boxes are matched with parking slots using overlap analysis.

</details>

---

<details>

<summary><b>📊 Occupancy Estimation</b></summary>

<br>

Parking slots are classified as

🟥 Occupied

🟩 Available

using slot-to-vehicle overlap.

</details>

---

<h2>📂 Project Structure</h2>

```text
parking-slot-detection/

├── parking_detection.py
├── preprocessing1.txt
├── preprocessing2.txt
├── P2.png
├── annotated_output.jpg
├── output.csv
├── requirements.txt
└── README.md
```

---

<h2>📊 Output</h2>

<table>

<tr>

<th>Output</th>

<th>Description</th>

</tr>

<tr>

<td>Annotated Image</td>

<td>Parking slots marked as Occupied / Available</td>

</tr>

<tr>

<td>CSV Report</td>

<td>Total, Occupied and Available Slots</td>

</tr>

</table>

---

<h2>⚙ Parameter Optimization</h2>

<ul>

<li>HSV Threshold Tuning</li>

<li>Canny Threshold Optimization</li>

<li>Hough Transform Optimization</li>

<li>Contour Filtering</li>

<li>Bounding Box Validation</li>

<li>Vehicle-to-Slot IoU Thresholding</li>

</ul>

---

<h2>🚀 Installation</h2>

```bash
git clone https://github.com/ivanantonybabu/parking-slot-detection.git

cd parking-slot-detection

pip install -r requirements.txt
```

---

<h2>▶ Usage</h2>

```bash
python parking_detection.py
```

The script will automatically

- Detect Parking Slots
- Detect Vehicles
- Estimate Occupancy
- Save Annotated Image
- Export CSV Statistics

---

<h2>🎯 Project Context</h2>

<p>

Developed as part of the

<b>STAR-PNT Summer Internship Program</b>

at

<b>IIT Tirupati Navavishkar I-Hub Foundation (IITTNiF)</b>

under the Computer Vision Challenge.

</p>

---

<h2>📌 Future Work</h2>

- 🎥 Real-time Video Support
- 📹 CCTV Integration
- ☁ Cloud Deployment
- 🌐 Web Dashboard
- 📱 Mobile App
- 🛰 Drone-based Parking Monitoring

---

<h2>👨‍💻 Author</h2>

<p>

<b>Ivan Antony Babu</b>

<br><br>

Robotics & Embedded Systems Engineer

<br><br>

📧 ivanantonybabu@gmail.com

<br>

💻 https://github.com/ivanantonybabu

<br>

💼 https://www.linkedin.com/in/ivan-antony-babu

<br>

🌐 https://ivanantonybabu.github.io/My.personal.website/

</p>

---

<p align="center">

<b>⭐ If you found this project useful, consider starring the repository.</b>

</p>
