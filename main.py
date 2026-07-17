# import numpy as np

import cv2 as cv
import numpy as np
# # from matplotlib import pyplot as plt
# # Load image data from file, then display the array
# img = cv.imread("baseball.jfif")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray = cv.medianBlur(gray, 5)
# rows = gray.shape[0]

# circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
#                           param1=35, param2=30, 
#                           minRadius=1, maxRadius=30)
# if circles  is not None:
#     circles = np.uint16(np.around(circles)) 
#     for i in circles[0, :]:
#         center = (i[0], i[1])
#         cv.circle(img, center, 1, (0, 100, 100), 3)
#         radius = i[2]
#         cv.circle(img, center, radius, (255, 0, 255), 3)                        
# cv.imshow('test',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

cap = cv.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream or file")
    exit()

while True:
    # Read a new frame from the camera
    # ret: a boolean indicating if the frame was successfully read
    # frame: the image frame itself
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame")
        break

    # Display the captured frame in a window named "Live Camera Feeqd"
    cv.imshow('Live Camera Feed', frame)

    # Break the loop when the 'q' key is pressed
    # cv.waitKey(1) waits for 1ms for a key event
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv.destroyAllWindows()