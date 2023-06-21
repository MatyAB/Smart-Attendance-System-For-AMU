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
import tkinter as tk


class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        self.var_course=StringVar()
        self.var_section=StringVar()
        self.var_lecture = tk.StringVar()
        self.var_student=StringVar()
        self.var_recognized_ids = set()  

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
        std_b1 = Button(bg_img,command=self.mark_attendanceQR,image=self.std_img2,cursor="hand2")
        std_b1.place(x=500,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.mark_attendanceQR,text="QR-code Scanner",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=500,y=350,width=180,height=45)

          # Current Course 
        current_course_frame =Label (bg_img,bd=2,bg="white",relief=RIDGE,text="",font=("verdana",12,"bold"),fg="navyblue")
        current_course_frame.place(x=100,y=170,width=350,height=170)
         #label Department
        dep_label=Label(current_course_frame,text="Select section",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=5,pady=15)

        dep_label=Label(current_course_frame,text="Select course",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=1,column=0,padx=5,pady=15)


        # button that send student record to attendancce table
        std_b1_1 = Button(current_course_frame,command=self.move_attd,text="submit",cursor="hand2",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        std_b1_1.grid(row=2,column=0,padx=5,pady=15)


               
            # Connect to the database
        db = mysql.connector.connect( host="localhost", user="root", password="maty", database="smart_attendance")
        cursor = db.cursor()

        # Get the course names from the database
        # cursor.execute("SELECT course_id from assign_course WHERE lecture_id={1221}")
        cursor.execute("SELECT course_idd FROM assign_course where lecture_id=3")
        courses = cursor.fetchall()
        # this code used for fetching lecture id for attendance purpose 
        cursor.execute("select email from lecture where lecture_id=3")
        row=cursor.fetchone()
        # Access the first element of the tuple to get the email value
        # self.var_lecture = row[0]
        self.var_lecture.set(row[0])
        # Create the gender_combo widget
        self.gender_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=13,font=("verdana",12,"bold"),state="readonly")
       
        self.gender_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        # Update the values of the gender_combo widget with the course names
        values = [course[0] for course in courses]
        self.gender_combo.config(values=values)

      
        #naming of the file name of attendance
        gender_combo=ttk.Combobox(current_course_frame,textvariable=self.var_section,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("A","B","C","D","E")
        gender_combo.current(0)
        gender_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

     
  


    def mark_attendanceQR(self):

        """Mark the attendance of a student in a course."""
        section = self.var_section.get()
        lecture = self.var_lecture.get()
        course=self.var_course.get()
        time1 = datetime.datetime.now().strftime("%H:%M:%S")
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        
        # Read the authorized users from the csv file
        with open("./registerStudent.csv", "r") as f:
            authorized_users = [l[:-1] for l in f.readlines() if len(l) > 2]
            f.close()
        # Open the log file for writing
        log_path = './log.csv'
        with open(log_path, 'a') as f:

            # Capture video from the camera
            cap = cv2.VideoCapture(0)

            # Keep track of the most recent access time for each user
            most_recent_access = {}

            # Set a threshold for logging time between accesses
            time_between_logs_th = 100

            # Loop until the user presses q
            while True:

                # Read a frame from the camera
                ret, frame = cap.read()

                # Decode the QR info from the frame
                qr_info = decode(frame)

                # If there is any QR info, process it
                if len(qr_info) > 0:

                    # Get the data, rect and polygon from the first QR info
                    qr = qr_info[0]
                    data = qr.data
                    rect = qr.rect
                    polygon = qr.polygon
                    conn = mysql.connector.connect(username="root", password="maty", host="localhost", database="smart_attendance", port=3306)
                    cur = conn.cursor()
                    # Check if the data is in the authorized users list
                    if data.decode() in authorized_users:
                        # Display a green message on the frame
                        cv2.putText(frame, "GRANTED", (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                        # Check if the data is not in the most recent access dict or if the time difference is greater than the threshold
                        if data.decode() not in most_recent_access or time.time() - most_recent_access[data.decode()] > time_between_logs_th:
                            # Update the most recent access time for the data
                            most_recent_access[data.decode()] = time.time()
                            student_id, name, sectionQ = data.decode().split(",")
                            # Write a log entry to the file with the data and datetime
                            with open(log_path, 'a') as f:
                
                                    f.write(" ")
                                    f.write("\n{},{}".format(data.decode(), datetime.datetime.now()))
                                    f.close()
                                    # cur.execute("select student_id from std_enroll where student_id=%s AND course_id=%s", (student_id, course))
                                    cur.execute("SELECT std_enroll.student_id FROM std_enroll JOIN student ON std_enroll.student_id = student.student_id WHERE std_enroll.student_id=%s AND std_enroll.course_id=%s AND student.section=%s",
                                      (student_id, course, section),)


                                    
                # Check if the query returns any rows
                            if cur.fetchone():
                                
                                # Insert the data into the attd table
                                cur.execute("INSERT INTO attd VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)", (name, student_id, lecture, course, section, date, time1, "Present"))
                                
                                # cur.execute("INSERT INTO attd VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)", (n,student_id,lecture,course,section,d1,dtString, "Present"))
                                # Add the student ID to the recognized set
                                self.var_recognized_ids.add(student_id)
                            #         cur.execute("select student_id from std_enroll where student_id=%s AND course_id=%s", (id, course))
                            # # Fetch one row from the cursor as a tuple
                            #         row = cur.fetchone()
                            #         cur.execute("INSERT INTO attd VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)", (name, id, lecture, course, section, date, time1, "Present"))
                            #     # Save the changes to the database
                                conn.commit()
                            conn.close()
                            self.move_att(student_id)
 
                    else:
                        cv2.putText(frame, 'ACCESS DENIED', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                    frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),
                                        (0, 255, 0), 5)

                    frame = cv2.polylines(frame, [np.array(polygon)], True, (255, 0, 0), 5)

                # Display the frame on a window named "QR Code Scanner"
                cv2.imshow("QR Code Scanner", frame)

                # Wait for 1 millisecond for a key press
                key = cv2.waitKey(1)

                # If the key is q, break out of the loop
                if key == ord("q"):
                    break

            # Release the camera resource
            cap.release()

            # Destroy all windows
            cv2.destroyAllWindows()
   
# Create a set to store the recognized student IDs

    def mark_attendance(self,i,n,r,course,student_id): 
        section=self.var_section.get()
        lecture=self.var_lecture.get()          
        with open(f"./att_reco/{course}.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            id_list=[]
            for line in myDatalist:
                entry=line.split((","))
                id_list.append(entry[1]) # Assuming the second column contains the student IDs

            if((student_id not in id_list)) and ((student_id not in self.var_recognized_ids)):
                now1=datetime.datetime.now()
                d1=now1.strftime("%d/%m/%Y")
                dtString=now1.strftime("%H:%M:%S")
                f.writelines(f" {n},{student_id},{lecture},{course}, {section}, {d1}, {dtString}, Present\n")

                conn = mysql.connector.connect( host="localhost", user="root", password="maty", database="smart_attendance")
                
                cur = conn.cursor()
    
                # Execute the query to check if the student is registered for the course and section
                cur.execute("SELECT std_enroll.student_id FROM std_enroll JOIN student ON std_enroll.student_id = student.student_id WHERE std_enroll.student_id=%s AND std_enroll.course_id=%s AND student.section=%s",
                (student_id, course, section),)
              
                # cur.execute("select student_id from std_enroll where student_id=%s AND course_id=%s  ", (student_id, course))
                # cur.execute("select section from student where section=%s ",(section))
                # Check if the query returns any rows
                if cur.fetchone():
                    # Insert the data into the attd table
                    cur.execute("INSERT INTO attd VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)", (n,student_id,lecture,course,section,d1,dtString, "Present"))
                    # Add the student ID to the recognized set
                    self.var_recognized_ids.add(student_id)
                    
                
                conn.commit()

                conn.close()


    def face_recog(self):
        course=self.var_course.get()
        with open(f"./att_reco/{course}.csv",'w') as file:
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
                student_id=id

                cursor.execute("select section from student where student_id="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select year from student where student_id="+str(id))
                i=cursor.fetchone()
                i="+".join(i)


                if confidence >80 :
                    cv2.putText(img,f"year:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"section:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,n,r,course,student_id)
                    self.move_att(student_id)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


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
     

    def move_attd(self):
        now = datetime.datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        status="absent"
        conn = mysql.connector.connect(
            host="localhost", user="root", password="maty", database="smart_attendance"
        )
        cur = conn.cursor()
        # in this code i want to copy student data to attendance only one section at time 
        # cur.execute("INSERT INTO attendance (std_ida, std_name, status) SELECT student_id, name,  'absent' FROM student where section= "+str(self.var_section.get())+" ")   
        sql = "INSERT INTO attendance (std_ida, std_name,section ) SELECT student_id, name, section  FROM student where section= %s"
        cur.execute(sql, (self.var_section.get(),))
      
        cur.execute(
        "UPDATE attendance SET lec_email=%s, course_ida=%s, date=%s, time=%s WHERE status=%s and CAST(date AS DATE) and course_ida=%s",
        (
            self.var_lecture.get(),
            self.var_course.get(),
            date,
            time,
            status,
            date,
            self.var_course.get()
         )
       )
      
        conn.commit()
        conn.close()



    def move_att(self, student_id):
        now = datetime.datetime.now()
         
        date = now.strftime("%d/%m/%Y")
        status="present"
        time = now.strftime("%H:%M:%S")
        conn = mysql.connector.connect(host="localhost", user="root", password="maty", database="smart_attendance")
        cur = conn.cursor()
        
        cur.execute(
            "UPDATE attendance SET time=%s, status=%s WHERE std_ida=%s AND date="+str(date)+"",
            (
                time,
                status,
                student_id
            )
        )
        conn.commit()
        conn.close()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()