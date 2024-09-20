import random
from data_handler import load_json, save_json

def generate_schedule():
    courses = load_json('data/courses.json')
    students = load_json('data/students.json')
    student_preferences = load_json('data/student_preferences.json')
    teachers = load_json('data/teachers.json')
    teacher_preferences = load_json('data/teacher_preferences.json')
    
    schedule = []
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = ['08:45 - 10:15', '10:30 - 12:00', '13:30 - 15:00']
    rooms = ['Room 101', 'Room 102', 'Room 103', 'Room 104', 'Room 105']

    # Group students by course
    course_student_count = {}
    for preference in student_preferences:
        course_id = preference['course_id']
        course_student_count[course_id] = course_student_count.get(course_id, 0) + 1

    # Track assigned courses to avoid assigning the same teacher to multiple courses
    teacher_course_assignment = {}

    # Generate schedule for courses with at least 20 students
    for course_id, count in course_student_count.items():
        if count >= 20:
            # Find available teachers for the course
            available_teachers = [
                pref['teacher_id'] for pref in teacher_preferences if pref['course_id'] == course_id
                and pref['teacher_id'] not in teacher_course_assignment
            ]
            if available_teachers:
                teacher_id = random.choice(available_teachers)
                # Assign the course to the teacher
                teacher_course_assignment[teacher_id] = course_id
                assigned_days = random.sample(days, 3)
                for i, day in enumerate(assigned_days):
                    time_slot = time_slots[i]
                    room = random.choice(rooms)
                    schedule.append({
                        "course_id": course_id,
                        "teacher_id": teacher_id,
                        "day": day,
                        "time_slot": time_slot,
                        "room": room
                    })

    save_json(schedule, 'data/schedule.json')
