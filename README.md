# Image-Resizer from URL

`mainURL.py` is a Python script designed to resize an image downloaded from a URL. It fetches the image data from the specified URL using the requests library and saves it locally as `currImage.jpg`. The script then utilizes the OpenCV library to resize the image based on configurable parameters such as the source, destination, and the percentage by which the image is resized (`scale_percent`). After resizing, the script saves the resized image as `newImage.png`.

## Usage

1. Clone the repository or download the `mainURL.py` file.
2. Ensure you have Python installed on your system.
3. Install the necessary libraries using pip: `pip install requests opencv-python`.
4. Modify the `url` variable to point to the desired image URL.
5. Run the script using Python: `python mainURL.py`.
6. The script will download the image from the URL, resize it according to the specified parameters, and save the resized image as `newImage.png`.

## Dependencies

- Python
- requests
- OpenCV

