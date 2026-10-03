###RECAPS
#Day5
import numpy as np
sensor_frame = np.zeros((460, 500,3), dtype=np.uint8) # Example: creates an uninitialized array of the specified shape
print(sensor_frame.shape)
roi = sensor_frame[200:500,0:200].copy()
#print(roi)
target_masked = (roi>220) & (roi<255)
#print(target_masked)
spot_checked = roi[[10,50,95],[20,80,110]]
#print("***Spot Checked ***")
#print(spot_checked)
##Brodacasing
image_color = sensor_frame * [1.2,1.0,8.0]
img_addititon = sensor_frame + 80
sum = np.sum(img_addititon)
print("***Sum***")
print(sum)
#print("*** Color enhenced ***")
#print(image_color)
A = img_addititon.sum(axis=0)
print("***Sum of columns***")
print(A)
