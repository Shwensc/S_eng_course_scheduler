import tkinter as tk
from tkinter import ttk
from data_handler import load_json

def display_schedule():
    schedule_window = tk.Tk()
    schedule_window.title("Course Schedule")

    schedule = load_json('data/schedule.json')
    courses = load_json('data/courses.json')
    teachers = load_json('data/teachers.json')

    course_dict = {course['course_id']: course['course_name'] for course in courses}
    teacher_dict = {teacher['teacher_id']: teacher['teacher_name'] for teacher in teachers}

    tree = ttk.Treeview(schedule_window, columns=('Day', 'Time Slot', 'Course Name', 'Teacher', 'Room'), show='headings')
    tree.heading('Day', text='Day')
    tree.heading('Time Slot', text='Time Slot')
    tree.heading('Course Name', text='Course Name')
    tree.heading('Teacher', text='Teacher')
    tree.heading('Room', text='Room')

    tree.column('Day', width=100)
    tree.column('Time Slot', width=150)
    tree.column('Course Name', width=150)
    tree.column('Teacher', width=150)
    tree.column('Room', width=100)

    tree.pack(pady=20)

    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    sorted_schedule = sorted(schedule, key=lambda x: (days_order.index(x['day']), x['time_slot']))

    for entry in sorted_schedule:
        course_name = course_dict[entry['course_id']]
        teacher_name = teacher_dict[entry['teacher_id']]
        tree.insert('', 'end', values=(entry['day'], entry['time_slot'], course_name, teacher_name, entry['room']))

    schedule_window.mainloop()
