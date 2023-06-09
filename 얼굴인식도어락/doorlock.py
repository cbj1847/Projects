from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
'''
pyqt 로 스크린에 UI표현
'''
from PIL import Image
import numpy as np
import functools
import cv2
#얼굴인식 opencv 사용

import threading
import sys
import os
import RPi.GPIO as GPIO
import time
from jsonDB import * #jsonDB 로 몇명의 얼굴이 저장되어있는지 확인
from opencv_wrapper import * #opencv_wrapper사용
from servo import * # 서보모터 사용


path = os.path.dirname(os.path.abspath(__file__))
offset=50
faceCascade = cv2.CascadeClassifier("/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")#얼굴 검색

video_capture = cv2.VideoCapture(-1) # 카메라 객체 생성 및
video_capture.set(cv2.CAP_PROP_FPS,10)# 셋팅값 설정
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH ,640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

recognizer = cv2.face.LBPHFaceRecognizer_create() #저장된얼굴과 비교하는 클래스
recognizer.read(path+'/trainer/trainer.yml') #훈련된파일 읽어오기
global personID, training
db = JsonDB('test.json')

personID = 0 #기본값 0
try:
    personID = db.read('person') #json 에 훈련된 저장된 값을 읽어오기
except:
    db.write('person',personID) #값이 없다면 초기값 0 저장
training = 0 #학습모드 0터치스크린에서 버튼을 눌러주면 1로 변경

def register (): # 얼굴 등록 함수
    global personID
    personID += 1 #사람 카운트
    name = personID
    db.write('person',personID) #카운트된사람수 업데이트
    print("name", name)
    i=0
    while True:
        ret, im =video_capture.read() # 촬영
        rows,cols,_ = im.shape
        #print(rows, cols)
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE) # 얼굴 검출
        for(x,y,w,h) in faces: 
            i=i+1
            offx = x - offset
            offx2 = x + offset + w
            offy = y- offset
            offy2 = y + offset + h # 여백
            if offx < 0:
                offx = 0
            elif offx2 > cols:
                offx2 = cols
            if offy < 0:
                offy = 0
            elif offy2 > rows:
                offy2 = rows
            cv2.imwrite("dataSet/face-"+str(name) +'.'+ str(i) + ".jpg", gray[offy:offy2,offx:offx2]) # dataSet 폴더에 저장 
            cv2.rectangle(im,(offx,offy),(offx2,offy2),(225,0,0),2)
        if i>20:
            break
        #카메라화면 표시 #      cv2.imshow('im',im)
        cv2.imwrite('/home/pi/project/pic.jpg', im)
        img.setPixmap(QPixmap('/home/pi/project/pic.jpg')) # 사진 스크린에 표시

def get_images_and_labels(datapath): # 저장된 사진파일 읽어오기
     image_paths = [os.path.join(datapath, f) for f in os.listdir(datapath)]
     images = []
     labels = []
     for image_path in image_paths:
         image_pil = Image.open(image_path).convert('L')
         image = np.array(image_pil, 'uint8')
         print(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
         nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
         print(nbr)
         faces = faceCascade.detectMultiScale(image)
         for (x, y, w, h) in faces:
             images.append(image[y: y + h, x: x + w])
             labels.append(nbr)
     return images, labels

def train(): # 학습 및 저장
    dataPath = path+'/dataSet'
    images, labels = get_images_and_labels(dataPath)
    print('label',labels)

    recognizer.train(images, np.array(labels)) # 학습
    recognizer.save(path+'/trainer/trainer.yml') # 저장

def trainFunc(event):
    global training
    training = 1






global makegroup
makegroup = 0
numX = 50
numY = 30
startX = 640
startY = 450
inX = 70
inY = 50
fontLeftMenu= QFont('나눔고딕OTF', 18, QFont.Thin)
def cam():
    global makegroup
    global personID, training
    font = cv2.FONT_HERSHEY_SIMPLEX
    openflag = 0
    waitTime = 0
    count = 0
    while True:
        ret, frame1 = video_capture.read()
        rows,cols,_ = frame1.shape
        #print("cam",rows,cols)
        if time.time() - waitTime > 10: #10초이상 초과하면 서보모터닫힘
            if time.time() - waitTime  < 12:
                servoClose()

        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100)
        )
        bigface = [0,0,0,0]

        for (x, y, w, h) in faces:
            offx = x - offset
            offx2 = x + offset + w
            offy = y- offset
            offy2 = y + offset + h
            if offx < 0:
                offx = 0
            elif offx2 > cols:
                offx2 = cols
            if offy < 0:
                offy = 0
            elif offy2 > rows:
                offy2 = rows
            cv2.rectangle(frame1,(offx,offy),(offx2,offy2),(225,0,0),2)
            if personID  > 0:
                nbr, conf = predict(recognizer,gray[y:y+h,x:x+w],0,cv2.COLOR_BGR2GRAY)
                print(conf, nbr)
                if conf <65: #매칭 score 수치 조정 가능
                    cv2.putText(frame1,str(nbr)+"", (x,y+h),font, 1.1, (0,0,255))
                    if time.time() - waitTime > 10:
                        waitTime = time.time()
                        servoOpen()
                    count = 0
                else:
                    count += 1
                    if count >10: #10번이상 등록되어있는 얼굴이 아니라면
                        count = 0 #count 제로로


        img.setPixmap(QPixmap('/home/pi/project/pic.jpg')) #카메라화면 표시
        cv2.imwrite('/home/pi/project/pic.jpg', frame1)
        if training == 1: # 버튼을 눌렀을경우 1로 변경되고
            register() # 등록
            train() # 재학습
            training = 0 #모드 다시 0으로 번경



class hardCtl(QMainWindow): #메인화면 생성 클래스
    def __init__(self, parent=None):
        super(hardCtl, self).__init__(parent)
        global idTxt, pwTxt, feedTxt, shitTxt,peeTxt,feedBtn, feed2Btn, timeCombo, minCombo, reserveBtn
        global hourFeed, minFeed,img

        img = QLabel(self) # 카메라 화면
        img.move(50,0)
        img.resize(640, 480)
        img.setPixmap(QPixmap('/home/pi/project/pic.jpg'))
        numberQ = QPushButton(self)  # 등록버튼
        numberQ.setFont(fontLeftMenu)
        numberQ.resize(numX,numY)
        numberQ.move(startX, startY)
        numberQ.setText("add")
        numberQ.mousePressEvent = trainFunc


        t2 = threading.Thread(target = cam) # 스레드로 동작
        t2.daemon = True
        t2.start()

        self.showFullScreen() # 풀스크린 출력

app = QApplication(sys.argv)
sb = hardCtl()
sb.resize(800, 480)
sb.move(0, 0)

sys.exit(app.exec_())
