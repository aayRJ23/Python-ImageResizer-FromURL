import cv2

#Configurable Parameters
source = "./dog.jpg"
destination = "newImage.png"
#Percentage by which the image is resized
scale_percent=50

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

