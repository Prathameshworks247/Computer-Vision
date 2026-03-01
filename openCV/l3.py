import cv2 

webcam = cv2.VideoCapture(0)


while True:
    ret, frame = webcam.read()
    
    if ret:
        cv2.imshow('frame',frame)
        if cv2.waitKey(40) & 0XFF == ord('q'):
            break
    
webcam.release()
cv2.destroyAllWIndows()