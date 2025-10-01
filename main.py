import cv2 
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

#boilerplate for capture video
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4,720)

detector = HandDetector(detectionCon=1)

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],  #l1
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],  #l2
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],  #l2
]
finaltext=[]

keyboard = Controller()

def drawall(img, buttonlist):
    for button in buttonlist:
        x,y = button.pos
        w,h = button.size
        cv2.rectangle(img, button.pos, (x+w, y+h),(255,100,265), cv2.FILLED)
        cv2.putText(img, button.text, (x+15, y+60), cv2.FONT_HERSHEY_COMPLEX,2,(25,255,255), 2)
    return img

#making button and these are resizeable
class Button():
    def __init__(self, pos,text,size=[85,85]):
        self.pos = pos
        self.size = size
        self.text = text
        
buttonlist = []    

for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonlist.append(Button([j*100+50, 100*i+50], key))
        
while True:
    success, img = cap.read()
    #find hands
    img = detector.findHands(img)
    #hand_landmark
    lmlist, bbox = detector.findPosition(img, draw=True)
    img = drawall(img, buttonlist)
    
    #check if hand is there
    if lmlist:
        for button in buttonlist:
            x,y=button.pos
            w,h = button.size
            
            if x<lmlist[8][0]<x+w and y<lmlist[8][1]<y+h:
                cv2.rectangle(img, button.pos, (x+w, y+h),(100,100,265), cv2.FILLED)
                cv2.putText(img, button.text, (x+15, y+60), cv2.FONT_HERSHEY_COMPLEX,2,(25,255,255), 2)
                
                l,_,_ = detector.findDistance(4,8, img,draw=False)   #find distance using just index
                print(l)
                
                if l<35:
                    keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x+w, y+h),(100,100,265), cv2.FILLED)
                    cv2.putText(img, button.text, (x+15, y+60), cv2.FONT_HERSHEY_COMPLEX,2,(100,100,100), 2)
                    finaltext += button.text
                    sleep(0.1)
                    
    cv2.rectangle(img, (50,350), (700,450),(100,100,265), cv2.FILLED)
    cv2.putText(img, "".join(finaltext), (60, 400), cv2.FONT_HERSHEY_COMPLEX, 2, (25, 255, 255), 2)

                
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    
