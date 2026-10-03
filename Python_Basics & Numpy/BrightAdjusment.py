import numpy as np
img = np.array([[50,100,150],
                [80,120,160]
                ])
print(img)
print(img.shape)
print(f"Original image size: {img.size}")
bright_img = img + 20
high_Contrast = img * 1.5
print(f"Brightness Image: {bright_img}")
print(f"Brightness Image shape: {bright_img.shape}")
print(f"High contrast image: {high_Contrast}")
print(f"High contrast Image shape: {high_Contrast.shape}")
print(f"Brightness Image size: {bright_img.size}")
avg_brightness = np.average(bright_img)
print(f"Average Brightness Image: {avg_brightness:.2f}")
avg_brightnessImg = np.average(img)
print(f"Average Brightness Image: {avg_brightnessImg:.2f}")
img_contrastSTD = np.std(high_Contrast)
print(f"Image contrast STD: {img_contrastSTD:.2f}")
darkest_pixel = np.min(bright_img)
print(f"Darkest Pixel of bright_img: {darkest_pixel:.2f}")
brightest_pixel = np.max(bright_img)
print(f"Brightest_pixel of bright_img: {brightest_pixel:.2f}")