import numpy as np
import matplotlib.pyplot as plt

# 1. Create a dummy "Image" (8x8 Grid)
# Let's simulate an edge: The left side is dark (low values), right side is bright (high values).
# This represents a vertical edge in a photo.
image = np.array([
    [10, 10, 10, 10, 200, 200, 200, 200],
    [10, 10, 10, 10, 200, 200, 200, 200],
    [10, 10, 10, 10, 200, 200, 200, 200],
    [10, 10, 10, 10, 200, 200, 200, 200],
    [10, 10, 10, 10, 200, 200, 200, 200],
    [10, 10, 10, 10, 200, 200, 200, 200],
    [10, 10, 10, 10, 200, 200, 200, 200],
    [10, 10, 10, 10, 200, 200, 200, 200]
], dtype=np.uint8)

# 2. Compute the Integral Image
# OpenCV has a function cv2.integral, but here is the raw math using numpy cumsum
# We calculate cumulative sum along rows, then along columns.
integral_image = np.cumsum(np.cumsum(image, axis=0), axis=1)

# Pad with zeros (standard practice for integral images to handle top/left boundaries easier)
H, W = image.shape
II = np.zeros((H + 1, W + 1))
II[1:, 1:] = integral_image

print("Original Image Sample (Top Left vs Top Right):")
print(f"Dark Pixel: {image[0][0]}, Bright Pixel: {image[0][4]}\n")

# 3. Define a Function to Calculate Area Sum using 4 Corners (O(1) complexity)
def get_rect_sum(ii, x, y, w, h):
    """
    ii: Integral Image
    x, y: Top-left corner of the rectangle
    w, h: Width and Height of the rectangle
    """
    A = ii[y, x]           # Top-left corner
    B = ii[y, x + w]       # Top-right corner
    C = ii[y + h, x]       # Bottom-left corner
    D = ii[y + h, x + w]   # Bottom-right corner
    
    # The Magic Formula
    return D - B - C + A

# 4. Simulate a Haar Feature Check (Vertical Edge Detection)
# We will compare a Left Rectangle (at x=2) vs a Right Rectangle (at x=4)
# Both are 2 pixels wide and 4 pixels tall.

# Left Rect (should be in the dark area)
left_sum = get_rect_sum(II, x=2, y=2, w=2, h=4)

# Right Rect (should be in the bright area)
right_sum = get_rect_sum(II, x=4, y=2, w=2, h=4)

# Haar Feature Calculation: Right (White) - Left (Black)
haar_value = right_sum - left_sum

print(f"Sum of pixels in Left Rectangle: {left_sum}")
print(f"Sum of pixels in Right Rectangle: {right_sum}")
print(f"Haar Feature Value: {haar_value}")

if haar_value > 1000:
    print(">> Strong Vertical Edge Detected!")
else:
    print(">> No Edge Detected.")