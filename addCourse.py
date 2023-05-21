from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# Testing Connection 


class addcourse:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Faculty add course Pannel")

          # variable declaration..............
        self.var_course_id=StringVar()
        self.var_course_name=StringVar()

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
        title_lb1 = Label(bg_img,text="add Course Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=680,y=660,width=660,height=480)

        # Student_course
        Student_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="navyblue")
        Student_course_frame.place(x=10,y=5,width=635,height=270)

        #Student id
        studentId_label = Label(Student_course_frame,text="Course-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(Student_course_frame,textvariable=self.var_course_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        # -----------------------------------------------------

         #Student name
        student_name_label = Label(Student_course_frame,text="Course-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(Student_course_frame,textvariable=self.var_course_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
      
# buttons

       #save button
        save_btn=Button(Student_course_frame,command=self.add_course,text="Add",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=3,column=1,padx=5,pady=10,sticky=W)

#Update button
        del_btn=Button(Student_course_frame,command=self.update_data,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=3,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(Student_course_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=3,column=3,padx=6,pady=10,sticky=W)

         #deletw button
        reset_btn=Button(Student_course_frame,command=self.delete_data,text="delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=3,column=0,padx=6,pady=10,sticky=W)
        # ===============================Table Sql Data View==========================

    

        # Left Label Frame 
        LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=400)


        table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=150,width=635,height=310)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("CourseId","CourseName"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("CourseId",text="Course-ID")
        self.attendanceReport.heading("CourseName",text="Course-Name")
       
 # Set Width of Colums 
        self.attendanceReport.column("CourseId",width=100)
        self.attendanceReport.column("CourseName",width=100)
       
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_left)
        self.fetch_data()
        # ............ function declaration...............
    def add_course(self):
                if self.var_course_id.get()=="" or self.var_course_name.get==""  :
                    messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
                    
                else:
                    try:
                        conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                        mycursor = conn.cursor()
                        mycursor.execute("insert into course values(%s,%s)",(
                        self.var_course_id.get(),
                        self.var_course_name.get()
                        
                       

                        ))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
                    except Exception as es:
                        messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def update_data(self):
            if self.var_course_id.get()=="" or self.var_course_name.get()=="" :
                messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
            else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to Update current Course!",parent=self.root)
                    if Update > 0:
                        conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                        mycursor = conn.cursor()
                        mycursor.execute("update course set course_name=%s where course_id=%s",( 

                        self.course_name.get(),
                        self.course_id.get()  
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
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from course")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()


    def reset_data(self):
        self.var_course_id.set("")
        self.var_course_id.set("")
    


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

        self.var_course_id.set(data[0]),
        self.var_course_name.set(data[1]),
       
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
                    sql="delete from course where course_id=%s"
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
    obj=addcourse(root)
    root.mainloop()