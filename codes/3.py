import cv2

path = 'images/qui.jpg'
i = cv2.imread(path, 0)

i_max = 255

i_binary = cv2.adaptiveThreshold(i, i_max, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 39, 2)

cv2.imshow('Optimize Binary Image', i_binary)
cv2.waitKey(0)
cv2.imwrite('images/optimize.jpg', i_binary)
cv2.destroyAllWindows()