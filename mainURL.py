import requests
from PIL import Image
import cv2

url = 'https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg'

data = requests.get(url).content

f = open('currImage.jpg','wb')

# Storing the image data inside the data variable to the file
f.write(data)
f.close()

# Opening the saved image and displaying it
img = Image.open('currImage.jpg')
img.show()


#Configurable Parameters
source = "./currImage.jpg"
destination = "newImage.png"
#Percentage by which the image is resized
scale_percent=200

#reading image
src=cv2.imread(source,cv2.IMREAD_COLOR)

#showing image
# cv2.imshow("image",src)

#Calculating new dimensions of the image
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

#resize image
output = cv2.resize(src,(new_width, new_height))

#write to the destination
cv2.imwrite(destination,output)

print("Image is successfully being resized by",scale_percent, "%")

