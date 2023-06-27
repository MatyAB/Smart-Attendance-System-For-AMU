from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from face_recognition import Face_Recognition
from attendance import Attendance
import mysql.connector
import cv2
import os
from attendance import Attendance
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from login import Login


class Lec:
    def __init__(self,root,lecture_email):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Lecture Pannel")



        self.lecture_email = lecture_email # use it as an instance attribute


        
    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\zzz.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=110)

         # backgorund image 
        bg1=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\f_bg.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=111,width=1366,height=768)

        imag=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\det1.jpg")
        imag=imag.resize((150,200),Image.LANCZOS)
        self.photoimag1=ImageTk.PhotoImage(imag)
                # set image as lable
        take_btn = Button(bg_img,image=self.photoimag1,cursor="hand2",command=self.attend)
        take_btn.place(x=400,y=120,width=180,height=180)
        
        image=Image.open(r"C:\Users\matib\OneDrive\Desktop\GC_2SEM\final\Images_GUI\att.jpg")
        image=image.resize((150,200),Image.LANCZOS)
        self.photoimag2=ImageTk.PhotoImage(image)
             # set image as lable
        view_btn = Button(bg_img,image=self.photoimag2,cursor="hand2",command=self.record)
        view_btn.place(x=650,y=120,width=180,height=180)
       
        lecturlbl = Label(bg_img,text="Lecture Pannel ",bg='#ffffff',fg='#270489',font=('Arial',32)).place(x=10,y=10,width=1257)
        takebtn = Button(bg_img,text='Take Attendance ',bg='#80d4e5',fg='#1f1f1f',font=('Arial',16),cursor='hand2',command=self.attend).place(x=400,y=302,width=200)
        viewbtn = Button(bg_img,text='View Attendance ',bg='#80d4e5',fg='#1f1f1f',font=('Arial',16),cursor='hand2',command=self.record).place(x=650,y=302,width=200)


    def attend(self):
                lecture_email = self.lecture_email
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window,lecture_email)
                # self.root.withdraw()

  
    def record(self):
                lecture_email = self.lecture_email
                self.new_window=Toplevel(self.root) # use name keyword argument
                self.app=Attendance(self.new_window,lecture_email)
                # self.root.withdraw()  
                
#  main class object
if __name__ == "__main__":
    root=Tk()
    obj=Lec(root,any)
    root.mainloop()

