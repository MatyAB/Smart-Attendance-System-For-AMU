from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import tkinter as tk




class lectureManage:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Faculty Manage Lecture account Pannel")

          # variable declaration..............
        self.var_course_id=StringVar()
        self.var_lec_id=StringVar()
        self.var_lec_password=StringVar()
        self.var_lec_phone=StringVar()
        self.var_lec_email=StringVar()


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
        title_lb1 = Label(bg_img,text="Lecture account ",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=580,y=660,width=960,height=580)
        # right_frame.place(x=980,y=10,width=660,height=480)

        # Student_course
        Student_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="navyblue")
        Student_course_frame.place(x=10,y=-25,width=635,height=270)

        #Lecture id
        studentId_label = Label(Student_course_frame,text="Lecture-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(Student_course_frame,textvariable=self.var_lec_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        # -----------------------------------------------------
     
        #Lecture id
        studentId_label = Label(Student_course_frame,text="Course-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(Student_course_frame,textvariable=self.var_course_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        # -----------------------------------------------------

     
         #delete button
        reset_btn=Button(Student_course_frame,command=self.delete_data,text="delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=3,column=0,padx=6,pady=10,sticky=W)
        # ===============================Table Sql Data View==========================


        # Left Label Frame 
        LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Lecture Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=400)


        table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=150,width=635,height=260)


        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Course",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=780,y=10,width=660,height=480)
        
        #update photo button
        update_photo_btn=Button(right_frame,command=self.Assign_Course,text="Assign Course",width=20,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_photo_btn.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        # Create a listbox for the courses
        self.course_listbox = tk.Listbox(right_frame, selectmode=tk.MULTIPLE,font=("verdana",12,"bold"),width=14,height=15)
        self.course_listbox.grid(row=0,column=3,padx=5,sticky=tk.W)

        # Connect to the database
        db = mysql.connector.connect( host="localhost", user="root", password="maty", database="smart_attendance")
        cursor = db.cursor()

        # Get the course names from the database
        cursor.execute("SELECT course_name FROM course")
        courses = cursor.fetchall()

        # Insert the course names into the listbox
        for course in courses:
            self.course_listbox.insert(tk.END, course[0])

       

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("Lec_Id","Lec_Name","Lec_Email","Course_Code","Course_Name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("Lec_Id",text="Lec_Id")
        self.attendanceReport.heading("Lec_Name",text="Lec_Name")
        self.attendanceReport.heading("Lec_Email",text="Lec_Email")
        self.attendanceReport.heading("Course_Code",text="Course_Code")
        self.attendanceReport.heading("Course_Name",text="Course_Name")
       

 # Set Width of Colums 
        self.attendanceReport.column("Lec_Id",width=100)
        self.attendanceReport.column("Lec_Name",width=100)
        self.attendanceReport.column("Lec_Email",width=100)
        self.attendanceReport.column("Course_Code",width=100)
        self.attendanceReport.column("Course_Name",width=100)
        self.attendanceReport["show"]="headings"
        
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_left)
        self.fetch_data()
        # ............ function declaration...............
             
             
    def Assign_Course(self):
        
            # Get the selected courses from the listbox
            selected_courses = [self.course_listbox.get(idx) for idx in self.course_listbox.curselection()]

            # Check if at least one course is selected
            if not selected_courses:
                        tk.messagebox.showerror("Error", "Please select at least one course.")
                        return

            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="maty", database="smart_attendance")
            cursor = db.cursor()

            # Get the lecture ID from the user input
            lecture_id = int(self.var_lec_id.get())

            # Insert a new enrollment record for each selected course
            for course_name in selected_courses:
                # Get the course ID from the database using the course name
                cursor.execute("SELECT course_id FROM course WHERE course_name=%s", (course_name,))
                course_id = cursor.fetchone()[0]

                # Insert the enrollment record into the database using the lecture ID and course ID
                sql = "INSERT INTO assign_course (lecture_id, course_idd) VALUES (%s, %s)"
                values = (lecture_id, course_id)
                try:
                    cursor.execute(sql, values)
                    db.commit()
                    # Show a success message
                    tk.messagebox.showinfo("Success", "Course assigned successfully.")
                except:
                    # Check if the error code is 1062 for duplicate entry
                   
                        # Show a warning message
                        tk.messagebox.showwarning("Warning", "This Course assigned before.")
                   

    # def Assign_Course(self):
       
    #     # Get the selected courses from the listbox
    #     selected_courses = [self.course_listbox.get(idx) for idx in self.course_listbox.curselection()]

    #     # Check if at least one course is selected
 
    #     if not selected_courses:
    #                 tk.messagebox.showerror("Error", "Please select at least one course.")
    #                 return
    #     lecture_id = int(self.var_lec_id.get())
    #     # Connect to the database
    #     db = mysql.connector.connect(host="localhost", user="root", password="maty", database="smart_attendance")
    #     cursor = db.cursor()

    #     # Insert a new enrollment record for each selected course
    #     for course_name in selected_courses:
    #         # Get the course ID from the database using the course name
    #         cursor.execute("SELECT course_id FROM course WHERE course_name=%s", (course_name,))
    #         course_id = cursor.fetchone()[0]

    #         # Insert the enrollment record into the database using the student ID and course ID
    #         sql = "INSERT INTO assign_course (lecture_id, course_idd) VALUES (%s, %s)"
    #         values = (lecture_id, course_id)
    #         cursor.execute(sql, values)
    #         db.commit()
  

    #     # Show a success message
    #     tk.messagebox.showinfo("Success", " course assigned successfully.")    


    # # ===========================fatch data form mysql attendance=====================

    def fetch_data(self):
        # Try to connect to database and execute query
        try:
            conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
            mycursor = conn.cursor()
            # Fix the syntax error in the query
            mycursor.execute("select lecture.lecture_id, lecture.name,lecture.email,assign_course.course_idd,course.course_name from lecture inner join assign_course on lecture.lecture_id=assign_course.lecture_id inner join course on course.course_id= assign_course.course_idd")
            data=mycursor.fetchall()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
            return 
        # Exit the function
        # Check if data is not empty
        if len(data)!= 0:
            # Clear the attendance report
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            # Insert the data into the attendance report
            for i in data:
                self.attendanceReport.insert("",END,values=i)
   

    def reset_data(self):
        self.var_course_id.set("")
        self.var_lec_name.set("")
    

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
            print(i)    

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_course_id.set(data[3]),
        self.var_lec_id.set(data[0]),
    

    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_course_id.get()=="":
            messagebox.showerror("Error","course Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from assign_course where course_idd=%s"
                    val=(self.var_course_id.get(),)
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


#  main class object
if __name__ == "__main__":
    root=Tk()
    obj=lectureManage(root)
    root.mainloop()