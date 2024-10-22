import cv2
import numpy as np

# Load the image
image = cv2.imread('20240407_105517.jpg')

# Convert to grayscale and apply Gaussian blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection with adjusted thresholds
edges = cv2.Canny(blurred, 100, 200)

# Find contours in the edged image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Initialize screen_cnt
screen_cnt = None

# Identify monitor's contour with improved filtering
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 1000: 
        continue
    
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    if len(approx) == 4:
        screen_cnt = approx
        break

# Check if a suitable contour was found
if screen_cnt is None:
    print("No suitable contour found.")
    exit()  # Handle accordingly

# Function to order points in clockwise order starting from top-left
def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  
    rect[2] = pts[np.argmax(s)]  
   
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  
    rect[3] = pts[np.argmax(diff)]  
    
    return rect

screen_cnt = order_points(screen_cnt.reshape(4, 2))

# Crop and de-skew using perspective transformation
pts1 = np.float32(screen_cnt)
width, height = 800, 600  
pts2 = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
warped_image = cv2.warpPerspective(image, matrix, (width, height))

# Save or display result
cv2.imwrite('after.jpg', warped_image)
cv2.imshow('Cropped and De-skewed Image', warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()