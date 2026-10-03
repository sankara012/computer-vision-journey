##Day 15
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("img.png")
"""Display the image in RGB format"""
#plt.imshow(image)
#plt.show()

"""Converting the image from BGR to RGB format"""
imgConverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("image Demo",imgConverted)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""Converting the image from BGR to RGB format using slicing method"""
"""imgsliced = image[:, :, ::-1]
cv2.imshow("image Demo BGR to RGB",imgsliced)
cv2.waitKey(0)"""


"""The image in BGR format"""
cv2.imshow("image Demo in BGR",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#The image shape
print("The image shape is:",image.shape)
print("The image type is:",type(image))
print("The image data type is:",image.dtype)
print("The image size is:",image.size)
