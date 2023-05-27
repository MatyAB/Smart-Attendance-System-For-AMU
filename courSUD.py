
from tkinter import*
import tkinter as tk
import mysql.connector
from tkinter import ttk
# Create a Tkinter GUI window
window = tk.Tk()

# Create form fields using Tkinter widgets
name_label = tk.Label(window, text="Name")
name_entry = tk.Entry(window)
course_id_label = tk.Label(window, text="Course ID")
course_id_combo = tk.ttk.Combobox(window)

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="maty",
  database="smart_attendance"
)

# Populate the combo box with course IDs from the course table
mycursor = mydb.cursor()
mycursor.execute("SELECT course_id FROM course")
course_ids = mycursor.fetchall()
course_id_combo['values'] = course_ids

# Create a function to insert values into the student table
def insert_student():
    # Retrieve the values from the form fields
    name = name_entry.get()
    course_id = course_id_combo.get()
    
    # Insert the values into the student table using SQL INSERT statement
    mycursor = mydb.cursor()
    sql = "INSERT INTO student (student_id, course) VALUES (%s, %s)"
    val = (name, course_id)
    mycursor.execute(sql, val)
    mydb.commit()

# Create a button to submit the form and insert values into the student table
submit_button = tk.Button(window, text="Submit", command=insert_student)

# Display the form fields and button in the window
name_label.pack()
name_entry.pack()
course_id_label.pack()
course_id_combo.pack()
submit_button.pack()

# Run the Tkinter event loop
window.mainloop()


