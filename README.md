# License Plate Detection (Real-time)

## Overview
This project uses OpenCV and EasyOCR to detect and recognize license plates from a real-time webcam feed. The detected license plates are saved in a text file.

## Prerequisites
Ensure you have Python installed on your system.

### Install Dependencies
Run the following command to install the required libraries:
```bash
pip install opencv-python numpy easyocr
```

## How It Works
1. Captures video from the webcam.
2. Converts frames to grayscale and detects edges.
3. Identifies potential license plates using contour detection.
4. Extracts the plate region and applies Optical Character Recognition (OCR) using EasyOCR.
5. Displays detected license plates on the screen.
6. Saves all detected license plates to `detected_plates.txt`.

## Usage
Save the provided Python script as `detect.py` and run:
```bash
python detect.py
```
Press `q` to exit the program.

## Output
- The detected license plates will be displayed on the screen.
- All detected plates will be saved in `detected_plates.txt`.

## Future Improvements
- Enhance detection using deep learning models like YOLO.
- Filter results to improve accuracy.
- Store detected plates in a database instead of a text file.

## License
This project is open-source and free to use.

Thank you✨

