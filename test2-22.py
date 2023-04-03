import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests # عشان نقدر نستدعي من النت ومايكون فيه مشاكل
from PIL import Image

img = Image.open(requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg', stream=True).raw)
img= img.resize((450,250))# غيرنا الحجم
img_arr= np.array(img)    # نحول الصوره لمصفوفه

gray= cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)# غيرنا من الالوان الى دراجات الرمادي عشان تكون قيمها صغيره

blur= cv2.GaussianBlur(gray, (5,5),0)         #  يسوي تحسين معالجة للصوره ما يكون فيها تشويش  
Image.fromarray(blur)

dilated= cv2.dilate(blur, np.ones((3,3))) # نوسع الصوره
Image.fromarray(dilated)

kernel= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))#أحد اساليب توسيع الصوره عشان نملي وحدات البيكسل ويمنع من تآكل الصوره
closing= cv2.morphologyEx(dilated,cv2.MORPH_CLOSE,kernel)#عشان يصير المعالجة للصوره اسهل 
Image.fromarray(closing)

Car_SRC = 'haarcascade_car.xml'#  مدربه للكشف عن السياراتdata
car = cv2.CascadeClassifier(Car_SRC)
cars = car.detectMultiScale(closing, 1.1 ,1)

cnt =0 # عشان يحسب عدد السيارات
for(x,y,w,h) in cars: 
    cv2.rectangle(img_arr,(x,y),(x+w,y+h),(255,0,0),2) # يسوي مستطيل لكل سياره الاثنين الاخيره لسمك المستطيل
    print(cnt,"Cars")
    Image.fromarray(img_arr)


cv2.imshow('image',img_arr) # يظهر الصوره
cv2.waitKey()
cv2.destroyAllWindows()