
# Import tkinter and mysql.connector modules
import tkinter as tk
import mysql.connector

# Create a class for the application
class App(tk.Tk):
    def __init__(self):
        # Initialize the parent class
        super().__init__()

        # Create a frame for the widgets
        add_course_frame = tk.Frame(self)
        add_course_frame.pack()

        # Create a label for the courses
        course_label = tk.Label(add_course_frame, text="Select Courses:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        course_label.grid(row=0,column=2,padx=5,sticky=tk.W)

        # Create a listbox for the courses
        self.course_listbox = tk.Listbox(add_course_frame, selectmode=tk.MULTIPLE,font=("verdana",12,"bold"),width=14,height=15)
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

        # Create a button to add enrollment
        enroll_button = tk.Button(add_course_frame, text="Enroll", command=self.add_enrollment)
        enroll_button.grid(row=1,column=3,padx=5,pady=5)

    def add_enrollment(self):
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
        student_id = int(self.var_std_id.get())

        # Insert a new enrollment record for each selected course
        for course_name in selected_courses:
            # Get the course ID from the database using the course name
            cursor.execute("SELECT lecture_id FROM course WHERE name=%s", (course_name,))
            course_id = cursor.fetchone()[0]

            # Insert the enrollment record into the database using the student ID and course ID
            sql = "INSERT INTO std_enroll (lecture_id, course_idd) VALUES (%s, %s)"
            values = (student_id, course_id)
            cursor.execute(sql, values)
            db.commit()

        # Show a success message
        tk.messagebox.showinfo("Success", "Enrollment added successfully.")

# Create an instance of the application and run it
app = App()
app.mainloop()
