import cv2

image_path = 'images/qui.jpg'
image = cv2.imread(image_path, 0)

th = 150
th_max = 255

res, img_bin = cv2.threshold(image, th, th_max, cv2.THRESH_BINARY)

cv2.imshow('Binary Image', img_bin)
cv2.waitKey(0)
cv2.imwrite('images/bin.jpg', img_bin)
cv2.destroyAllWindows()