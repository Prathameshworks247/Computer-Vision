import cv2

img = cv2.imread('data/image.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('gray', gray)
cv2.imshow('rgb', rgb)
cv2.imshow('hsv', hsv)
cv2.waitKey(0)

cv2.imwrite('data/gray_image.jpeg', gray)
cv2.imwrite('data/rgb_image.jpeg', rgb)
cv2.imwrite('data/hsv_image.jpeg', hsv)

img.release()
gray.release()
rgb.release()
cv2.destroyAllWindows()