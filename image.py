import cv2
a=cv2.imread("/home/abhi/Pictures/IMG_342423.png")
a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)

cv2.imshow("img",a)
cv2.waitKey(0)
cv2.destroyAllWindows()
