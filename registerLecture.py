from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# from admin import Admin
import mysql.connector
import tkinter as tk
import hashlib
from passlib.hash import pbkdf2_sha256



class RegisterLecture:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")
        img=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

# class RegisterLecture:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Register")
#         self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_lec_id=StringVar()
        self.var_lec_name=StringVar()
        self.var_lec_phone=StringVar()
        self.var_lec_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        def val_tch_id():
            spin = self.txtuser.get()
            if len(spin) == 0:
                 msg.config(fg='red', text='ID can\'t remain empty',bg='#f2f2f2',font=('arial',10))
            else:
                 if not spin.isdigit():
                    msg.config(fg='red', text='ID must be an integer',bg='#f2f2f2',font=('arial',10))
                 else:
                    msg.config(fg='#fff', text='', bg='#f2f2f2',font=('arial',10))
                    # self.txtuser.delete(0, END)
	    		
    
        def val_tch_name():
            name = self.txtname.get()
            
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
                        # self.txtname.delete(0, END)
                except Exception as ep:
                    messagebox.showerror('error', ep)

        def val_email():
            email =self.txtemail.get()
            special_ch = ['@', '.']
            if len(email) == 0:
                msg3.config(fg='red', text='email can\'t remain empty',bg='#f1e8fe',font=('arial',10))                  
            elif not any(ch in special_ch for ch in email):
                msg3.config(fg='red',text='invalid email!',font=('arial',10))
            
            else:
                msg3.config(text='')
                # self.txtemail.delete(0, END)              
            
        def val_mob():
            mbl = self.txtphone.get()

            if len(mbl) == 0:
                msg4.config(fg='red', text='Mobile number can\'t be empty',bg='#f0f0f0',font=('arial',10))
                if any(ch.isdigit() for ch in mbl):
                    if len(mbl) == 10:
                        mob = int(mbl)
                        msg4.config(fg='red',text='',font=('arial',10))
                        # self.txtphone.delete(0, END)
                    else:
                        msg4.config(fg='red',text='Invalid mobile number',font=('arial',10))
            elif not mbl.isdigit():
                msg4.config(fg='red', text='Mob-number must be an integer',bg='#f1e8fe',font=('arial',10))

        def val_pssw():
            password = self.txtpss.get()
            special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[',
']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
            msg5 = Label(frame1,text='',bg='#f1e8fe')
            msg5.place(x=440,y=420)
            if len(password) == 0:
                msg5.config( text='Password can\'t be empty')
            else:
                
                if not any(ch in special_ch for ch in password):
                    msg5.config(text='Atleast 1 special character required!')
                elif not any(ch.isupper() for ch in password):
                    msg5 = 'Atleast 1 uppercase character required!'
                elif not any(ch.islower() for ch in password):
                    msg5 = 'Atleast 1 lowercase character required!'
                elif not any(ch.isdigit() for ch in password):
                    msg5 = 'Atleast 1 number required!'
                elif len(password) < 8:
                    msg5 = 'Password must be minimum of 8 characters!'
                else:
                    msg5 = ''

      
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
        fr.place(x=55,y=155,width=1366,height=760)
        # pannel_lbl = Label(root,text='Student Pannel ',bg='#051344',fg='#ffffff',font=('Arial',32)).place(x=500,y=70)
        frame1 = LabelFrame(fr,bd=2, bg="#f1e8fe",relief=SOLID,text="Lecture Details",font=("Arial",12,"bold"),fg="navyblue",highlightbackground='black')
        frame1.place(x=10,y=5,width=650,height=450)

        lname =lb1= Label(frame1,text="Lecture ID:",font=("times new roman",15,"bold"),fg="#002B53",bg="#f1e8fe")
        lname.place(x=20,y=20)

        #entry1 
        self.txtuser=ttk.Entry(frame1,textvariable=self.var_lec_id,font=("times new roman",15,"bold"))
        self.txtuser.place(x=20,y=50,width=270)
        msg = Label(frame1,text='',bg='#f1e8fe')
        msg.place(x=20,y=105)

        #label2 
        lname =lb1= Label(frame1,text="Lecture Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#f1e8fe")
        lname.place(x=20,y=110)

        #entry2 
        self.txtname=ttk.Entry(frame1,textvariable=self.var_lec_name,font=("times new roman",15,"bold"))
        self.txtname.place(x=20,y=145,width=280)

        msg2 = Label(frame1,text='',bg='#f1e8fe')
        msg2.place(x=60,y=180)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame1,text="Phone:",font=("times new roman",15,"bold"),fg="#002B53",bg="#f1e8fe")
        cnum.place(x=350,y=20)

        #entry1 
        self.txtphone=ttk.Entry(frame1,textvariable=self.var_lec_phone,font=("times new roman",15,"bold"))
        self.txtphone.place(x=350,y=50,width=270)
        msg3 = Label(frame1,text='',bg='#f1e8fe')
        msg3.place(x=350,y=105)


        #label2 
        email =lb1= Label(frame1,text="Email",font=("times new roman",15,"bold"),fg="#002B53",bg="#f1e8fe")
        email.place(x=350,y=110)

        #entry2 
        self.txtemail=ttk.Entry(frame1,textvariable=self.var_lec_email,font=("times new roman",15,"bold"))
        self.txtemail.place(x=350,y=145,width=270)

        msg4 = Label(frame1,text='',bg='#f1e8fe')
        msg4.place(x=350,y=180)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame1,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#f1e8fe")
        ssq.place(x=20,y=200)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame1,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=20,y=235,width=270)


        #label2 
        sa =lb1= Label(frame1,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#f1e8fe")
        sa.place(x=20,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=20,y=305,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#f1e8fe")
        pwd.place(x=350,y=200)

        #entry1 
        self.txtpss=ttk.Entry(frame1,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtpss.place(x=350,y=235,width=270)

        


        # #label2 
        # cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        # cpwd.place(x=430,y=430)

        # #entry2 
        # self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        # self.txtpwd.place(x=433,y=455,width=270)

        # Creating Button Register
        loginbtn=Button(frame1,command=lambda:(self.reg(), val_tch_id(),val_tch_name(),val_email(),val_mob(),val_pssw),text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC",cursor='hand2')
        loginbtn.place(x=23,y=370,width=130,height=35)

       # Creating Button Register
        loginbtn=Button(frame1,command=self.update_data,text="Update",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC",cursor='hand2')
        loginbtn.place(x=185,y=370,width=130,height=35)
          # Creating Button Delete
        loginbtn=Button(frame1,command=self.delete_data,text="Delete",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC",cursor='hand2')
        loginbtn.place(x=340,y=370,width=130,height=35)

           # Creating Button Register
        loginbtn=Button(frame1,command=self.go_back,text="Back",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="#f2f2f2",activeforeground="white",activebackground="#007ACC",cursor='hand2')
        loginbtn.place(x=500,y=370,width=130,height=35)

        

        frame2= Frame(fr,bg="#F2F2F2")
        frame2.place(x=665,y=5,width=600,height=450)

# table for lecture account
#scroll bar 
        scroll_x = ttk.Scrollbar(frame2,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(frame2,orient=VERTICAL)

        #create table 
        self.lectureAccount = ttk.Treeview(frame2,column=("LecureId","LectureName","Email","Phone","SecurityQuestion","SecurityAnswer","Password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.lectureAccount.xview)
        scroll_y.config(command=self.lectureAccount.yview)

        self.lectureAccount.heading("LecureId",text="Lecture-ID")
        self.lectureAccount.heading("LectureName",text="Lecture-Name")
        self.lectureAccount.heading("Email",text="Email")
        self.lectureAccount.heading("Phone",text="Phone")
        self.lectureAccount.heading("SecurityQuestion",text="SecurityQuestion")
        self.lectureAccount.heading("SecurityAnswer",text="SecurityAnswer")
        self.lectureAccount.heading("Password",text="Password")


        # Set Width of Colums 
        self.lectureAccount.column("LecureId",width=100)
        self.lectureAccount.column("LectureName",width=100)
        self.lectureAccount.column("Email",width=100)
        self.lectureAccount.column("Phone",width=100)
        self.lectureAccount.column("SecurityQuestion",width=100)
        self.lectureAccount.column("SecurityQuestion",width=100)
        self.lectureAccount.column("Password",width=100)
        self.lectureAccount["show"]="headings"
       
    
        self.lectureAccount.pack(fill=BOTH,expand=1)
        self.lectureAccount.bind("<ButtonRelease>",self.get_cursor_left1)
        self.fetch_data()
        # ............ function declaration..................

    def reg(self):
        if (self.var_lec_id.get()=="" or self.var_lec_name.get()=="" or self.var_lec_phone.get()=="" or self.var_lec_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" ):
            messagebox.showerror("Error","All Field Required!")
        # elif(self.var_pwd.get() != self.var_cpwd.get()):
        #     messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        else:
            try:
                password = self.var_pwd.get()
                hash_object = hashlib.sha256(password.encode())
                hashed_passw = pbkdf2_sha256.encrypt(password)

                    
                conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                mycursor = conn.cursor()
                query=("select * from lecture where email=%s")
                value=(self.var_lec_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into lecture values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_lec_id.get(),
                    self.var_lec_name.get(),
                    self.var_lec_email.get(),
                    self.var_lec_phone.get(),
                    self.var_ssq.get(),
                    self.var_sa.get(),
                    hashed_passw
                    ))
                # def encrypt_password(password):
                    

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    


    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from lecture")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.lectureAccount.delete(*self.lectureAccount.get_children())
            for i in data:
                self.lectureAccount.insert("",END,values=i)
            conn.commit()
        conn.close()


    def reset_data(self):
        self.var_lec_id.set(""),
        self.var_lec_name.set(""),
        self.var_lec_phone.set("")
        self.var_lec_email.set(""),
        self.var_ssq.set(""),
        self.var_sa.set(""),
        self.var_pwd.set(""),
    
    



    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.lectureAccount.delete(*self.lectureAccount.get_children())
        for i in rows:
            self.lectureAccount.insert("",END,values=i)
            print(i)    

    def get_cursor_left1(self,event=""):
        cursor_focus = self.lectureAccount.focus()
        content = self.lectureAccount.item(cursor_focus)
        data = content["values"]

        self.var_lec_id.set(data[0]),
        self.var_lec_name.set(data[1]),
        self.var_lec_email.set(data[2]),
        self.var_lec_phone.set(data[3]),
        self.var_ssq.set(data[4]),
        self.var_sa.set(data[5]),
        self.var_pwd.set(data[6]),
        
    #    update lecture function
    def update_data(self):
        password = self.var_pwd.get()
        hash_object = hashlib.sha256(password.encode())
        hashed_passw = pbkdf2_sha256.encrypt(password)

        # Check if any field is empty
        if self.var_lec_id.get()=="" or self.var_lec_name.get()=="" or self.var_lec_phone.get()=="" or self.var_lec_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
            return # Exit the function
        # Check if passwords match
        # if self.var_pwd.get() != self.var_cpwd.get():
        #     messagebox.showerror("Error","Passwords do not match!",parent=self.root)
        #     return # Exit the function
        # Confirm update
        Update=messagebox.askyesno("Update","Do you want to Update current account!",parent=self.root)
        if not Update:
            return # Exit the function
        # Try to connect to database and execute query
        try:
            conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("update lecture set name=%s,email=%s,phone=%s,s_question=%s,s_answer=%s,password=%s where lecture_id=%s",( 
                self.var_lec_name.get(),
                self.var_lec_email.get(),
                self.var_lec_phone.get(),
                self.var_ssq.get(),
                self.var_sa.get(),
                hashed_passw,
                self.var_lec_id.get()
            )
            )

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
            self.fetch_data()
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_lec_id.get()=="":
            messagebox.showerror("Error","course Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from lecture where lecture_id=%s"
                    val=(self.var_lec_id.get(),)
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

    def go_back(self):
            from admin import Admin
            self.root.withdraw()
            self.new_window=Toplevel(self.root)
            self.app=Admin(self.new_window)  
            
                  

if __name__ == "__main__":
    root=Tk()
    app=RegisterLecture(root)
    root.mainloop()