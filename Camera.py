import cv2 as cv
from ultralytics import YOLO
import math
import time
yolo = YOLO("yolov8n.pt")



def find_camera():
    for index in range(5):  # Check indexes 0 through 4
        cap = cv.VideoCapture(index)
        if cap.isOpened():
            print(f"Camera found at index: {index}")
            cap.release()
            return index
        cap.release()
    print("No camera found.")
    return None

working_index = find_camera()


cap = cv.VideoCapture("Test.mp4")

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream or file")
    exit()
frame_count = 0
pastmidx = 0
pastmidy = 0
framecap = 0
start = time.time()
while True and framecap <= 800:
    framecap += 1
    # Read a new frame from the camera
    # ret: a boolean indicating if the frame was successfully read
    # frame: the image frame itself
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame")
        break
    results = yolo.track(frame, stream=True)
    for result in results:
        class_names = result.names 
        for box in result.boxes:
            cls = int(box.cls[0])
            class_name = class_names[cls]
            if box.conf[0] > 0.4 and class_name == 'cell phone':
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                currmidx = (x2 - x1) / 2 
                currmidy = (y2 - y1) / 2
                distance = math.sqrt((currmidx - pastmidx)**2 + (currmidy - pastmidy)**2)
                pastmidy = currmidy
                pastmidx = currmidx
                print(distance)
                # cls = int(box.cls[0])
                # class_name = class_names[cls]

                conf = float(box.conf[0])

                cv.rectangle(frame, (x1 , y1), (x2, y2), 2)

                cv.putText(frame, f"{class_name} {conf:.2f} {distance}",
                            (x1, max(y1 - 10, 20)), cv.FONT_HERSHEY_SIMPLEX,
                            0.6, 2)

                
    # Display the captured frame in a window named "Live Camera Feed"
    cv.imshow('Live Camera Feed', frame)

    # Break the loop when the 'q' key is pressed
    # cv.waitKey(1) waits for 1ms for a key event
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    # if frame_count > 20:
    #     break
    # frame_count += 1

end = time.time()
seconds = end - start
fps = 120 / seconds
print(fps)