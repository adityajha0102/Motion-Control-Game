import cv2 
import pyautogui
import time
count=0
count1=0
cap=cv2.VideoCapture(0)
tracker= cv2.TrackerCSRT_create()    #suitable for smaller objects
#tracker=cv2.TrackerKCF_create()     #better for bigger objects   (recommended)
#tracker=cv2.TrackerMOSSE_create()  ##not good
#tracker=cv2.TrackerGOTURN_create()
#CSRT_create()
success,img= cap.read()
img = cv2.flip(img, 1)
bbox= cv2.selectROI("tracking",img,False)
tracker.init(img,bbox)
def drawbox(img,bbox):
    x,y,w,h= int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    global count,count1
    if(x>285 and y>160 and x<355 and y <320):
        count=0
    if(y>205 and y<275 and x>300 and x<340):
        count1=0
    if(count1<1):
        if(x>0 and y<205):
            print("up")
            pyautogui.keyDown('up')
            pyautogui.keyUp('up')
            count1+=1
        elif(x>0 and y>275):
            print("down")
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')
            count1+=1
    if(count<1):
        if(x>355 and y>160):
            print("right")
            pyautogui.keyDown('right')
            pyautogui.keyUp('right')
            count+=1
        elif(x<285 and y>160):
            print("left")
            pyautogui.keyDown('left')
            pyautogui.keyUp('left')
            count+=1
            time.sleep(0.001)
        
        
    cv2.circle(img,(x,y), 10,(255, 255, 0),3)

while True:
    timer= cv2.getTickCount()
    success,img= cap.read()
    img = cv2.flip(img, 1)
    cv2.line(img,(0,205),(640,205),(0,224,19),2)        #horizontal up  
    cv2.line(img,(0,275),(640,275),(0,224,19),2)       #horizontal down
    cv2.line(img,(285,0),(285,480),(0,224,19),2)       #vertical left
    cv2.line(img,(355,0),(355,480),(0,224,19),2)       #vertical right
    success,bbox= tracker.update(img)
    if success:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"lost",(75,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,223,0),2)
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(7,50),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,223,0),2)
    cv2.imshow("video",img)
    if cv2.waitKey(1) == ord('q'):
        break