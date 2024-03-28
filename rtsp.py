import cv2
cap = cv2.VideoCapture("rtsp://admin:zxcSaas2024@192.168.100.158:554/H.264")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()