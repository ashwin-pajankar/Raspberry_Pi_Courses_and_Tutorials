import cv2

windowName = "Live Video Feed"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

filename = 'output.avi'

# http://www.fourcc.org/codecs.php
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')

framerate = 30
resolution = (640, 480)

Output = cv2.VideoWriter(filename, codec, framerate, resolution)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:

    ret, frame = cap.read()
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    Output.write(frame)

    cv2.imshow(windowName, frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()










    
