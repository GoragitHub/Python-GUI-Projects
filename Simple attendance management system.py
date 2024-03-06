import tkinter as tk
from tkinter import ttk
from datetime import datetime
import csv
from tkinter.messagebox import *

# Simulated user database (For production use, implement secure storage and password hashing)
users = {
    "user1": "password1",
    "user2": "password2"
}

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        tk.Label(root, text="User ID:").grid(row=0, column=0)
        self.user_id_entry = tk.Entry(root)
        self.user_id_entry.grid(row=0, column=1)

        tk.Label(root, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(root, text="Login", command=self.login_user)
        self.login_button.grid(row=2,column=1)

    def login_user(self):
        user_id = self.user_id_entry.get()
        password = self.password_entry.get()
        
        if users.get(user_id) == password:
            showinfo("Login Success", f"Welcome {user_id}")
            # Close the login window and open the main app window
            root.destroy()
            new_root = tk.Tk()
            app = AttendanceSystem(new_root, user_id)
            new_root.mainloop()
            
        else:
            showerror("Login Failed", "Invalid User ID or Password")

class AttendanceSystem:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Employee Attendance Management System")
        self.logged_in_user_id = user_id
        self.marked_leave = False

        # Initialize marked_names as an empty set
        self.marked_names = set()

        # Display a welcome message or user ID label if desired
        tk.Label(root, text=f"Welcome {user_id}").grid(row=0, columnspan=2)

        # Treeview for attendance records
        self.tree = ttk.Treeview(root, columns=("User ID", "Status", "Time"), show="headings")
        self.tree.heading("User ID", text="User ID")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Time", text="Time")
        self.tree.grid(row=1, columnspan=2)

        # Buttons for marking attendance and leave
        self.mark_button = tk.Button(root, text="Mark Attendance", command=self.mark_attendance)
        self.mark_button.grid(row=2,column=0)

        self.leave_button = tk.Button(root, text="Mark Leave", command=self.mark_leave)
        self.leave_button.grid(row=2,column=1)

    def mark_attendance(self):
        if not self.marked_leave:  # Only allow marking attendance if leave is not already marked
            status = "Present"
            name = self.logged_in_user_id  
            if name not in self.marked_names:
                self.update_attendance(name, status)
                showinfo("Success", "Attendance marked successfully.")
    
    def mark_leave(self):
        if not self.marked_leave:  # Only allow marking leave once
            status = "Left"
            name = self.logged_in_user_id  
            if name in self.marked_names:
                self.update_attendance(name, status)
                showinfo("Success", "Leave marked successfully.")
                self.marked_leave = True  # Set marked_leave to True after marking leave

    def update_attendance(self, user_id, status):
       time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

       with open('attendance_records.csv', mode='a', newline='') as file:
           writer = csv.writer(file)
           writer.writerow([user_id,status,time])

       # Update UI Treeview with new attendance record.
       values_to_insert = (user_id,status,time)
       if status == "Present":
           iid_value='present'+user_id  # Unique identifier for present record.
           if not (self.tree.exists(iid_value)):
               # Insert only if not already present to prevent duplicates.
               self.tree.insert("", index='end', iid=iid_value ,values=values_to_insert)
               # Add user to marked names set.
               self.marked_names.add(user_id)
       elif status == "Left":
           iid_value='left'+user_id  # Unique identifier for left record.
           if not (self.tree.exists(iid_value)):
               # Insert only if not already left to prevent duplicates.
               # This assumes a person can't leave more than once per day/session.
               present_iid='present'+user_id 
               if (self.tree.exists(present_iid)):
                #    self.tree.delete(present_iid) 
                pass
               self.tree.insert("", index='end', iid=iid_value ,values=values_to_insert)

if __name__ == "__main__":
    root = tk.Tk()
    login_app = LoginWindow(root)
    root.mainloop()