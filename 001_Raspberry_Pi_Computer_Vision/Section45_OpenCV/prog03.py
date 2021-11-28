import cv2

imgpath = "/home/pi/Dataset/4.2.03.tiff"
img = cv2.imread(imgpath, 0)

cv2.namedWindow('Mandrill', cv2.WINDOW_AUTOSIZE)

cv2.imshow('Mandrill', img)
cv2.waitKey(0)
cv2.destroyWindow('Mandrill')
