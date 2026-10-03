###Day4-5 challenge
import numpy as np
from PIL import Image
image = Image.open("./img.png")
print(f"The actual size of the image is: {image.size}")
img_array = np.array(image)
print(f"The actual dimension of the image is: {img_array.ndim}")
print(f"The new size of the image with array: {img_array.shape}")
#Image dimension & type
print(f"Array Image Type: {img_array.dtype}")
print(f"Array Image dimension:{img_array.ndim}")
height, width, channels = img_array.shape
print(f"Height:{height}")
print(f"Width: {width}")
print(f"Channels: {channels}")

###Region of Interest
startH = int(height * 1/4)
endH   = int(height * 3/4)
print(startH,endH)
startW = int(width * 1/4)
endW   = int(width * 3/4)
print(startW,endW)
roi = img_array[startH:endH,startW:endW]
print(roi)
print(f"ROI shape: {roi.shape}")

##Saving the image
roi_image = Image.fromarray(roi)
roi_image.save("Image.png")
roi_image.show()
print("Original pixel:", img_array[startH, startW])

roi[0, 0] = [255, 0, 0]
#Image.fromarray(img_array).show()
print("Original pixel after modification:", img_array[startH, startW])

darkest_pixel = np.min(img_array)
print(f"Darkest Pixel of the image array: {darkest_pixel:.2f}")
brightest_pixel = np.max(img_array)
print(f"Brightest_pixel of the image array: {brightest_pixel:.2f}")
avg_brightness = np.average(img_array)
print(f"Average Brightness of the image array: {avg_brightness:.2f}")
bright_img = img_array + 70
print(f"the new array image is {bright_img}")

green_channel = img_array[:,:,1]
print(f"green_channel: {green_channel}")

red_intensity = img_array[:,:,2]
print(f"red intensity: {red_intensity}")

mean_bright = np.mean(green_channel)
print(f"mean_bright: {mean_bright:.2f}")