import mysql.connector
from tkinter import messagebox
import csv

# df =pandas.read_csv("log.csv")
# csv_data=csv.reader(open('log.csv'))            
# print(df)
try:
    conn = mysql.connector.connect(username="root", password="maty",host="localhost",database="smart_attendance",port=3306)
    mycursor = conn.cursor()
    csv_data=csv.reader(open('log.csv'))
    for row in csv_data:
      mycursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s)", row)
    messagebox.showinfo("Delete","Successfully Deleted!")

except Exception as es:
    messagebox.showerror("Error",f"Due to: {str(es)}")

conn.commit()
conn.close()
