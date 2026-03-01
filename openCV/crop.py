import os
import cv2

img = cv2.imread('data/image.jpeg')

print(img.shape)

cropped_img = img[20:130,30:140]

cv2.imshow('frame',cropped_img)
cv2.waitKey(0)
img.release()
cropped_img.release()
cv2.destroyAllWIndows()