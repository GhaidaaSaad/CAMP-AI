#يتعرف على زواياالكلام
import cv2
import numpy as np
import matplotlib.pyplot as plt

imge = cv2.imread("sy.png")
gray= cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)

plt.imshow(imge),plt.show()    #بهذي المكتبه تظهر الصوره بابعاد س و ص
#plt.waitforbuttonpress()  #عشان يظهر الصوره مع السطر اللي قبله يحافظ على الصوره

corner= cv2.goodFeaturesToTrack(gray, 30, 0.01, 10)
corner= np.int0(corner)

for i in corner :
    x,y =i.ravel()
    cv2.circle(imge, (x,y), 3, 50, -1)

plt.imshow(imge)
plt.waitforbuttonpress()