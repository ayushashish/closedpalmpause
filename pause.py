import cv2
import pyautogui

cscPath="closed_frontal_palm.xml"
cpalm=cv2.CascadeClassifier(cscPath)
count=0
cap=cv2.VideoCapture(0)

while (True):
    ret, frame=cap.read()
    cv2.imshow("close palm to pause",frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    paw=cpalm.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(30,30))
    
    if (len(paw)!=0):
        
        print ("closed palm detected",count)
        count=count+1
        pyautogui.keyDown('space')
        for i in range (0,10,1):
            ret, frame=cap.read()
        
    c = cv2.waitKey(7) % 0x100
    if c == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
