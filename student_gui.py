import tkinter as tk
from tkinter import messagebox
from data_handler import load_json, save_json

def student_gui():
    student_window = tk.Tk()
    student_window.title("Student Course Selection")

    students = load_json('data/students.json')
    courses = load_json('data/courses.json')
    student_preferences = load_json('data/student_preferences.json')

    def submit_preferences(student_id, selected_courses):
        for course_id in selected_courses:
            student_preferences.append({
                "student_id": student_id,
                "course_id": int(course_id)
            })
        save_json(student_preferences, 'data/student_preferences.json')
        messagebox.showinfo("Success", "Your preferences have been saved!")

    def on_submit():
        student_name = student_name_entry.get()
        selected_courses = list(course_listbox.curselection())
        if not student_name or not selected_courses:
            messagebox.showerror("Error", "Please select a student and courses.")
            return

        student_id = next((s['student_id'] for s in students if s['student_name'] == student_name), None)
        if not student_id:
            messagebox.showerror("Error", "Student not found.")
            return

        submit_preferences(student_id, selected_courses)
        student_window.destroy()

    tk.Label(student_window, text="Select Student:").pack(pady=10)
    student_name_entry = tk.Entry(student_window)
    student_name_entry.pack(pady=5)

    tk.Label(student_window, text="Select Courses:").pack(pady=10)
    course_listbox = tk.Listbox(student_window, selectmode=tk.MULTIPLE)
    for course in courses:
        course_listbox.insert(tk.END, course['course_name'])
    course_listbox.pack(pady=5)

    submit_button = tk.Button(student_window, text="Submit", command=on_submit)
    submit_button.pack(pady=20)

    student_window.mainloop()
