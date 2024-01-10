import cv2

img = cv2.imread('images/qui-rm.png', 1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, img_binary = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

img_contour = cv2.drawContours(img, contours, -1, (0, 255, 0), 5)

cv2.imshow('Object Edge', img_contour)
cv2.waitKey(0)
cv2.imwrite('images/object.jpg', img_contour)
cv2.destroyAllWindows()