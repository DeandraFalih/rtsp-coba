import cv2
cap = cv2.VideoCapture("rtsp://192.168.100.146:8080/h264_pcm.sdp")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()