import cv2
cap = cv2.VideoCapture("video.mp4")
#cap = cv2.VideoCapture("rtsp://103.131.105.122:1935/cctv-public/ViewNolKilo.stream")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()