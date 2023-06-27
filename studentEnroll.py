from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter as tk

class EnrollStd:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")

        #-------------------------Variables-----------------------
        
        crs_entry=StringVar()
        id_entry=StringVar()

        def add_enrollment():
       
            # Get the selected courses from the listbox
            selected_courses = [self.course_listbox.get(idx) for idx in self.course_listbox.curselection()]

            # Check if at least one course is selected
            if not selected_courses:
                tk.messagebox.showerror("Error", "Please select at least one course.")
                return

            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="maty", database="smart_attendance")
            cursor = db.cursor()

            # Get the student ID from the user input
            student_id = int(id_entry.get())

            # Insert a new enrollment record for each selected course
            for course_name in selected_courses:
                # Get the course ID from the database using the course name
                cursor.execute("SELECT course_id FROM course WHERE course_name=%s", (course_name,))
                course_id = cursor.fetchone()[0]

                # Insert the enrollment record into the database using the student ID and course ID
                sql = "INSERT INTO std_enroll (student_id, course_id) VALUES (%s, %s)"
                values = (student_id, course_id)
                cursor.execute(sql, values)
                db.commit()

            # Show a success message
            tk.messagebox.showinfo("Success", "Enrollment added successfully.")

        def validation():
            spin = IDentry.get()
            if len(spin) == 0:
                msg.config(fg='red', text='ID can\'t remain empty')
            else:
                    if not spin.isdigit():
                        msg.config(fg='red', text='ID must be an integer')
                        IDentry.delete(0, END)
                    else:
                        msg.config(fg='#fff', text='', font=('sans-serif', 14))
                        IDentry.delete(0, END)   
        def val_crs_name():
            name = name_entry.get()
            if len(name) == 0:
              msg2.config(fg='red', text='Name can\'t be empty',bg='#f0f0f0',font=('arial',10))
              name_entry.delete(0, END)
            else:
                try:
                    if len(name)>100:
                        msg2.config(fg='red',text='Nameis too long',bg='#f0f0f0',font=('arial',10))
                        name_entry.delete(0, END)
                    elif name.isdigit():
                        msg2.config(fg='red',text='Name can\'t be a number',bg='#f0f0f0',font=('arial',10)) 
                        name_entry.delete(0, END)     
                    elif any(ch.isdigit() for ch in name):
                        msg2.config(fg='red',text='Name can\'t have numbers',font=('arial',10))
                        name_entry.delete(0, END)
                    else:
                        msg2.config(text='')
                        name_entry.delete(0, END)
                except Exception as ep:
                    messagebox.showerror('error', ep)                                              
        
          # ............ function declaration...............
        def add_course():
                if IDentry.get()=="" or name_entry.get==""  :
                        messagebox.showerror("Error","Please Fill All Fields are Required!",parent=root)
                            
                else:
                    try:
                                conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                                mycursor = conn.cursor()
                                mycursor.execute("insert into course values(%s,%s)",(
                                IDentry.get(),
                                name_entry.get()
                           
        
                                ))
                                conn.commit()
                                fetch_data()
                                conn.close()
                                IDentry.delete(0, END)
                                name_entry.delete(0,END)
        
                                messagebox.showinfo("Success","All Records are Saved!",parent=root)
                    except Exception as es:
                                messagebox.showerror("Error",f"Due to: {str(es)}",parent=root)
        
        
        
        def delete_data():
                if IDentry.get()=="":
                    messagebox.showerror("Error","course Id Must be Required!",parent=root)
                else:
                    try:
                        delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=root)
                        if delete>0:
                            conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='face_recognizer',port=3306)
                            mycursor = conn.cursor() 
                            sql="delete from course where course_id=%s"
                            val=(IDentry.get(),)
                            mycursor.execute(sql,val)
                            IDentry.delete(0, END)
        
                        else:
                            if not delete:
                                return
        
                        conn.commit()
                        fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete","Successfully Deleted!",parent=root)
                    except Exception as es:
                        messagebox.showerror("Error",f"Due to: {str(es)}",parent=root) 
        
        
                                # ===========================fatch data form mysql attendance=====================
        
        def fetch_data():
                conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                mycursor = conn.cursor()
        
                mycursor.execute("select student_id, name from student")
                data=mycursor.fetchall()
        
                if len(data)!= 0:
                    tv.delete(*tv.get_children())
                    for i in data:
                        tv.insert("",END,values=i)
                    conn.commit()
                conn.close()
        def fetchData(rows):
            global mydata
            mydata = rows
            tv.delete(*tv.get_children())
            for i in rows:
                tv.insert("",END,values=i)
                print(i)    
        def get_cursor_left(event=""):
            cursor_focus = tv.focus()
            content = tv.item(cursor_focus)
            data = content["values"]
        
            id_entry.set(data[0]),
            crs_entry.set(data[1])


    


    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

        fr = Frame(bg_img,bg='#f1e8fe',highlightbackground='black', highlightcolor='black',highlightthickness=2,bd=5).place(x=200,y=10,width=500,height=500)
     
        #===============Lbel frame for all==============================
     
        lblfr1 = LabelFrame(bg_img,bd=2, bg="#f1e8fe",relief=SOLID,font=("Arial",12,"bold"),fg="navyblue",highlightbackground='black')
        lblfr1.place(x=210,y=25,width=480,height=475)
       
        lblfr = LabelFrame(lblfr1,text='' ,bd=1, bg="#f1e8fe",relief=RIDGE,font=("Arial",12,"bold"),fg="navyblue")
        lblfr.place(x=20,y=20,width=440,height=180)
        
        IDlabel = Label(lblfr,text='Student ID',bg='#f1e8fe',font=('Arial',15),fg="navyblue").place(x=20,y=20)
       
        IDentry = ttk.Entry(lblfr,textvariable=id_entry,font=('Arial',15,'bold'))
        IDentry.place(x=140,y=20)
       
        msg = Label(lblfr,text='',bg='#f1e8fe')
        msg.place(x=140,y=50)
        
        crslabel = Label(lblfr,text='Student Name',bg='#f1e8fe',font=('Arial',15),fg="navyblue").place(x=20,y=100)
       
        name_entry = ttk.Entry(lblfr,textvariable=crs_entry,font=('Arial',15,'bold'))
        name_entry.place(x=150,y=100)
       
        msg2 = Label(lblfr,text='',bg='#f1e8fe')
        msg2.place(x=150,y=135)
        addlbl = Label(root,text=' Enroll a student',bg='#ffffff',fg='#270489',font=('Arial',32)).place(x=5,y=70,width=1400)

        #=============LABEl frame for buttons===============
        lblfr2 = LabelFrame(lblfr1,text='' ,bd=1, bg="#f1e8fe",relief=RIDGE,font=("Arial",12,"bold"),fg="navyblue")
        lblfr2.place(x=20,y=220,width=440,height=100)
      
        addbtn = Button(lblfr2,text='Add ',bg='#270489',fg='#f1e8fe',font=('Arial',15),command= lambda: (add_enrollment(), validation(),val_crs_name())).place(x=30,y=20,width=100)
        updtbtn = Button(lblfr2,text='Update ',font=('Arial',15),bg='#270489',fg='#f1e8fe').place(x=160,y=20,width=100)
      
        # resttbtn = Button(fr,text='Reset ',font=('Arial',15),bg='#270489',fg='#f1e8fe').place(x=540,y=350)
        deltbtn = Button(lblfr2,text='Delete ',font=('Arial',15),bg='#270489',fg='#f1e8fe').place(x=290,y=20,width=100)
        backbtn = Button(root,command=self.go_back, text='Back ',font=('Arial',15),bg='#270489',fg='#f1e8fe').place(x=20,y=75,width=100)

        # ======tree view frame===========
        fra = Frame(bg_img,bg='black').place(x=702,y=10,width=300,height=68)
        
        tree_frame = Frame(bg_img,bg='#12cafd',highlightcolor='black',highlightthickness=1)
        tree_frame.place(x=702,y=80,width=300,height=430)
        lblfr2 = LabelFrame(tree_frame,bd=2, bg="white",relief=SOLID,font=("Arial",12,"bold"),fg="navyblue",highlightbackground='black')
        lblfr2.place(x=810,y=200,width=250,height=355)
        scroll_x = ttk.Scrollbar(tree_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tree_frame,orient=VERTICAL)

        # course list box 
          # Create a listbox for the courses
        list_frame = Frame(bg_img,bg="#f1e8fe",highlightcolor='black',highlightthickness=1)
        list_frame.place(x=1003,y=10,width=200,height=500)
        self.course_listbox = tk.Listbox(list_frame, selectmode=tk.MULTIPLE,bg="#f1e8fe",relief=SOLID,font=("Arial",14,"bold"),fg="navyblue",highlightbackground='black',width=14,height=15)
        self.course_listbox.place(x=5,y=70,width=150,height=400)

        # Connect to the database
        db = mysql.connector.connect( host="localhost", user="root", password="maty", database="smart_attendance")
        cursor = db.cursor()

        # Get the course names from the database
        cursor.execute("SELECT course_name FROM course")
        courses = cursor.fetchall()

        # Insert the course names into the listbox
        for course in courses:
            self.course_listbox.insert(tk.END, course[0])
        
        
        style = ttk.Style()
        style.configure("mystyle.Treeview",font=('Arial',13),rowheight=50)
        style.configure("mystyle.Treeview.Heading",font=('Arial',13))
        tv = ttk.Treeview(tree_frame,columns=(1,2),style="mystyle.Treeview",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=tv.xview)
        scroll_y.config(command=tv.yview)
        tv.heading("1",text="Student ID")
        tv.column("1",width="150")
        tv.heading("2",text="Student Name")
        tv.column("2",width="150")
        tv["show"]='headings'
        tv.pack()
        tv.bind("<ButtonRelease>",get_cursor_left)
        fetch_data()


    def go_back(self):
        from admin import Admin
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        self.app = Admin(self.new_window)    
#  main class object
if __name__ == "__main__":
    root=Tk()
    obj=EnrollStd(root)
   

    root.mainloop()
