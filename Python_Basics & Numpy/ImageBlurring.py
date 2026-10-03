import numpy as np
import matplotlib.pyplot as plt
"""PHASE I"""
size=100
img = np.zeros((size,size),dtype = np.float32)
img[30:70,30:70] = 200
Gaussian_noise = np.random.normal(0,30,(size,size))
noisy_img = np.clip(img + Gaussian_noise, 0, 255).astype(np.uint8)

"""PHASE II"""
def manual_blur(image, k=1):
  output = np.zeros_like(image, dtype=np.float32)
  h, w = image.shape
  for i in range(h):
    for j in range(w):
      i_min, i_max = max(0, i-k), min(h, i+k+1)
      j_min, j_max = max(0, j-k), min(w, j+k+1)

      neighborhood = image[i_min:i_max, j_min:j_max]
      output[i, j] = neighborhood.mean()
  return output.astype(np.uint8)
blurred = manual_blur(noisy_img, k=2)

fig, axes = plt.subplots(1, 2, figsize=(8,4))
axes[0].imshow(noisy_img, cmap='gray'); axes[0].set_title("Noisy Original")
axes[1].imshow(blurred, cmap='gray'); axes[1].set_title("Your manual_blur() result")
plt.tight_layout()
print("Ran successfully. Output shape:", blurred.shape, "dtype:", blurred.dtype)