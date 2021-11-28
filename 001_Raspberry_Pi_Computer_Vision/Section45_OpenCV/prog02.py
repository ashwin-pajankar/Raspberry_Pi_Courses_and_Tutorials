import cv2

imgpath = "/home/pi/Dataset/4.2.03.tiff"
img = cv2.imread(imgpath)

outpath = "/home/pi/test.png"
cv2.imwrite(outpath, img)
