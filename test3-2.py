import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cape = cv2.VideoCapture('C:/Users/ghaid/OneDrive/Documents/AI/IMG_7668 (1).MP4')

while True:
    _,img= cape.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces= face.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
         cv2.rectangle(img, (x,y),(x+y,y+h),(255,0,0),3)
    cv2.imshow("video",img)

    k= cv2.waitKey(30) & 0xff
    if k==27:  #  يقفلEscاذا ضغطنا 
        break
    
cape.release()
