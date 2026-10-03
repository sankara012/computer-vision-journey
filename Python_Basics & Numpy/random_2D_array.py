import numpy as np
noise_frame = np.random.randint(0, 256, size=(200, 200), dtype=np.uint8)
normalized_frame = np.clip(noise_frame.astype(np.float32) * 1.2 + 30, 0, 255).astype(np.uint8)
thresholded_frame = np.where(normalized_frame > 128, 255, 0)
target_count = np.sum(thresholded_frame == 255)
mean_orig = np.mean(noise_frame)
mean_thresholded = np.mean(thresholded_frame)
print(f"Origin Mean:{mean_orig}")
print(f"Threshold Mean: {mean_thresholded}")
print(f"Original Count: {target_count}")
print(noise_frame)

