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
