from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
import datetime
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import time

class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        self.var_dep=StringVar()
        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\matib\OneDrive\Desktop\MyFinal\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg2.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face and QR code Attendance taking Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        
        std_img_btnQR=Image.open(r"Images_GUI\qr1.png")
        std_img_btnQR=std_img_btnQR.resize((180,180),Image.ANTIALIAS)
        self.std_img2=ImageTk.PhotoImage(std_img_btnQR)

        std_img_btn=Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=700,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=700,y=350,width=180,height=45)
        # QR-code Button
        std_b1 = Button(bg_img,command=self.Qr_code,image=self.std_img2,cursor="hand2")
        std_b1.place(x=500,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.Qr_code,text="QR-code Scanner",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=500,y=350,width=180,height=45)

          # Current Course 
        current_course_frame = LabelFrame(bd=2,bg="white",relief=RIDGE,text="",font=("verdana",12,"bold"),fg="navyblue")
        current_course_frame.place(x=100,y=300,width=300,height=100)
         #label Department
        dep_label=Label(current_course_frame,text="name csv file",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=5,pady=15)

        #naming of the file name of attendance
    
        current_course_frame = ttk.Entry(current_course_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        current_course_frame.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        # def create_csv(self):       
        #     filename="f{d1}.csv"
        #     filepath= "C:/Users/matib/Videos/prooooo/MY_trial"
        #     path=os.path.join(filename, filepath)
        #     with open(filename,"w" ) as csfile:

        #         filewriter=csv.writer(filename, delimiter=',',
        #                               quotechar='|', quoting=csv.QUOTE_MINIMAL)

     
#=====================Attendance==============================


    def Qr_code(self):
        # header=['id','roll','name','time','date',]
        with open('./registerStudent.csv', 'r') as f:
             authorized_users = [l[:-1] for l in f.readlines() if len(l) > 2]
             f.close()

        log_path = './log.csv'
        with open(log_path, 'w') as f:
                            
            # f.write("id,roll,name,time,date,attend")

            cap = cv2.VideoCapture(0)

            most_recent_access = {}

            time_between_logs_th = 10

            while True:

                ret, frame = cap.read()

                qr_info = decode(frame)

                if len(qr_info) > 0:

                    qr = qr_info[0]

                    data = qr.data
                    rect = qr.rect
                    polygon = qr.polygon

                    if data.decode() in authorized_users:
                        cv2.putText(frame,'ACCESS GRANTED', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                        if data.decode() not in most_recent_access.keys() \
                                or time.time() - most_recent_access[data.decode()] > time_between_logs_th:
                            most_recent_access[data.decode()] = time.time()
                            with open(log_path, 'a') as f:
                            
                                f.write(" ")
                                f.write("\n{},{}".format(data.decode(), datetime.datetime.now()))
                                f.close()

                    else:
                        cv2.putText(frame, 'ACCESS DENIED', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                    frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),
                                        (0, 255, 0), 5)

                    frame = cv2.polylines(frame, [np.array(polygon)], True, (255, 0, 0), 5)

                cv2.imshow('webcam', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()

    def mark_attendance(self,i,n,r,filename):           
        with open(f"./att_reco/{filename}.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
               entry=line.split((","))
               name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
              now1=datetime.datetime.now()
              d1=now1.strftime("%d/%m/%Y")
              dtString=now1.strftime("%H:%M:%S")
              f.writelines(f"{i}, {n}, {r}, {dtString}, {d1},{filename}, Present\n")

    #==============================Face_Recognition==============================

    def face_recog(self):
        filename=self.var_dep.get()
        with open(f"./att_reco/{filename}.csv",'w') as file:
         writer=csv.writer(file)
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn = mysql.connector.connect(username='root', password='maty',host='localhost',database='smart_attendance',port=3306)
                cursor = conn.cursor()
                cursor.execute("select name from student where student_id="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select section from student where student_id="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select year from student where student_id="+str(id))
                i=cursor.fetchone()
                i="+".join(i)


                if confidence > 75:
                    cv2.putText(img,f"year:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"section:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,n,r,filename)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #=============================
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)



            if cv2.waitKey(1) & 0xFF == ord('q') :
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
