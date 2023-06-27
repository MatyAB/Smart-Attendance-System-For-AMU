from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter as tk
import csv
from tkinter import filedialog
import qrcode
from datetime import datetime

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")

        #-----------Variables-------------------
        self.var_dep=StringVar()
        self.var_sec=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_divi=StringVar()
        self.var_photo=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_rol2=StringVar()
        self.var_teacher=StringVar()
        # self.var_course==StringVar()


        def val_std_id():
            spin = studentId_entry.get()
            if len(spin) == 0:
                 msg.config(fg='red', text='ID can\'t remain empty',bg='#f1e8fe',font=('arial',10))
            else:
                 if not spin.isdigit():
                    msg.config(fg='red', text='ID must be an integer',bg='#f1e8fe',font=('arial',10))
                 else:
                    msg.config(fg='#fff', text='', bg='#f1e8fe',font=('arial',10))
                    studentId_entry.delete(0, END)
	    		
    
        def val_std_name():
            name = student_name_entry.get()
            
            if len(name) == 0:
              msg2.config(fg='red', text='Name can\'t be empty',bg='#f0f0f0',font=('arial',10))
            else:
                try:
                    if len(name)>100:
                        msg2.config(fg='red',text='Nameis too long',bg='#f0f0f0',font=('arial',10))
                    elif name.isdigit():
                        msg2.config(fg='red',text='Name can\'t be a number',bg='#f0f0f0',font=('arial',10)) 
                    elif any(ch.isdigit() for ch in name):
                        msg2.config(fg='red',text='Name can\'t have numbers',font=('arial',10))
                    else:
                        msg2.config(text='')
                        student_name_entry.delete(0, END)
                except Exception as ep:
                    messagebox.showerror('error', ep)

        def val_email():
                 email =student_email_entry.get()
                 special_ch = ['@', '.']
                 if len(email) == 0:
                      msg3.config(fg='red', text='email can\'t remain empty',bg='#f1e8fe',font=('arial',10))                  
                 elif not any(ch in special_ch for ch in email):
                      msg3.config(fg='red',text='invalid email!',font=('arial',10))
                 else:
                      msg3.config(text='')
                      student_email_entry.delete(0, END)              
        def val_mob():
                mbl = student_mob_entry.get()
                if len(mbl) == 0:
                    msg4.config(fg='red', text='Mobile number can\'t be empty',bg='#f0f0f0',font=('arial',10))
                if any(ch.isdigit() for ch in mbl):
                     if len(mbl) == 10:
                         mob = int(mbl)
                         msg4.config(fg='red',text='',font=('arial',10))
                         student_mob_entry.delete(0, END)
                     else:
                         msg4.config(fg='red',text='Invalid mobile number',font=('arial',10))
                elif not mbl.isdigit():
                    msg4.config(fg='red', text='Mob-number must be an integer',bg='#f1e8fe',font=('arial',10))
                                
        

    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=110)

         # backgorund image 
        bg1=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=111,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Student Pannel",font=("verdana",28,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=35)
        fr = Frame(root,bg='#f1e8fe',highlightbackground='black', highlightcolor='black',highlightthickness=2,bd=3)
        fr.place(x=55,y=155,width=620,height=480)
        # pannel_lbl = Label(root,text='Student Pannel ',bg='#051344',fg='#ffffff',font=('Arial',32)).place(x=500,y=70)
        frame1 = LabelFrame(fr,bd=2, bg="#f1e8fe",relief=SOLID,text="Student Details",font=("Arial",12,"bold"),fg="navyblue",highlightbackground='black')
        frame1.place(x=10,y=5,width=600,height=460)
        
        
        year = Label(frame1,text='Year ',bg='#f1e8fe',fg='#001aa0',font=("Arial",12,"bold")).place(x=10,y=25)
        year_combo=ttk.Combobox(frame1,textvariable=self.var_year, width=15,font=("Arial",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","1st year","2nd year","3rd year","4th year","5th year")
        year_combo.current(0)
        year_combo.place(x=70,y=25)
        semlbl = Label(frame1,text='Semister ',bg='#f1e8fe',fg='#001aa0',font=("Arial",12,"bold")).place(x=10,y=70)
        
        
        sem_combo=ttk.Combobox(frame1,textvariable=self.var_semester, width=15,font=("Arial",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semister","1st semister","2nd semister")
        sem_combo.current(0)
        sem_combo.place(x=100,y=70)
        
        seclbl = Label(frame1,text='Section ',bg='#f1e8fe',fg='#001aa0',font=("Arial",12,"bold")).place(x=10,y=120)
        sem_combo=ttk.Combobox(frame1,textvariable=self.var_sec, width=15,font=("Arial",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Section","A","B","C")
        sem_combo.current(0)
        sem_combo.place(x=100,y=120)
        
        frame2 = LabelFrame(frame1,bd=2,bg="#f1e8fe",relief=RIDGE,text="Class Student Information",font=("Arial",12,"bold"),fg="navyblue")
        frame2.place(x=10,y=160,width=580,height=270)
        
        #Student id
        studentId_label = Label(frame2,text="Std-ID:",font=("Arial",12,"bold"),fg="navyblue",bg="#f1e8fe")
        studentId_label.place(x=10,y=20)
        
        studentId_entry = ttk.Entry(frame2,textvariable=self.var_std_id, width=15,font=("Arial",12,"bold"))
        studentId_entry.place(x=75,y=20)
        
        msg = Label(frame2,text='',bg='#f1e8fe')
        msg.place(x=75,y=45)
        
        #Student name
        student_name_label = Label(frame2,text="Std-Name:",font=("Arial",12,"bold"),fg="navyblue",bg="#f1e8fe")
        student_name_label.place(x=290,y=20)
        
        student_name_entry = ttk.Entry(frame2,textvariable=self.var_std_name,width=15,font=("Arila",12,"bold"))
        student_name_entry.place(x=380,y=20)
        
        msg2 = Label(frame2,text='',bg='#f1e8fe')
        msg2.place(x=380,y=45)
        
        #Gender
        student_gender_label = Label(frame2,text="Gender:",font=("Arial",12,"bold"),fg="navyblue",bg="#f1e8fe")
        student_gender_label.place(x=10,y=80)
        
        #combo box 
        gender_combo=ttk.Combobox(frame2,textvariable=self.var_gender,width=13,font=("Arial",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.place(x=80,y=80)
        
        #Email
        student_email_label = Label(frame2,text="Email:",font=("Arial",12,"bold"),fg="navyblue",bg="#f1e8fe")
        student_email_label.place(x=300,y=80)
        
        student_email_entry = ttk.Entry(frame2,textvariable=self.var_email,width=15,font=("Arial",12,"bold"))
        student_email_entry.place(x=360,y=80,width=200)
        
        msg3 = Label(frame2,text='',bg='#f1e8fe')
        msg3.place(x=360,y=105)
        
        #Phone Number
        student_mob_label = Label(frame2,text="Mob-No:",font=("Arial",12,"bold"),fg="navyblue",bg="#f1e8fe")
        student_mob_label.place(x=10,y=130)
        
        student_mob_entry = ttk.Entry(frame2,width=15,textvariable=self.var_mob,font=("Arisl",12,"bold"))
        student_mob_entry.place(x=80,y=130)
        
        msg4 = Label(frame2,text='',bg='#f1e8fe')
        msg4.place(x=80,y=155)
        
        
        radiobtn1=ttk.Radiobutton(frame2, text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=1,padx=300,pady=140,sticky=W)
        
        radiobtn1=ttk.Radiobutton(frame2,text="No Photo Sample",value="No")
        radiobtn1.grid(row=5,column=1,padx=450,pady=140,sticky=W)
        
        #Button Frame
        btn_frame = Frame(fr,bd=0,bg="#f1e8fe",relief=RIDGE)
        btn_frame.place(x=30,y=390,width=535,height=60)
                
        
        #save button
            
        save_btn=Button(btn_frame,command=lambda:(self.add_data() ,val_std_id(),val_std_name(),val_email(),val_mob()), text="Save",width=7,font=("Arial",12,"bold"),fg="white",bg="navyblue")
            
        save_btn.grid(row=0,column=0,padx=15,pady=10,sticky=W)
        
            
        #update button
        
            
        update_btn=Button(btn_frame,command=self.update_data, text="Update",width=7,font=("Arial",12,"bold"),fg="white",bg="navyblue")
            
        update_btn.grid(row=0,column=1,padx=15,pady=10,sticky=W)

        back_btn=Button(bg_img,command=self.go_back, text="Back",width=7,font=("Arial",12,"bold"),fg="white",bg="navyblue")
            
        back_btn.place(x=5,y=5,width=80,height=25)
        
            
        #delete button
        
            
        # del_btn=Button(btn_frame,text="Delete",width=7,font=("Arial",12,"bold"),fg="white",bg="navyblue")
            
        # del_btn.grid(row=0,column=2,padx=15,pady=10,sticky=W)
        
        
      
            
        # qr code button button
            
        qr_btn=Button(btn_frame,text="QR-Code", command=lambda:(self.genQR() ,val_std_id(),val_std_name(),val_email(),val_mob()), width=7,font=("Arial",12,"bold"),fg="white",bg="navyblue")
            
        qr_btn.grid(row=0,column=2,padx=1,pady=10,sticky=W)
        
        qr_btn=Button(btn_frame,text="Reset", command=lambda:(self.delete_data() ), width=7,font=("Arial",12,"bold"),fg="white",bg="navyblue")
            
        qr_btn.grid(row=0,column=4,padx=1,pady=10,sticky=W)
            
        #take photo button
        #take_photo_btn=Button(btn_frame,text="Take Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Pic",width=9,font=("Arial",12,"bold"),fg="white",bg="navyblue")
        
        take_photo_btn.grid(row=0,column=3,padx=15,pady=10,sticky=W)
            
        searchfr = LabelFrame(root,bd=2,bg="#f1e8fe",relief=SOLID,text="Search System",font=("Arial",12,"bold"),fg="navyblue",highlightcolor='black',highlightthickness=2)
        searchfr.place(x=680,y=155,width=555,height=130)
        
        search_label = Label(searchfr,text="Search:",font=("Arial",12,"bold"),fg="navyblue",bg="#f1e8fe")
        search_label.place(x=10,y=15)
        
        #combo box 
        search_combo=ttk.Combobox(searchfr,width=13,font=("Arial",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Student_ID")
        search_combo.current(0)
        search_combo.place(x=90,y=15)
        
        search_entry = ttk.Entry(searchfr,width=15,font=("Arial",12,"bold"))
        search_entry.place(x=260,y=15)

       
        
        search_btn=Button(searchfr,text="Search",width=9,font=("Arial",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=0,padx=435,pady=10,sticky=W)
        
        
        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(root,bd=2,bg="white",relief=RIDGE,highlightcolor='black',highlightthickness=2,highlightbackground='black')
        table_frame.place(x=680,y=230,width=555,height=410)
        
        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
                
        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","Email","Gender","Section","Phone","Year","Semister","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semister",text="semister")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"
        
                # Set Width of Colums 
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=150)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Section",width=50)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Year",width=100)    
        self.student_table.column("Semister",width=100)
        self.student_table.column("Photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


# ==================Function Decleration==============================
    def add_data(self):
        if self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_sec.get(),
                self.var_mob.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_photo.get(),
                
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
            conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
            mycursor = conn.cursor()

            mycursor.execute("select * from student")
            data=mycursor.fetchall()

            if len(data)!= 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
           
    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        
        self.var_email.set(data[2]),
        self.var_gender.set(data[3]),
        self.var_sec.set(data[4]),
        self.var_year.set(data[6]),
        self.var_semester.set(data[7]),
        
        self.var_mob.set(data[5]),
        self.var_photo.set(data[8])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_sec.get()==""  or self.var_gender.get()==""  or self.var_email.get()=="" or self.var_mob.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set year=%s,Semister=%s, Section=%s, Name=%s,Gender=%s,Email=%s,Phone=%s,status=%s where student_id=%s",( 
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_sec.get(),
                    self.var_std_name.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_mob.get(),
                    self.var_photo.get(),
                    self.var_std_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_divi.set("Morning"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT ID,Name,dep,course,year,sem,divison,gender,dob,mobile,address,roll,Email,Teacher,Photo FROM student where roll='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                my_cursor.execute("select * from student where roll= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def genQR(self):
          if self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
          else:
            try:
    
                    id=self.var_std_id.get()
                    fname=self.var_std_name.get()
                    section=self.var_sec.get()
                
                
                    with open('registerStudent.csv','a',newline='\n')as f:
                        writer= csv.writer(f)
                        writer.writerow([id,fname,section])
                    data=(f"{id},{fname},{section}")
                    img=qrcode.make(data)
                    img.save(f"./qrImage/{id}.png")
                
                    # Open the qr image file and create a photo image object
                    qr_img = Image.open(f"./qrImage/{id}.png")
                    qr_photo = ImageTk.PhotoImage(qr_img)
                
            
                    # Create a pop up window that will display the qr image
                    pop_up = tk.Toplevel()
                    pop_up.title("QR Code")
                
                    # Create a label widget that will show the photo image object
                    qr_label = tk.Label(pop_up, image=qr_photo)
                    qr_label.image = qr_photo # keep a reference to avoid garbage collection
                    qr_label.pack()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
                #=====================This part is related to Opencv Camera part=======================
                # ==================================Generate Data set take image=========================
                
    def generate_dataset(self):
        if self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1
                mycursor.execute("update student set name=%s,section=%s,year=%s,semister=%s,gender=%s,phone=%s,email=%s,status=%s where student_id=%s",( 
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_sec.get(),
                    self.var_std_name.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_mob.get(),
                    self.var_photo.get(),
                    self.var_std_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="img_data/student."+str(id)+"."+str(img_id)+".jpg"          
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==10:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def go_back(self):
        from admin import Admin
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        self.app = Admin(self.new_window)
#  main class object
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
