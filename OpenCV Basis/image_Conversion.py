### DAY 17 CHALLENGE ###
import cv2
image = cv2.imread("img.png")
Gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
HSV_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

## Printing out the shapes of all the 3 versions ##
"""Displaying the shape of the original image"""
print("Original Image Shape:",image.shape)

"""Displaying the shape of the grayscale image"""
print("Grayscale Image Shape:",Gray_image.shape)

"""Displaying the shape of the HSV image"""
print("HSV Image Shape:",HSV_image.shape)

##Displaying the images
"""The original image"""
cv2.imshow("Original Image in BGR",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""The Grayscale image"""
cv2.imshow("Grayscale Image",Gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""The HSV image"""
cv2.imshow("HSV Image",HSV_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
