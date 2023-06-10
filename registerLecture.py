from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class RegisterLecture:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

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



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\matib\OneDrive\Desktop\MyFinal\Images_GUI\bgReg.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=10,y=80,width=720,height=560)

        frame2= Frame(self.root,bg="#F2F2F2")
        frame2.place(x=750,y=80,width=600,height=560)

        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=300,y=130)

        #label1 
        fname =lb1= Label(frame,text="Lecture ID:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=50,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_lec_id,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=225,width=270)

        #label2 
        lname =lb1= Label(frame,text="Lecture Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=50,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lec_name,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=50,y=295,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Phone:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=430,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_lec_phone,font=("times new roman",15,"bold"))
        self.txtuser.place(x=433,y=225,width=270)


        #label2 
        email =lb1= Label(frame,text="Email",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=430,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lec_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=433,y=295,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=50,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=50,y=375,width=270)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=50,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=50,y=445,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=433,y=350)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=433,y=375,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=430,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=433,y=445,width=270)

        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=23,y=510,width=130,height=35)

       # Creating Button Register
        loginbtn=Button(frame,command=self.update_data,text="Update",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=185,y=510,width=130,height=35)
          # Creating Button Delete
        loginbtn=Button(frame,command=self.delete_data,text="Delete",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=340,y=510,width=130,height=35)

           # Creating Button Register
        loginbtn=Button(frame,command=self.reset_data,text="Reset",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=500,y=510,width=130,height=35)



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
        if (self.var_lec_id.get()=="" or self.var_lec_name.get()=="" or self.var_lec_phone.get()=="" or self.var_lec_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        else:
            messagebox.showinfo("Successfully","Successfully Register!")
            try:
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
                    self.var_pwd.get()
                    ))

                    conn.commit()
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
        # Check if any field is empty
        if self.var_lec_id.get()=="" or self.var_lec_name.get()=="" or self.var_lec_phone.get()=="" or self.var_lec_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
            return # Exit the function
        # Check if passwords match
        if self.var_pwd.get() != self.var_cpwd.get():
            messagebox.showerror("Error","Passwords do not match!",parent=self.root)
            return # Exit the function
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
                self.var_pwd.get(),
                self.var_lec_id.get()
            ))

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

        

if __name__ == "__main__":
    root=Tk()
    app=RegisterLecture(root)
    root.mainloop()