# يحدد زوايا الأشكال
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("rec.png")
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray= np.float32(gray)# يحول الصوره لمصفوفه

des= cv2.cornerHarris(gray,2, 5, 0.07)
des= cv2.dilate(des, None)
img[des >0.01 * des.max()]=[20, 10,20]

plt.imshow(img)  # cv2.imshow('imag',imd)
plt.waitforbuttonpress()
