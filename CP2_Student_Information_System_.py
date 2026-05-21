import os

FILE_NAME = "students.txt"

student_ids = []
student_first_names = []
student_last_names = []
student_courses = []
student_year_levels = []

def load_students():
    """Load student records from the file when the program starts."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 5:
                    student_ids.append(data[0])
                    student_first_names.append(data[1])
                    student_last_names.append(data[2])
                    student_courses.append(data[3])
                    student_year_levels.append(int(data[4]))
                    student_year_levels.append(int(data[4]))


def save_students():
    """Save all student records to the file."""
    with open(FILE_NAME, "w") as file:
        for i in range(len(student_ids)):
            file.write(
                f"{student_ids[i]}|"
                f"{student_first_names[i]}|"
                f"{student_last_names[i]}|"
                f"{student_courses[i]}|"
                f"{student_year_levels[i]}\n"
            )

def add_student():
    print("\n-- Add Student --")
    sid = input("Enter Student ID: ").strip()

    if sid in student_ids:
        print("ID already exists!")
        return

    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    course = input("Enter Course: ").strip()

    while True:
        try:
            year_level = int(input("Enter Year Level (1-5): "))
            if 1 <= year_level <= 5:
                break
            else:
                print("Year level must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    student_ids.append(sid)
    student_first_names.append(first_name)
    student_last_names.append(last_name)
    student_courses.append(course)
    student_year_levels.append(year_level)

    save_students()
    print(f"Student '{first_name} {last_name}' added successfully!")

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
    print("\n-- Search Student --")
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
    print("\n-- Delete Student --")
    sid = input("Enter Student ID to delete: ").strip()

    if sid in student_ids:
        i = student_ids.index(sid)

        print(f"Deleted: {student_first_names[i]} {student_last_names[i]}")

        student_ids.pop(i)
        student_first_names.pop(i)
        student_last_names.pop(i)
        student_courses.pop(i)
        student_year_levels.pop(i)

        save_students()
    else:
        print("Student not found.")
