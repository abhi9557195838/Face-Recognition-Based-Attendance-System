from this import s
from student import Student
from train import Train
from face_recog import FaceRecog
from attendance import Attendance
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter


class FRS:
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

        img1=Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\stuimg.png")
        img1=img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(f_lbl,image=self.photoimg1,command=self.student_detail,cursor="hand2")
        b1.place(x=100,y=75,width=200,height=200)

        b1=Button(f_lbl,text="Student",cursor="hand2",command=self.student_detail,font=("times new roman",20,"bold"),bg="black",fg="white")
        b1.place(x=100,y=275,width=200,height=40)

        img2=Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\train.jpeg")
        img2=img2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(f_lbl,image=self.photoimg2,command=self.train_data,cursor="hand2")
        b2.place(x=100,y=325,width=200,height=200)

        b2=Button(f_lbl,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="black",fg="white")
        b2.place(x=100,y=525,width=200,height=40)

        img3=Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\face-recognition-ar-hologram-screen-smart-technology.jpg")
        img3=img3.resize((200,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(f_lbl,image=self.photoimg3,command=self.recog,cursor="hand2")
        b3.place(x=1235,y=75,width=200,height=200)

        b3=Button(f_lbl,text="Face Recognize",cursor="hand2",command=self.recog,font=("times new roman",20,"bold"),bg="black",fg="white")
        b3.place(x=1235,y=275,width=200,height=40)

        img4=Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\photos.png")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(f_lbl,image=self.photoimg4,command=self.open_img,cursor="hand2")
        b4.place(x=100,y=575,width=200,height=200)

        b4=Button(f_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="black",fg="white")
        b4.place(x=100,y=775,width=200,height=40)

        img5=Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\stuimg.png")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(f_lbl,image=self.photoimg5,command=self.attendance,cursor="hand2")
        b5.place(x=1235,y=325,width=200,height=200)

        b5=Button(f_lbl,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",20,"bold"),bg="black",fg="white")
        b5.place(x=1235,y=525,width=200,height=40)

        img6=Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\exit.png")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(f_lbl,image=self.photoimg6,command=self.exit,cursor="hand2")
        b6.place(x=1235,y=575,width=200,height=200)

        b6=Button(f_lbl,text="Exit",command=self.exit,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b6.place(x=1235,y=775,width=200,height=40)

    def open_img(self):
        os.startfile(r"C:\Users\hp\Desktop\Attendance system\rawimage")

    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def recog(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecog(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("FRS","Are you sure you want to exit",parent=self.root)
        if self.exit >0:
           self.root.destroy()
        else:
            return

if __name__== "__main__":
     root=Tk()
     obj=FRS(root)
     root.mainloop()        