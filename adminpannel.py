from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# Testing Connection 


class Admin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Admin Pannel")

          # variable declaration..............
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_std_email=StringVar()
        self.var_std_section=StringVar()
        self.var_std_year=StringVar()
        self.var_std_gender=StringVar()
        self.var_std_phone=StringVar()
        self.var_coure_id=StringVar()
        self.var_lec_name=StringVar()
        self.var_dep_id=StringVar()
        self.var_dep_name=StringVar()
        self.var_lecture_id=StringVar()
        self.var_lecture_name=StringVar()
        self.var_lecture_email=StringVar()
        self.var_lecture_phone=StringVar()

 # first header image  
        img=Image.open(r"C:\Users\matib\OneDrive\Desktop\MyFinal\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

         # backgorund image 
        bg1=Image.open(r"C:\Users\matib\OneDrive\Desktop\MyFinal\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Admin Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        # Student_course
        Student_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="navyblue")
        Student_course_frame.place(x=10,y=5,width=635,height=270)

        #Student id
        studentId_label = Label(Student_course_frame,text="Std-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(Student_course_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        # -----------------------------------------------------

         #Student name
        student_name_label = Label(Student_course_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(Student_course_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        #label section
        cou_label=Label(Student_course_frame,text="Section",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=1,column=0,padx=5,pady=15)

        #combo box 
        cou_combo=ttk.Combobox(Student_course_frame,textvariable=self.var_std_section,width=15,font=("verdana",12,"bold"),state="readonly")
        cou_combo["values"]=("A","B","C","D","E")
        cou_combo.current(0)
        cou_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        #-------------------------------------------------------------
       #Email
        student_email_label = Label(Student_course_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(Student_course_frame,textvariable=self.var_std_email,width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #label Gender
        year_label=Label(Student_course_frame,text="Gender",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=2,column=0,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(Student_course_frame,textvariable=self.var_std_gender,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Gender","Male","Female",)
        year_combo.current(0)
        year_combo.grid(row=2,column=1,padx=5,pady=15,sticky=W)

        #-----------------------------------------------------------------
       #Phone Number
        student_mob_label = Label(Student_course_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(Student_course_frame,textvariable=self.var_std_phone,width=15,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

          #label year
        cou_label=Label(Student_course_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=3,column=0,padx=5,pady=15)

        #combo box 
        cou_combo=ttk.Combobox(Student_course_frame,textvariable=self.var_std_year,width=15,font=("verdana",12,"bold"),state="readonly")
        cou_combo["values"]=("1 st","2 nd","3 rd","4 th","5 th")
        cou_combo.current(0)
        cou_combo.grid(row=3,column=1,padx=5,pady=15,sticky=W)
   
# buttons

       #save button
        save_btn=Button(Student_course_frame,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=4,column=0,padx=5,pady=10,sticky=W)


        # ............ function declaration...............
    def add_data(self):
                if self.var_std_id.get()=="" or self.var_std_name.get==""  or self.var_std_email.get()==""  or  self.var_std_section.get()=="Select Section" or  self.var_std_gender.get()=="Select Gender" or self.var_std_phone.get()=="" or self.var_std_year.get()=="Select Year" :
                    messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
                    
                else:
                    try:
                        conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                        mycursor = conn.cursor()
                        mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_std_email.get(),
                        self.var_std_section.get(),
                        self.var_std_gender.get(),
                        self.var_std_phone.get(),
                        self.var_std_year.get(),

                        ))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
                    except Exception as es:
                        messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)






        


#  main class object
if __name__ == "__main__":
    root=Tk()
    obj=Admin(root)
    root.mainloop()