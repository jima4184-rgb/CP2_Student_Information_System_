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
