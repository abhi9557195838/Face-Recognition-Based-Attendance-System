from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
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

        img3=Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\tr.png ")
        img3=img3.resize((200,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(f_lbl,image=self.photoimg3,command=self.train_classifier,cursor="hand2")
        b3.place(x=650,y=275,width=220,height=220)

        b1=Button(f_lbl,text="Train",cursor="hand2",command=self.train_classifier,font=("times new roman",20,"bold"),bg="black",fg="white")
        b1.place(x=650,y=495,width=220,height=40)

    def train_classifier(self):
        data_dir=(r"C:\Users\hp\Desktop\Attendance system\rawimage")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write(r"C:\Users\hp\Desktop\Attendance system/classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset Completed...")


if __name__== "__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop() 