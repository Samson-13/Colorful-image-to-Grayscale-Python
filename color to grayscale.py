import cv2 as cv

colorImg = cv.imread('color.jpeg')

# Shows the original colorful image
cv.imshow('Original Image', colorImg)

# Convert to Grayscale
convToGray = cv.cvtColor(colorImg, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', convToGray)

cv.waitKey(0)