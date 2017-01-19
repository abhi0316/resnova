import cv2
a=cv2.VideoCapture(0)
while True:
	ret,frame=a.read()
	cv2.imshow("vid",frame)
	if cv2.waitKey(1) & 0xFF == ord('c'):
 		break
cap.release()
cv2.destroyAllWindows()

