import cv2

# Load original image (this is in BGR by default)
dolphin_bgr_correct = cv2.imread("img.png")

# Convert to RGB (this will look "wrong" if displayed with cv2.imshow,
# since cv2.imshow expects BGR)
dolphin_rgb_wrong = cv2.cvtColor(dolphin_bgr_correct, cv2.COLOR_BGR2RGB)

# --- Save both versions to disk ---
cv2.imwrite("dolphin_bgr_correct.png", dolphin_bgr_correct)
cv2.imwrite("dolphin_rgb_wrong.png", dolphin_rgb_wrong)
print("Both files saved.")

# --- Reload both files FRESH from disk (new variables) ---
loaded_correct = cv2.imread("dolphin_bgr_correct.png")
loaded_wrong = cv2.imread("dolphin_rgb_wrong.png")

# --- Display the reloaded versions ---
# cv2.imshow always expects BGR data to display correctly
cv2.imshow("Reloaded: dolphin_bgr_correct.png", loaded_correct)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Reloaded: dolphin_rgb_wrong.png", loaded_wrong)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---