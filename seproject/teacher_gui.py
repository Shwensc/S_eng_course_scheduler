import tkinter as tk
from tkinter import messagebox
from data_handler import load_json, save_json

def teacher_gui():
    teacher_window = tk.Tk()
    teacher_window.title("Teacher Course Selection")

    teachers = load_json('data/teachers.json')
    courses = load_json('data/courses.json')
    teacher_preferences = load_json('data/teacher_preferences.json')

    def submit_preferences(teacher_id, selected_courses):
        for course_id in selected_courses:
            teacher_preferences.append({
                "teacher_id": teacher_id,
                "course_id": int(course_id)
            })
        save_json(teacher_preferences, 'data/teacher_preferences.json')
        messagebox.showinfo("Success", "Your preferences have been saved!")

    def on_submit():
        teacher_name = teacher_name_entry.get()
        selected_courses = list(course_listbox.curselection())
        if not teacher_name or not selected_courses:
            messagebox.showerror("Error", "Please select a teacher and courses.")
            return

        teacher_id = next((t['teacher_id'] for t in teachers if t['teacher_name'] == teacher_name), None)
        if not teacher_id:
            messagebox.showerror("Error", "Teacher not found.")
            return

        submit_preferences(teacher_id, selected_courses)
        teacher_window.destroy()

    tk.Label(teacher_window, text="Select Teacher:").pack(pady=10)
    teacher_name_entry = tk.Entry(teacher_window)
    teacher_name_entry.pack(pady=5)

    tk.Label(teacher_window, text="Select Courses:").pack(pady=10)
    course_listbox = tk.Listbox(teacher_window, selectmode=tk.MULTIPLE)
    for course in courses:
        course_listbox.insert(tk.END, course['course_name'])
    course_listbox.pack(pady=5)

    submit_button = tk.Button(teacher_window, text="Submit", command=on_submit)
    submit_button.pack(pady=20)

    teacher_window.mainloop()
