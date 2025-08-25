import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9985"
)

# Create a cursor object
cursor = conn.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS employee_data")

# Switch to the created database
cursor.execute("USE employee_data")

# Create table employee_performance
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee_performance (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        tasks_completed INT,
        scheduled_hours INT,
        attended_hours INT,
        tasks_completed_on_time INT
    )
""")

data = [
    ("John", 50, 160, 150, 45),
    ("Alice", 45, 160, 155, 40),
    ("Bob", 55, 160, 150, 50)
]

cursor.executemany("""
    INSERT INTO employee_performance (name, tasks_completed, scheduled_hours, attended_hours, tasks_completed_on_time)
    VALUES (%s, %s, %s, %s, %s)
""", data)

# Commit changes
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()

print("Database and table created successfully!")

import tkinter as tk
from tkinter import messagebox
import mysql.connector

def fetch_employee_data(employee_name):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee_performance WHERE LOWER(name) = %s", (employee_name.lower(),))
    return cursor.fetchone()

def calculate_rating(employee):
    scheduled_hours = employee["scheduled_hours"]
    attended_hours = employee["attended_hours"]
    tasks_completed = employee["tasks_completed"]
    tasks_completed_on_time = employee["tasks_completed_on_time"]

    # Calculate completion rate
    completion_rate = tasks_completed / scheduled_hours

    # Calculate adherence to deadlines rate
    adherence_rate = tasks_completed_on_time / tasks_completed

    # Calculate attendance rate
    attendance_rate = attended_hours / scheduled_hours

    # Calculate rating based on completion rate, adherence rate, and attendance rate
    rating = (completion_rate + adherence_rate + attendance_rate) / 3 * 10

    # Limit rating to a maximum of 10
    rating = min(rating, 10)

    return rating

def display_employee_performance():
    employee_name = employee_name_entry.get().strip()
    if not employee_name:
        messagebox.showerror("Error", "Please enter an employee name.")
        return

    employee = fetch_employee_data(employee_name)
    if not employee:
        messagebox.showerror("Error", f"No data found for employee '{employee_name}'.")
        return

    rating = calculate_rating(employee)

    # Clear previous performance details
    for widget in performance_frame.winfo_children():
        widget.destroy()

    # Display performance details
    tk.Label(performance_frame, text=f"Hello, {employee['name']}").pack()
    tk.Label(performance_frame, text=f"Scheduled Hours: {employee['scheduled_hours']}").pack()
    tk.Label(performance_frame, text=f"Worked Hours: {employee['attended_hours']}").pack()
    tk.Label(performance_frame, text=f"Tasks Completed: {employee['tasks_completed']}").pack()
    tk.Label(performance_frame, text=f"Tasks Completed on Time: {employee['tasks_completed_on_time']}").pack()

    rating_label.config(text=f"Rating: {rating:.2f} ★", font=("Arial", 14, "bold"))

def main():
    root = tk.Tk()
    root.title("Employee Performance")

    global employee_name_entry
    tk.Label(root, text="Enter Employee Name:").pack()
    employee_name_entry = tk.Entry(root)
    employee_name_entry.pack()

    display_button = tk.Button(root, text="Display Performance", command=display_employee_performance)
    display_button.pack()

    global performance_frame
    performance_frame = tk.Frame(root)
    performance_frame.pack()

    global rating_label
    rating_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
    rating_label.pack()

    root.mainloop()

if __name__ == "__main__":
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='9985',
                                         database='employee_data')
    main()
    connection.close()
