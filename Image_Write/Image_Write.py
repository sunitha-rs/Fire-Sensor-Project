import cv2
image = cv2.imread("Waterfalls.jfif")
window_name = "Image_Write"

font = cv2.FONT_HERSHEY_SIMPLEX
text = "Joga Falls"
org = (50,50)
fontScale = 1
color = (255,0,0) 
thickness = 2

image = cv2.putText(image, text, org, font, fontScale,color, thickness, cv2.LINE_AA)  

cv2.imwrite("output.jpg", image)

cv2.waitKey(0)
