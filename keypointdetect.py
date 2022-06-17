import cv2
import mediapipe as mp
import numpy as np


cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
im = np.ones((480,640,3),dtype=np.uint8)*255

while True:
    lst =[]
    im = im*0
    _, frame = cap.read()
    if _==0:
        break
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(im,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = frame.shape
            cx,cy = int(lm.x * w), int(lm.y *h)  
            lst.append([id,cx,cy])
            # if id:#id to track
            #     h,w,c = frame.shape
            #     cx,cy = int(lm.x * w), int(lm.y *h)            
            #     cv2.circle(im,(cx,cy),5,(0,255,0),-1)

    cv2.imshow('fm',frame)
    cv2.imshow('W',im)
    if cv2.waitKey(4)==27:
        break
    print(lst)

cv2.destroyAllWindows()
print(len(lst))