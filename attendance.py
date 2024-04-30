from tkinter import *
from tkinter import ttk
from turtle import update
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1980x1020+0+0")
        self.root.title("FRS")

        self.var_atten_id= StringVar()
        self.var_atten_roll= StringVar()
        self.var_atten_name= StringVar()
        self.var_atten_branch= StringVar()
        self.var_atten_time= StringVar()
        self.var_atten_date= StringVar()
        self.var_atten_attendance= StringVar()

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

        ac_frame=LabelFrame(L_frame,bd=2,relief=RIDGE,bg="white")
        ac_frame.place(x=5,y=135,width=720,height=400)

        a_lbl=Label(ac_frame,text="AttendanceID:",font=("times new roman",12,"bold"))
        a_lbl.grid(row=0,column=0,padx=10,sticky=W)

        a_lbl=ttk.Entry(ac_frame,width=28,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        a_lbl.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        a_lbl=Label(ac_frame,text="Roll No.:",font=("times new roman",12,"bold"))
        a_lbl.grid(row=0,column=2,padx=4,pady=8)

        a_lbl=ttk.Entry(ac_frame,textvariable=self.var_atten_roll,width=28,font=("times new roman",12,"bold"))
        a_lbl.grid(row=0,column=3,pady=8)

        a_lbl=Label(ac_frame,text="Name:",font=("times new roman",12,"bold"))
        a_lbl.grid(row=1,column=0)

        a_lbl=ttk.Entry(ac_frame,textvariable=self.var_atten_name,width=28,font=("times new roman",12,"bold"))
        a_lbl.grid(row=1,column=1,pady=8)

        a_lbl=Label(ac_frame,text="Branch:",font=("times new roman",12,"bold"))
        a_lbl.grid(row=1,column=2)

        a_lbl=ttk.Entry(ac_frame,textvariable=self.var_atten_branch,width=28,font=("times new roman",12,"bold"))
        a_lbl.grid(row=1,column=3,pady=8)

        a_lbl=Label(ac_frame,text="Time:",font=("times new roman",12,"bold"))
        a_lbl.grid(row=2,column=0)

        a_lbl=ttk.Entry(ac_frame,textvariable=self.var_atten_time,width=28,font=("times new roman",12,"bold"))
        a_lbl.grid(row=2,column=1,pady=8)

        a_lbl=Label(ac_frame,text="Date:",font=("times new roman",12,"bold"))
        a_lbl.grid(row=2,column=2)

        a_lbl=ttk.Entry(ac_frame,textvariable=self.var_atten_date,width=28,font=("times new roman",12,"bold"))
        a_lbl.grid(row=2,column=3,pady=8)

        a_lbl=Label(ac_frame,text="Attendance Status:",font=("times new roman",12,"bold"))
        a_lbl.grid(row=3,column=0)

        self.d_combo=ttk.Combobox(ac_frame,textvariable=self.var_atten_attendance,width=26,font=("times new roman",12,"bold"),state="readonly")
        self.d_combo["values"]=("Status","Present","Absent")

        self.d_combo.grid(row=3,column=1,pady=10)
        self.d_combo.current(0)

        b_frame=Frame(ac_frame,bd=2,relief=RIDGE)
        b_frame.place(x=0,y=300,width=536,height=35)

        b7=Button(b_frame,text="Import csv",command=self.impCsv,cursor="hand2",width=17,font=("times new roman",13,"bold"),bg="black",fg="white")
        b7.grid(row=0,column=0)

        b8=Button(b_frame,text="Export csv",command=self.expcsv,cursor="hand2",width=17,font=("times new roman",13,"bold"),bg="black",fg="white")
        b8.grid(row=0,column=1)

        b99=Button(b_frame,text="Reset",command=self.reset_data,cursor="hand2",width=17,font=("times new roman",13,"bold"),bg="black",fg="white")
        b99.grid(row=0,column=3)

        #R

        R_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="DETAILS",font=("times new roman",12,"bold"))
        R_frame.place(x=750,y=10,width=720,height=580)

        t_frame=LabelFrame(R_frame,bd=2,relief=RIDGE,bg="white")
        t_frame.place(x=5,y=5,width=710,height=530)

        sc_x=ttk.Scrollbar(t_frame,orient=HORIZONTAL)
        sc_y=ttk.Scrollbar(t_frame,orient=VERTICAL)

        self.a_r_t=ttk.Treeview(t_frame,columns=("id","roll","name","branch","time","date","attendance"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.pack(side=BOTTOM,fill=X)
        sc_y.pack(side=RIGHT,fill=Y)
        sc_x.config(command=self.a_r_t.xview)
        sc_y.config(command=self.a_r_t.yview)

        self.a_r_t.heading("id",text="Attendance ID")
        self.a_r_t.heading("roll",text="Roll No.")
        self.a_r_t.heading("name",text="Name")
        self.a_r_t.heading("branch",text="Branch")
        self.a_r_t.heading("time",text="Time")
        self.a_r_t.heading("date",text="Date")
        self.a_r_t.heading("attendance",text="Attendance")
        
        self.a_r_t["show"]="headings"

        self.a_r_t.column("id",width=100)
        self.a_r_t.column("roll",width=100)
        self.a_r_t.column("name",width=100)
        self.a_r_t.column("branch",width=100)
        self.a_r_t.column("time",width=100)
        self.a_r_t.column("date",width=100)
        self.a_r_t.column("attendance",width=100)
 
        self.a_r_t.pack(fill=BOTH,expand=1)

        self.a_r_t.bind("<ButtonRelease>",self.get_cursor)

    def fetchdata(self,rows):
        self.a_r_t.delete(*self.a_r_t.get_children())
        for i in rows:
            self.a_r_t.insert("",END,values=i)

    def impCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    
    def expcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.a_r_t.focus()
        content=self.a_r_t.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_branch.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_branch.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    
if __name__== "__main__":
     root=Tk()
     obj=Attendance(root)
     root.mainloop()