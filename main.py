from student_data import load_students
from student_operations import (
    add_student,
    view_students,
    search_student,
    delete_student,
    update_student
)


def show_menu():
    print("\n================================")
    print("   STUDENT INFORMATION SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("0. Exit")
    print("================================")


def main():
    load_students()

    while True:
        show_menu()

        choice = input("Enter a number: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()