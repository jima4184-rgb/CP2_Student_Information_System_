from student_data import *
from utils import is_valid_name


def add_student():
    print("\n-- Add Student --")
    sid = input("Enter Student ID: ").strip()

    if sid in student_ids:
        print("ID already exists!")
        return

    while True:
        first_name = input("Enter First Name: ").strip()
        if is_valid_name(first_name):
            break
        print("Invalid input. First name cannot contain numbers.")

    while True:
        last_name = input("Enter Last Name: ").strip()
        if is_valid_name(last_name):
            break
        print("Invalid input. Last name cannot contain numbers.")

    while True:
        course = input("Enter Course: ").strip()
        if is_valid_name(course):
            break
        print("Invalid input. Course cannot contain numbers.")

    while True:
        try:
            year_level = int(input("Enter Year Level (1-5): "))
            if 1 <= year_level <= 5:
                break
            print("Year level must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    student_ids.append(sid)
    student_first_names.append(first_name)
    student_last_names.append(last_name)
    student_courses.append(course)
    student_year_levels.append(year_level)

    save_students()
    print("Student added successfully!")


def view_students():
    print("\n-- All Students --")

    if not student_ids:
        print("No students found.")
        return

    print(f"{'ID':<12} {'First Name':<15} {'Last Name':<15} {'Course':<10} {'Yr':>3}")
    print("-" * 58)

    for i in range(len(student_ids)):
        print(
            f"{student_ids[i]:<12} "
            f"{student_first_names[i]:<15} "
            f"{student_last_names[i]:<15} "
            f"{student_courses[i]:<10} "
            f"{student_year_levels[i]:>3}"
        )


def search_student():
    sid = input("Enter Student ID: ").strip()

    if sid in student_ids:
        i = student_ids.index(sid)

        print(f"ID        : {student_ids[i]}")
        print(f"Name      : {student_first_names[i]} {student_last_names[i]}")
        print(f"Course    : {student_courses[i]}")
        print(f"Year Level: {student_year_levels[i]}")
    else:
        print("Student not found.")


def delete_student():
    sid = input("Enter Student ID to delete: ").strip()

    if sid in student_ids:
        i = student_ids.index(sid)

        student_ids.pop(i)
        student_first_names.pop(i)
        student_last_names.pop(i)
        student_courses.pop(i)
        student_year_levels.pop(i)

        save_students()
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def update_student():
    sid = input("Enter Student ID to update: ").strip()

    if sid in student_ids:
        i = student_ids.index(sid)

        student_first_names[i] = input("Enter New First Name: ")
        student_last_names[i] = input("Enter New Last Name: ")
        student_courses[i] = input("Enter New Course: ")

        while True:
            try:
                year = int(input("Enter New Year Level (1-5): "))
                if 1 <= year <= 5:
                    student_year_levels[i] = year
                    break
            except ValueError:
                print("Invalid input.")

        save_students()
        print("Student updated successfully!")
    else:
        print("Student not found.")