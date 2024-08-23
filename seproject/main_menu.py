import tkinter as tk
from student_gui import student_gui
from teacher_gui import teacher_gui
from schedule_generator import generate_schedule
from display_gui import display_schedule

def main_menu():
    root = tk.Tk()
    root.title("Course Scheduling System")

    tk.Label(root, text="Course Scheduling System", font=('Arial', 16)).pack(pady=20)

    student_button = tk.Button(root, text="Student Course Selection", command=student_gui)
    student_button.pack(pady=10)

    teacher_button = tk.Button(root, text="Teacher Course Selection", command=teacher_gui)
    teacher_button.pack(pady=10)

    generate_button = tk.Button(root, text="Generate Schedule", command=generate_schedule)
    generate_button.pack(pady=10)

    display_button = tk.Button(root, text="Display Schedule", command=display_schedule)
    display_button.pack(pady=10)

    root.mainloop()
