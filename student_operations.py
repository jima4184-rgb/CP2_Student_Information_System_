from student_data import *
from utils import is_valid_name


def get_valid_name(prompt):
    """Validate first and last names"""
    while True:
        name = input(prompt).strip()

        if not name:
            print("This field cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Name must contain letters only.")
        else:
            return name.title()


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

    print(
        f"{'ID':<12} "
        f"{'First Name':<15} "
        f"{'Last Name':<15} "
        f"{'Course':<10} "
        f"{'Yr':>3}"
    )

    print("-" * 58)

    records = list(
        zip(
            student_ids,
            student_first_names,
            student_last_names,
            student_courses,
            student_year_levels
        )
    )

    records.sort()

    for sid, fname, lname, course, year in records:
        print(
            f"{sid:<12} "
            f"{fname:<15} "
            f"{lname:<15} "
            f"{course:<10} "
            f"{year:>3}"
        )

    print("-" * 58)
    print(f"Total Students: {len(student_ids)}")



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

        print(
            f"Student Found: "
            f"{student_first_names[i]} "
            f"{student_last_names[i]} "
        )

        confirm = input("Are you sure? (Y/N): ").upper()

        if confirm == "Y":
            student_ids.pop(i)
            student_first_names.pop(i)
            student_last_names.pop(i)
            student_courses.pop(i)
            student_year_levels.pop(i)

            save_students()

            print("Student deleted successfully.")
        else:
            print("Delete cancelled.")
    else:
        print("Student not found.")


def update_student():
    sid = input("Enter Student ID to update: ").strip()

    if sid not in student_ids:
        print("Student not found.")
        return

        i = student_ids.index(sid)

        print(
        f"Current Name      : "
        f"{student_first_names[i]} "
        f"{student_last_names[i]}"
    )
    print(f"Current Course    : {student_courses[i]}")
    print(f"Current Year Level: {student_year_levels[i]}")

    new_first = input(
        f"Enter New First Name [{student_first_names[i]}]: "
    ).strip()

    if new_first:
        student_first_names[i] = new_first.title()

    new_last = input(
        f"Enter New Last Name [{student_last_names[i]}]: "
).strip()

    if new_last:
        student_last_names[i] = new_last.title()

    new_course = input(
        f"Enter New Course [{student_courses[i]}]: "
    ).strip()

    if new_course:
        student_courses[i] = new_course.upper()

    while True:
        new_year = input(
            f"Enter New Year Level [{student_year_levels[i]}]: "
        ).strip()

        if not new_year:
            break

        try:
            new_year = int(new_year)

            if 1 <= new_year <= 5:
                student_year_levels[i] = new_year
                break
            else:
                print("Year level must be between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")


        save_students()
        print("Student updated successfully!")
    else:
        print("Student not found.")