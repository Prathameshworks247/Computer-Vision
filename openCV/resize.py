import cv2 

import os 

img = cv2.imread('data/image.jpeg')

print(img.shape)

resized = cv2.resize(img, (1000,1000))

cv2.imshow('img',resized)
cv2.waitKey(0)

img.release()
resized.release()
cv2.destroyAllWIndows()