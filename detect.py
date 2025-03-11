import cv2
import easyocr
import numpy as np

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Open webcam
cap = cv2.VideoCapture(0)

# Create a text file to store detected license plates
output_file = "detected_plates.txt"

with open(output_file, "w") as file:
    file.write("Detected License Plates:\n")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect edges using Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    
    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Approximate contour to get a polygonal shape
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        
        # If contour has 4 sides, it could be a license plate
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            plate_region = frame[y:y+h, x:x+w]
            
            # Perform OCR on the detected plate
            text_results = reader.readtext(plate_region)
            
            for (bbox, text, prob) in text_results:
                if prob > 0.5:  # Confidence threshold
                    print(f"Detected Plate: {text}")
                    
                    # Save to file
                    with open(output_file, "a") as file:
                        file.write(text + "\n")
                    
                    # Draw bounding box and text on the frame
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Show output frame
    cv2.imshow("License Plate Detection", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
