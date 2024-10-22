## Overview

This Python script automates the process of detecting a TV or computer monitor within an image, cropping the screen content, and correcting any perspective distortion (de-skewing). The result is an accurately cropped image that displays only the content of the monitor or TV.

## Features

- **Automatic Detection**: Identifies the largest rectangular shape in the image, which is assumed to be the monitor or TV.
- **Cropping**: Crops the identified area from the original image.
- **De-skewing**: Corrects perspective distortion to produce a straightened view of the monitor's content.
- **User-Friendly Output**: Saves the processed image and optionally displays it for immediate review.

## Requirements

To run this script, you need to have Python installed along with the following libraries:

- OpenCV
- NumPy

You can install these libraries using pip:

```bash
pip install opencv-python numpy
```

## Installation

1. **Clone or Download the Repository**: 
   Clone this repository or download the script file directly.

2. **Install Dependencies**: 
   Ensure you have Python installed on your machine. Install the required libraries as mentioned above.

3. **Prepare Your Image**: 
   Place your input image (e.g., `before.jpg`) in the same directory as the script or specify the correct path in the script.

## Usage

1. **Open the Script**: 
   Open `myscript.py` in your preferred code editor.

2. **Modify Input Image Path (if necessary)**: 
   If your input image is named differently or located in another directory, update the line:
   
   ```python
   image = cv2.imread('before.jpg')
   ```

3. **Run the Script**: 
   Execute the script using Python:

   ```bash
   python myscript.py
   ```

4. **Output**: 
   After running, you will find an output image saved as `after.jpg` in the same directory. This image will contain only the cropped and de-skewed content from the detected monitor or TV.

## How It Works

### Step-by-Step Breakdown

1. **Image Loading**:
   - The script begins by loading an image file specified by the user.

2. **Preprocessing**:
   - The image is converted to grayscale.
   - A Gaussian blur is applied to reduce noise and improve edge detection.

3. **Edge Detection**:
   - Canny edge detection is performed to identify edges within the image.

4. **Contour Detection**:
   - Contours are detected from the edged image.
   - The contours are sorted by area to find potential candidates for monitors/TVs.

5. **Contour Filtering**:
   - The script checks each contour to find a suitable rectangular shape (with four corners).
   - If no suitable contour is found, an error message is displayed, and execution stops.

6. **Point Ordering**:
   - The four corners of the detected contour are ordered in a clockwise manner starting from the top-left corner.

7. **Perspective Transformation**:
   - A perspective transformation matrix is created based on these points to crop and de-skew the identified area.
   
8. **Saving and Displaying Output**:
   - The resulting cropped and de-skewed image is saved as `after.jpg`.
   - Optionally, it can be displayed using OpenCV's imshow function for immediate feedback.

## Troubleshooting

- If you encounter errors regarding contour detection or if no output is produced, ensure that your input image contains a clear view of a monitor or TV.
- Adjust parameters such as Canny edge detection thresholds and contour area filtering based on your specific images for better results.
- Check that all required libraries are installed correctly.

## Example Input/Output

### Input Image (`before.jpg`)
Before Image  *(Replace with actual path)*

### Output Image (`after.jpg`)
After Image  *(Replace with actual path)*

## Contributing

If you would like to contribute to this project, please feel free to fork this repository and submit a pull request with improvements or bug fixes.

## License

This project is licensed under [MIT License](LICENSE).
