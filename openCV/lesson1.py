import cv2

img = cv2.imread('data/image.jpeg')
print(img.shape)

# cv2.imwrite('data/lora.png', img)

cv2.imshow('image',img)
cv2.waitKey(0)