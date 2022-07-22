from datetime import datetime
from re import I
import cv2 , time,pandas

first_frame=None

status_list=[None,None]

vdo=cv2.VideoCapture(0, cv2.CAP_DSHOW)

# for recording the time using the date time method wherever the object isn't present 
times=[]
df=pandas.DataFrame(columns=["start","end"])

while True:

    status=0
    check,frame=vdo.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame= gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thres_frame=cv2.threshold(delta_frame,20,255,cv2.THRESH_BINARY)[1]
    thres_frame=cv2.dilate(thres_frame,None,iterations=2)

    (cnts,_)=cv2.findContours(thres_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<10000:
            continue
        #if the contour is equal or bigger than 1000 then we will create a rectangle ..
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        # take the coordinates and then create a recatngle over there 
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,255,0),3)
    status_list.append(status)
    status_list=status_list[-2:]
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())


    cv2.imshow("t's me ",gray)
    cv2.imshow("Delta",delta_frame)
    cv2.imshow("Threshold frame ",thres_frame)
    cv2.imshow("Color Frame",frame)

    key = cv2.waitKey(1)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"start":(times[i]),"end":(times[i+1])},ignore_index=True)

df.to_csv("Times.csv")

cv2.destroyAllWindows()
vdo.release()

