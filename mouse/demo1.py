import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("EVENT_LBUTTONDOWN:")
        print((event,x,y))
        cv2.circle(img,(x,y),5,(255,0,0),-1)  # draw a blue circle
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("EVENT_RBUTTONDOWN:")
        print((event,x,y))
        cv2.circle(img,(x,y),5,(0,0,255),-1)  # draw a red circle
 

cv2.startWindowThread() # run this first for Notebook!  See https://txt.arboreus.com/2012/07/11/highgui-opencv-window-from-ipython.html

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

print("Press ESC to quit")

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(10) & 0xFF == 27:
        print("quit")
        break
cv2.destroyAllWindows()

