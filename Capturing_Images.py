#click on the image

import cv2 

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    check, frame = webcam.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('s'): 
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        webcam.release()
        cv2.destroyAllWindows()
        print("Image saved!")
        break
    elif key == ord('q'):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

        
        
