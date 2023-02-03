import cv2
import numpy as np

def detect_colors(img_path):
    # Load the image
    img = cv2.imread("C:\\Users\\Zaki\\Downloads\\image.jpg")

    # Check if the image was loaded successfully
    if img is None:
        raise Exception("Failed to load the image.")

    # Convert the image to the HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the range of colors to detect
    color_ranges = {
        'red': [(0, 120, 70), (10, 255, 255)],
        'blue': [(100, 120, 70), (120, 255, 255)],
        'black': [(0, 0, 0), (180, 255, 40)],
    }

    # Create an empty result image
    result_img = img.copy()

    # Iterate over the color ranges
    for color_name, (lower, upper) in color_ranges.items():
        # Create a mask for the current color range
        mask = cv2.inRange(hsv_img, np.array(lower), np.array(upper))

        # Use morphological transformations to improve the mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw a bounding box around each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if color_name == 'red':
                cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            elif color_name == 'blue':
                cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            elif color_name == 'black':
                cv2.rectangle(result_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Return the result image
    return result_img

# Call the detect_colors function
result_img = detect_colors("image.jpg")

# Show the result image
cv2.imshow("Result", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
