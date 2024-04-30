from tkinter import *
from tkinter import ttk
from turtle import update
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1980x1020+0+0")
        self.root.title("FRS")

        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_branch=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_dob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        img =Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\female-programmer-scanning-her-face-with-biometric-security-technology-virtual-screen-digital-remix.jpg")
        img=img.resize((1550,850),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
    
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=850)

        title_lbl=Label(f_lbl,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1550,height=50)

        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=23,y=150,width=1480,height=600)

        #L

        L_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="DETAILS",font=("times new roman",12,"bold"))
        L_frame.place(x=10,y=10,width=750,height=580)

        img1 =Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\detail.png")
        img1=img1.resize((720,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(L_frame,image=self.photoimg1)
        f_lbl.place(x=5,y=0,width=720,height=135)

        cc_frame=LabelFrame(L_frame,bd=2,relief=RIDGE,text="CURRENT COURSE DETAILS",font=("times new roman",12,"bold"))
        cc_frame.place(x=5,y=135,width=720,height=150)

        d_lbl=Label(cc_frame,text="Course",font=("times new roman",12,"bold"))
        d_lbl.grid(row=0,column=0,padx=10,sticky=W)

        d_combo=ttk.Combobox(cc_frame,width=28,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        d_combo["values"]=("Select Course","Bachelor of Technology","Diploma","MBA","Master in Technology")
        d_combo.current(0)
        d_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        d_lbl=Label(cc_frame,text="Year",font=("times new roman",12,"bold"))
        d_lbl.grid(row=0,column=3,padx=10,sticky=W)

        d_combo=ttk.Combobox(cc_frame,width=28,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        d_combo["values"]=("Select Year","2022-23","2023-24","2024-25","2025-26")
        d_combo.current(0)
        d_combo.grid(row=0,column=4,padx=2,pady=10,sticky=W)

        s_lbl=Label(cc_frame,text="Branch",font=("times new roman",12,"bold"))
        s_lbl.grid(row=1,column=0,padx=10,sticky=W)

        s_lbl=ttk.Entry(cc_frame,width=30,textvariable=self.var_branch,font=("times new roman",12,"bold"))
        s_lbl.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        d_lbl=Label(cc_frame,text="Semester",font=("times new roman",12,"bold"))
        d_lbl.grid(row=1,column=3,padx=10,sticky=W)

        d_combo=ttk.Combobox(cc_frame,width=28,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        d_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        d_combo.current(0)
        d_combo.grid(row=1,column=4,padx=2,pady=10,sticky=W)

        #s detail
        
        cs_frame=LabelFrame(L_frame,bd=2,relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"))
        cs_frame.place(x=5,y=250,width=720,height=300)

        s_lbl=Label(cs_frame,text="StudentID",font=("times new roman",12,"bold"))
        s_lbl.grid(row=0,column=0,padx=10,sticky=W)

        s_lbl=ttk.Entry(cs_frame,width=28,textvariable=self.var_std_id,font=("times new roman",12,"bold"))
        s_lbl.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        s_lbl=Label(cs_frame,text="Student Name",font=("times new roman",12,"bold"))
        s_lbl.grid(row=0,column=2,padx=10,sticky=W)

        s_lbl=ttk.Entry(cs_frame,width=28,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        s_lbl.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        s_lbl=Label(cs_frame,text="Roll no.",font=("times new roman",12,"bold"))
        s_lbl.grid(row=1,column=0,padx=10,sticky=W)

        s_lbl=ttk.Entry(cs_frame,width=28,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        s_lbl.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        s_lbl=Label(cs_frame,text="Email",font=("times new roman",12,"bold"))
        s_lbl.grid(row=1,column=2,padx=10,sticky=W)

        s_lbl=ttk.Entry(cs_frame,width=28,textvariable=self.var_email,font=("times new roman",12,"bold"))
        s_lbl.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        s_lbl=Label(cs_frame,text="DOB",font=("times new roman",12,"bold"))
        s_lbl.grid(row=2,column=0,padx=10,sticky=W)

        s_lbl=ttk.Entry(cs_frame,width=28,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        s_lbl.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        s_lbl=Label(cs_frame,text="Phone no",font=("times new roman",12,"bold"))
        s_lbl.grid(row=2,column=2,padx=10,sticky=W)

        s_lbl=ttk.Entry(cs_frame,width=28,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        s_lbl.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        s_lbl=Label(cs_frame,text="Address",font=("times new roman",12,"bold"))
        s_lbl.grid(row=3,column=0,padx=10,sticky=W)

        s_lbl=ttk.Entry(cs_frame,width=28,textvariable=self.var_address,font=("times new roman",12,"bold"))
        s_lbl.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        s_lbl=Label(cs_frame,text="Teacher Name",font=("times new roman",12,"bold"))
        s_lbl.grid(row=3,column=2,padx=10,sticky=W)

        s_lbl=ttk.Entry(cs_frame,width=28,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        s_lbl.grid(row=3,column=3,padx=2,pady=10,sticky=W)
        
        #Radiobutton
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="Take Photo", value="yes")
        radio1.grid(row=6,column=0)

        radio1=ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="Don't Take Photo", value="No")
        radio1.grid(row=6,column=1)

        b_frame=Frame(cs_frame,bd=2,relief=RIDGE)
        b_frame.place(x=0,y=200,width=715,height=35)


        b7=Button(b_frame,text="Save",cursor="hand2",width=17,command=self.add_data,font=("times new roman",13,"bold"),bg="black",fg="white")
        b7.grid(row=0,column=0)

        b8=Button(b_frame,text="Update",cursor="hand2",width=17,command=self.update_data,font=("times new roman",13,"bold"),bg="black",fg="white")
        b8.grid(row=0,column=1)

        b9=Button(b_frame,text="Delete",cursor="hand2",width=17,command=self.delete_data,font=("times new roman",13,"bold"),bg="black",fg="white")
        b9.grid(row=0,column=2)

        b99=Button(b_frame,text="Reset",cursor="hand2",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="black",fg="white")
        b99.grid(row=0,column=3)

        b_frame1=Frame(cs_frame,bd=2,relief=RIDGE)
        b_frame1.place(x=0,y=235,width=715,height=35)
 
        b90=Button(b_frame1,text="Take Photo",cursor="hand2",width=35,command=self.generate_dataset,font=("times new roman",13,"bold"),bg="black",fg="white")
        b90.grid(row=0,column=0)

        b91=Button(b_frame1,text="Update Photo",cursor="hand2",width=35,font=("times new roman",13,"bold"),bg="black",fg="white")
        b91.grid(row=0,column=1)

        #R

        R_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="DETAILS",font=("times new roman",12,"bold"))
        R_frame.place(x=750,y=10,width=720,height=580)

        img2 =Image.open(r"C:\Users\hp\Desktop\Attendance system\IMAGES\black.jpg")
        img2=img2.resize((750,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        f_lbl=Label(R_frame,image=self.photoimg2)
        f_lbl.place(x=5,y=0,width=710,height=135)

        #s_frame=LabelFrame(R_frame,bd=2,relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"))
        #s_frame.place(x=5,y=135,width=710,height=70)

        #s_lbl=Label(s_frame,text="Search:",font=("times new roman",15,"bold"))
        #s_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #s_combo=ttk.Combobox(s_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        #s_combo["values"]=("Select","Roll_no","Phone_no")
        #s_combo.current(0)
        #s_combo.grid(row=0,column=1,padx=4,pady=10,sticky=W)

        #e_lbl=ttk.Entry(s_frame,width=20,font=("times new roman",12,"bold"))
        #e_lbl.grid(row=0,column=2,padx=4,pady=10,sticky=W)

        #b80=Button(s_frame,text="Search",cursor="hand2",width=12,font=("times new roman",13,"bold"),bg="black",fg="white")
        #b80.grid(row=0,column=3,padx=4)

        #b95=Button(s_frame,text="Show",cursor="hand2",width=12,font=("times new roman",13,"bold"),bg="black",fg="white")
        #b95.grid(row=0,column=4,padx=4)

        t_frame=Frame(R_frame,bd=2,relief=RIDGE)
        t_frame.place(x=5,y=150,width=710,height=410)

        sc_x=ttk.Scrollbar(t_frame,orient=HORIZONTAL)
        sc_y=ttk.Scrollbar(t_frame,orient=VERTICAL)

        self.s_t=ttk.Treeview(t_frame,columns=("Course","Year","Branch","Semester","id","name","roll","email","phone","dob","address","teacher","photo"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.pack(side=BOTTOM,fill=X)
        sc_y.pack(side=RIGHT,fill=Y)
        sc_x.config(command=self.s_t.xview)
        sc_y.config(command=self.s_t.yview)

        self.s_t.heading("Course",text="Course")
        self.s_t.heading("Year",text="Year")
        self.s_t.heading("Branch",text="Branch")
        self.s_t.heading("Semester",text="Semester")
        self.s_t.heading("id",text="Student_id")
        self.s_t.heading("name",text="Name")
        self.s_t.heading("roll",text="Roll_no")
        self.s_t.heading("email",text="Email")
        self.s_t.heading("phone",text="Phone_no")
        self.s_t.heading("dob",text="D.O.B")
        self.s_t.heading("address",text="Address")
        self.s_t.heading("teacher",text="Teacher_name")
        self.s_t.heading("photo",text="PhotoSample")

        self.s_t["show"]="headings"

        self.s_t.column("Course",width=150)
        self.s_t.column("Year",width=150)
        self.s_t.column("Branch",width=150)
        self.s_t.column("Semester",width=150)
        self.s_t.column("id",width=150)
        self.s_t.column("name",width=150)
        self.s_t.column("roll",width=150)
        self.s_t.column("email",width=150)
        self.s_t.column("phone",width=150)
        self.s_t.column("dob",width=150)
        self.s_t.column("address",width=150)
        self.s_t.column("teacher",width=150)
        self.s_t.column("photo",width=150)

        self.s_t.pack(fill=BOTH,expand=1)
        self.s_t.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data() 

    def add_data(self):
         if self.var_course.get()=="Select Course" or self.var_std_name=="" or self.var_std_id=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
         else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@9557",database="attendance_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                         self.var_course.get(),
                                                                                                         self.var_year.get(),
                                                                                                         self.var_branch.get(),
                                                                                                         self.var_semester.get(),
                                                                                                         self.var_std_id.get(),
                                                                                                         self.var_std_name.get(),
                                                                                                         self.var_roll.get(), 
                                                                                                         self.var_email.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_teacher.get(),
                                                                                                         self.var_radio1.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

#fetch 
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@9557",database="attendance_system")
         my_cursor=conn.cursor() 
         my_cursor.execute("select*from student")
         data=my_cursor.fetchall()

         if len(data)!=0:
            self.s_t.delete(*self.s_t.get_children())
            for i in data:
                self.s_t.insert("",END,values=i)
            conn.commit()
         conn.close()   

    def get_cursor(self,event=""):
        cursor_focus=self.s_t.focus()
        content=self.s_t.item(cursor_focus)
        data=content["values"]

        self.var_course.set(data[0])                       
        self.var_year.set(data[1]),
        self.var_branch.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]), 
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_teacher.set(data[11]),
        self.var_radio1.set(data[12])

    def update_data(self):
        if self.var_course.get()=="Select Course" or self.var_std_name=="" or self.var_std_id=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                if Update>0:
                   conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@9557",database="attendance_system")
                   my_cursor=conn.cursor()
                   my_cursor.execute("update student set Course=%s,Year=%s,Branch=%s,Semester=%s,Name=%s,Roll=%s,Email=%s,Phone=%s,Dob=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                                                     self.var_branch.get(),
                                                                                                                                                                                                                     self.var_semester.get(),         
                                                                                                                                                                                                                     self.var_std_name.get(),
                                                                                                                                                                                                                     self.var_roll.get(), 
                                                                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                                                                     self.var_std_id.get()
                                                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to  delete this student Data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@9557",database="attendance_system")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def reset_data(self):
        self.var_course.set("Select Course")                       
        self.var_year.set("Select Year"),
        self.var_branch.set(""),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_roll.set(""), 
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_dob.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #generate dataset

    def generate_dataset(self):
        if self.var_course.get()=="Select Course" or self.var_std_name=="" or self.var_std_id=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@9557",database="attendance_system")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Course=%s,Year=%s,Branch=%s,Semester=%s,Name=%s,Roll=%s,Email=%s,Phone=%s,Dob=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                    self.var_branch.get(),
                                                                                                                                                                                                    self.var_semester.get(),         
                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                    self.var_roll.get(), 
                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # load frontal face predefined

                face_classifier=cv2.CascadeClassifier(r"C:\Users\hp\AppData\Roaming\Python\Python310\site-packages\cv2\data\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0) #0 for web cam 1 for another
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=r"rawimage\user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data set compieted")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


if __name__== "__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()