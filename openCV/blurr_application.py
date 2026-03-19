import cv2 

img = cv2.imread('data/noise.jpeg')


blur = cv2.blur(img, (5,5))
gauss_blur = cv2.GaussianBlur(img, (5,5), 0)
median_blur = cv2.medianBlur(img, 5)

cv2.imshow('img', img)
cv2.imshow('blur', blur)
cv2.imshow('gauss_blur', gauss_blur)
cv2.imshow('median_blur', median_blur)
cv2.waitKey(0)
img.release()
blur.release()
median_blur.release()
gauss_blur.release()
cv2.destroyAllWindows()
