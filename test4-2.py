import cv2

face= cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
camera = cv2.VideoCapture(0)
while True:
    read_ok,frame = camera.read()
    Leabels=[]
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face.detectMultiScale(gray)
    for(x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff ==ord ('z'):
        break

camera.release()
cv2.destroyAllWindows()