import tkinter as tk
from tkinter import messagebox
import json

try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()

    if name == "" or roll == "":
        messagebox.showerror("Error", "Enter all details")
        return

    student = {"name": name, "roll": roll}
    students.append(student)
    save_data()

    messagebox.showinfo("Success", "Student Added")

def view_students():
    text.delete("1.0", tk.END)

    for s in students:
        text.insert(tk.END, f"Name: {s['name']} Roll: {s['roll']}\n")

window = tk.Tk()
window.title("Student Management System")
window.geometry("400x400")

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Roll Number").pack()
roll_entry = tk.Entry(window)
roll_entry.pack()

tk.Button(window, text="Add Student", command=add_student).pack()
tk.Button(window, text="View Students", command=view_students).pack()

text = tk.Text(window)
text.pack()

window.mainloop()