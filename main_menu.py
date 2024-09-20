import tkinter as tk
from tkinter import messagebox
from student_gui import student_gui
from teacher_gui import teacher_gui
from schedule_generator import generate_schedule
from display_gui import display_schedule
from data_handler import load_json, save_json

# Admin name (for simplicity, we hardcode this)
ADMIN_NAME = "Admin123"

def main_menu():
    root = tk.Tk()
    root.title("Course Scheduling System - Login")

    def login():
        name = name_entry.get()

        students = load_json('data/students.json')
        teachers = load_json('data/teachers.json')

        if name == ADMIN_NAME:
            messagebox.showinfo("Login Success", "Welcome, Admin")
            root.destroy()
            open_admin_menu()
        else:
            student = next((s for s in students if s['student_name'] == name), None)
            teacher = next((t for t in teachers if t['teacher_name'] == name), None)

            if student:
                messagebox.showinfo("Login Success", f"Welcome, {student['student_name']} (Student)")
                root.destroy()
                open_student_menu()
            elif teacher:
                messagebox.showinfo("Login Success", f"Welcome, {teacher['teacher_name']} (Teacher)")
                root.destroy()
                open_teacher_menu()
            else:
                messagebox.showerror("Login Error", "Name not found. Please try again.")

    tk.Label(root, text="Enter Your Name to Login", font=('Arial', 16)).pack(pady=20)
    tk.Label(root, text="Name:").pack(pady=5)
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=10)
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=20)

    root.mainloop()

def open_student_menu():
    root = tk.Tk()
    root.title("Course Scheduling System - Student")
    tk.Label(root, text="Welcome, Student!", font=('Arial', 16)).pack(pady=20)

    student_button = tk.Button(root, text="Student Course Selection", command=student_gui)
    student_button.pack(pady=10)

    display_button = tk.Button(root, text="Display Schedule", command=display_schedule)
    display_button.pack(pady=10)

    root.mainloop()

def open_teacher_menu():
    root = tk.Tk()
    root.title("Course Scheduling System - Teacher")
    tk.Label(root, text="Welcome, Teacher!", font=('Arial', 16)).pack(pady=20)

    teacher_button = tk.Button(root, text="Teacher Course Selection", command=teacher_gui)
    teacher_button.pack(pady=10)

    display_button = tk.Button(root, text="Display Schedule", command=display_schedule)
    display_button.pack(pady=10)

    root.mainloop()

# Admin menu with added options to add and delete students, teachers, and courses
def open_admin_menu():
    root = tk.Tk()
    root.title("Course Scheduling System - Admin")

    tk.Label(root, text="Welcome, Admin!", font=('Arial', 16)).pack(pady=20)

    generate_button = tk.Button(root, text="Generate Schedule", command=generate_schedule)
    generate_button.pack(pady=10)

    display_button = tk.Button(root, text="Display Schedule", command=display_schedule)
    display_button.pack(pady=10)

    add_student_button = tk.Button(root, text="Add Student", command=add_student)
    add_student_button.pack(pady=10)

    add_teacher_button = tk.Button(root, text="Add Teacher", command=add_teacher)
    add_teacher_button.pack(pady=10)

    add_course_button = tk.Button(root, text="Add Course", command=add_course)
    add_course_button.pack(pady=10)

    delete_student_button = tk.Button(root, text="Delete Student", command=delete_student)
    delete_student_button.pack(pady=10)

    delete_teacher_button = tk.Button(root, text="Delete Teacher", command=delete_teacher)
    delete_teacher_button.pack(pady=10)

    delete_course_button = tk.Button(root, text="Delete Course", command=delete_course)
    delete_course_button.pack(pady=10)

    root.mainloop()

# Functions to add new students, teachers, and courses
def add_student():
    add_window = tk.Tk()
    add_window.title("Add Student")
    tk.Label(add_window, text="Enter Student ID:").pack(pady=5)
    student_id_entry = tk.Entry(add_window)
    student_id_entry.pack(pady=5)
    tk.Label(add_window, text="Enter Student Name:").pack(pady=5)
    student_name_entry = tk.Entry(add_window)
    student_name_entry.pack(pady=5)

    def save_student():
        student_id = int(student_id_entry.get())
        student_name = student_name_entry.get()
        students = load_json('data/students.json')
        new_student = {"student_id": student_id, "student_name": student_name}
        students.append(new_student)
        save_json(students, 'data/students.json')
        messagebox.showinfo("Success", f"Student {student_name} added successfully.")
        add_window.destroy()

    save_button = tk.Button(add_window, text="Save", command=save_student)
    save_button.pack(pady=10)
    add_window.mainloop()

def add_teacher():
    add_window = tk.Tk()
    add_window.title("Add Teacher")
    tk.Label(add_window, text="Enter Teacher ID:").pack(pady=5)
    teacher_id_entry = tk.Entry(add_window)
    teacher_id_entry.pack(pady=5)
    tk.Label(add_window, text="Enter Teacher Name:").pack(pady=5)
    teacher_name_entry = tk.Entry(add_window)
    teacher_name_entry.pack(pady=5)

    def save_teacher():
        teacher_id = int(teacher_id_entry.get())
        teacher_name = teacher_name_entry.get()
        teachers = load_json('data/teachers.json')
        new_teacher = {"teacher_id": teacher_id, "teacher_name": teacher_name}
        teachers.append(new_teacher)
        save_json(teachers, 'data/teachers.json')
        messagebox.showinfo("Success", f"Teacher {teacher_name} added successfully.")
        add_window.destroy()

    save_button = tk.Button(add_window, text="Save", command=save_teacher)
    save_button.pack(pady=10)
    add_window.mainloop()

def add_course():
    add_window = tk.Tk()
    add_window.title("Add Course")
    tk.Label(add_window, text="Enter Course ID:").pack(pady=5)
    course_id_entry = tk.Entry(add_window)
    course_id_entry.pack(pady=5)
    tk.Label(add_window, text="Enter Course Name:").pack(pady=5)
    course_name_entry = tk.Entry(add_window)
    course_name_entry.pack(pady=5)

    def save_course():
        course_id = int(course_id_entry.get())
        course_name = course_name_entry.get()
        courses = load_json('data/courses.json')
        new_course = {"course_id": course_id, "course_name": course_name}
        courses.append(new_course)
        save_json(courses, 'data/courses.json')
        messagebox.showinfo("Success", f"Course {course_name} added successfully.")
        add_window.destroy()

    save_button = tk.Button(add_window, text="Save", command=save_course)
    save_button.pack(pady=10)
    add_window.mainloop()

# Functions to delete students, teachers, and courses
def delete_student():
    delete_window = tk.Tk()
    delete_window.title("Delete Student")
    tk.Label(delete_window, text="Enter Student ID to Delete:").pack(pady=5)
    student_id_entry = tk.Entry(delete_window)
    student_id_entry.pack(pady=5)

    def confirm_delete():
        student_id = int(student_id_entry.get())
        students = load_json('data/students.json')
        students = [s for s in students if s['student_id'] != student_id]
        save_json(students, 'data/students.json')
        messagebox.showinfo("Success", f"Student ID {student_id} deleted successfully.")
        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete", command=confirm_delete)
    delete_button.pack(pady=10)
    delete_window.mainloop()

def delete_teacher():
    delete_window = tk.Tk()
    delete_window.title("Delete Teacher")
    tk.Label(delete_window, text="Enter Teacher ID to Delete:").pack(pady=5)
    teacher_id_entry = tk.Entry(delete_window)
    teacher_id_entry.pack(pady=5)

    def confirm_delete():
        teacher_id = int(teacher_id_entry.get())
        teachers = load_json('data/teachers.json')
        teachers = [t for t in teachers if t['teacher_id'] != teacher_id]
        save_json(teachers, 'data/teachers.json')
        messagebox.showinfo("Success", f"Teacher ID {teacher_id} deleted successfully.")
        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete", command=confirm_delete)
    delete_button.pack(pady=10)
    delete_window.mainloop()

def delete_course():
    delete_window = tk.Tk()
    delete_window.title("Delete Course")
    tk.Label(delete_window, text="Enter Course ID to Delete:").pack(pady=5)
    course_id_entry = tk.Entry(delete_window)
    course_id_entry.pack(pady=5)

    def confirm_delete():
        course_id = int(course_id_entry.get())
        courses = load_json('data/courses.json')
        courses = [c for c in courses if c['course_id'] != course_id]
        save_json(courses, 'data/courses.json')
        messagebox.showinfo("Success", f"Course ID {course_id} deleted successfully.")
        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete", command=confirm_delete)
    delete_button.pack(pady=10)
    delete_window.mainloop()
