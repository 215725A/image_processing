import cv2

image = cv2.imread('images/cup.jpg')

height = image.shape[0]
width = image.shape[1]

image_copy1 = image.copy()
image_copy1 = cv2.cvtColor(image_copy1,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(image_copy1,95,255,cv2.THRESH_BINARY)
contours1, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, contours1, -1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('Drawn contours', image)
cv2.imwrite('images/edge.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()