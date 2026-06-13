import tkinter as tk
from tkinter import ttk, messagebox

from student_data import (
    student_ids,
    student_first_names,
    student_last_names,
    student_courses,
    student_year_levels,
    save_students,
)
from utils import is_valid_name

MAROON = "#800000"
GOLD = "#FFD700"


def open_add_student(root):
    win = tk.Toplevel(root)
    win.title("Add Student")
    win.geometry("450x500")
    win.configure(bg="white")

    frame = tk.Frame(win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="ADD STUDENT",
        font=("Arial", 24, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=10)

    def labeled_entry(text):
        tk.Label(frame, text=text, bg="white", font=("Arial", 12)).pack()
        entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
        entry.pack(pady=5)
        return entry

    id_entry = labeled_entry("STUDENT ID")
    first_entry = labeled_entry("FIRST NAME")
    last_entry = labeled_entry("LAST NAME")
    course_entry = labeled_entry("COURSE")
    year_entry = labeled_entry("YEAR LEVEL (1-5)")

def save():
        sid = id_entry.get().strip()
        first_name = first_entry.get().strip()
        last_name = last_entry.get().strip()
        course = course_entry.get().strip()
        year = year_entry.get().strip()

        if not sid or not first_name or not last_name or not course or not year:
            messagebox.showerror("Error", "All fields are required.")
            return

        if sid in student_ids:
            messagebox.showerror("Error", "ID already exists!")
            return

        if not is_valid_name(first_name):
            messagebox.showerror("Error", "First name cannot contain numbers.")
            return

        if not is_valid_name(last_name):
            messagebox.showerror("Error", "Last name cannot contain numbers.")
            return

        if not is_valid_name(course):
            messagebox.showerror("Error", "Course cannot contain numbers.")
            return

        try:
            year_level = int(year)
            if not (1 <= year_level <= 5):
                messagebox.showerror("Error", "Year level must be between 1 and 5.")
                return
        except ValueError:
            messagebox.showerror("Error", "Year level must be a number.")
            return

        if not messagebox.askyesno("Confirm", "Save this student?"):
            return

        student_ids.append(sid)
        student_first_names.append(first_name.title())
        student_last_names.append(last_name.title())
        student_courses.append(course.upper())
        student_year_levels.append(year_level)

        save_students()

        messagebox.showinfo("Success", "Student added successfully!")
        win.destroy()

    tk.Button(
        frame,
        text="SAVE",
        font=("Arial", 14, "bold"),
        width=18,
        bg=MAROON,
        fg="white",
        command=save,
    ).pack(pady=20)


def open_view_students(root):
    win = tk.Toplevel(root)
    win.title("View Students")
    win.geometry("800x500")
    win.configure(bg="white")

    tk.Label(
        win,
        text="ALL STUDENTS",
        font=("Arial", 18, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=10)

    columns = ("ID", "First Name", "Last Name", "Course", "Year Level")

    tree = ttk.Treeview(win, columns=columns, show="headings")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    def refresh():
        tree.delete(*tree.get_children())

        records = list(
            zip(
                student_ids,
                student_first_names,
                student_last_names,
                student_courses,
                student_year_levels,
            )
        )
        records.sort()

        for record in records:
            tree.insert("", "end", values=record)

    refresh()

    btn_frame = tk.Frame(win, bg="white")
    btn_frame.pack(pady=5)

    def on_double_click(event):
        selected = tree.focus()
        if selected:
            values = tree.item(selected, "values")
            open_edit_student(win, values, refresh)

    tree.bind("<Double-1>", on_double_click)

    total_label = tk.Label(
        win,
        text=f"Total Students: {len(student_ids)}",
        bg="white",
        font=("Arial", 12, "bold"),
    )
    total_label.pack(pady=5)

    def refresh_all():
        refresh()
        total_label.config(text=f"Total Students: {len(student_ids)}")

    tk.Button(
        btn_frame, text="Refresh", command=refresh_all, bg=MAROON, fg="white"
    ).pack(side="left", padx=5)

    tk.Label(
        win,
        text="Double-click a row to edit that student.",
        bg="white",
        font=("Arial", 10, "italic"),
    ).pack(pady=2)


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