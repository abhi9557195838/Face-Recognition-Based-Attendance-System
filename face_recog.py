from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import os


class FaceRecog:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1980x1020+0+0")
        self.root.title("ATTENDANCE SYSTEM")

        img =Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\female-programmer-scanning-her-face-with-biometric-security-technology-virtual-screen-digital-remix.jpg")
        img=img.resize((1550,850),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=850)

        title_lbl=Label(f_lbl,text="ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="Black",fg="White")
        title_lbl.place(x=0,y=0,width=1550,height=50)

        img3=Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\recog.jpeg")
        img3=img3.resize((200,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(f_lbl,image=self.photoimg3,command=self.recognition,cursor="hand2")
        b3.place(x=650,y=275,width=220,height=220)

        b=Button(f_lbl,text="Recognize",cursor="hand2",command=self.recognition,font=("times new roman",20,"bold"),bg="black",fg="white")
        b.place(x=650,y=495,width=220,height=40)

    def mark(self,i,r,n,d):
        with open(r"C:\Users\hp\Desktop\Attendance system\data.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #recognition
    def recognition(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@9557",database="attendance_system")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select branch from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"Student_id : {i}",(x,y-95),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll_no : {r}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name : {n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Branch : {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
 
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier(r"C:\Users\hp\AppData\Roaming\Python\Python310\site-packages\cv2\data\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\hp\Desktop\Attendance system/classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
               
        video_cap.release()
        cv2.destroyAllWindows()

if __name__== "__main__":
     root=Tk()
     obj=FaceRecog(root)
     root.mainloop() 

