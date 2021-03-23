import cv2 #To read image / capture camera input(video)
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640) # 3 is for width
cap.set(4, 480) # 4 is for height
camera = True
data = ""

if cap is None or not cap.isOpened():
    print("Warning: unable to open video source")


else:
    while camera == True:
        success, frame = cap.read()
        for code in decode(frame):
            print(code.type)
            data = code.data.decode('utf-8')
            print("The data inside the QR code is: " + data)

        cv2.imshow("Scanner",frame)
        key = cv2.waitKey(20) & 0xFF


        if data!= "":
            key = 27

        if key == 27:
            cv2.destroyAllWindows()
            break

