import cv2

image =cv2.imread("myp.jpg")
#print(image) #يطبع مصفوفات لبكسلات الصوره
#print(image.shape)  #يطبع ابعاد الصوره 

#يحول الصوره لتدرجات الرمادي
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('ghaida',gray)# يظهر الصوره
i=cv2.waitKey(0)         #عشان اذا ضغطت اكس يقفل 
 
cv2.imwrite("myp_gray.jpg" , gray) # ويحفظها بهذا الاسمgrayبياخذ الصوره من

if i==27 or i==('c'): #ويقفل الصوره cاذا ضغطت 27 او
   cv2.destroyAllWindows()




