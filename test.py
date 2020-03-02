import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	Low_Red = np.array([161, 155, 84])
	High_Red = np.array([179, 255, 255])
	mask = cv2.inRange(hsv_frame, Low_Red, High_Red)

	cv2.imshow("Frame", frame)
	cv2.imshow("red mask", mask)
	
	key = cv2.waitKey(1)
	if key == 27:
		break