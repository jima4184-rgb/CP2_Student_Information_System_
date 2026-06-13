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


def open_edit_student(parent, selected_data, refresh_callback):
    sid, first_name, last_name, course, year = selected_data

    win = tk.Toplevel(parent)
    win.title("Edit Student")
    win.geometry("400x450")
    win.configure(bg="white")

    frame = tk.Frame(win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="EDIT STUDENT",
        font=("Arial", 20, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=10)

    tk.Label(frame, text=f"Student ID: {sid}", bg="white", font=("Arial", 12, "bold")).pack(pady=5)

    def labeled_entry(text, value):
        tk.Label(frame, text=text, bg="white").pack()
        entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
        entry.insert(0, value)
        entry.pack(pady=5)
        return entry

    first_entry = labeled_entry("FIRST NAME", first_name)
    last_entry = labeled_entry("LAST NAME", last_name)
    course_entry = labeled_entry("COURSE", course)
    year_entry = labeled_entry("YEAR LEVEL (1-5)", year)

    def save():
        new_first = first_entry.get().strip()
        new_last = last_entry.get().strip()
        new_course = course_entry.get().strip()
        new_year = year_entry.get().strip()

        if not new_first or not new_last or not new_course or not new_year:
            messagebox.showerror("Error", "All fields are required.")
            return

        if not is_valid_name(new_first):
            messagebox.showerror("Error", "First name cannot contain numbers.")
            return

        if not is_valid_name(new_last):
            messagebox.showerror("Error", "Last name cannot contain numbers.")
            return

        if not is_valid_name(new_course):
            messagebox.showerror("Error", "Course cannot contain numbers.")
            return

        try:
            year_level = int(new_year)
            if not (1 <= year_level <= 5):
                messagebox.showerror("Error", "Year level must be between 1 and 5.")
                return
        except ValueError:
            messagebox.showerror("Error", "Year level must be a number.")
            return

        if not messagebox.askyesno("Confirm", "Save changes to this student?"):
            return

        i = student_ids.index(sid)
        student_first_names[i] = new_first.title()
        student_last_names[i] = new_last.title()
        student_courses[i] = new_course.upper()
        student_year_levels[i] = year_level

        save_students()

        messagebox.showinfo("Success", "Student updated successfully!")
        win.destroy()
        refresh_callback()

    tk.Button(
        frame,
        text="SAVE CHANGES",
        font=("Arial", 14, "bold"),
        width=18,
        bg=MAROON,
        fg="white",
        command=save,
    ).pack(pady=20)


def open_search_student(root):
    win = tk.Toplevel(root)
    win.title("Search Student")
    win.geometry("500x400")
    win.configure(bg="white")

    frame = tk.Frame(win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="SEARCH STUDENT",
        font=("Arial", 22, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=10)

    tk.Label(frame, text="Enter Student ID", bg="white").pack()

    id_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    id_entry.pack(pady=10)

    result_box = tk.Text(frame, font=("Arial", 12), width=45, height=8)
    result_box.pack(pady=10)

    def do_search():
        sid = id_entry.get().strip()
        result_box.delete("1.0", "end")

        if sid in student_ids:
            i = student_ids.index(sid)
            result_box.insert("end", f"ID        : {student_ids[i]}\n")
            result_box.insert(
                "end",
                f"Name      : {student_first_names[i]} {student_last_names[i]}\n",
            )
            result_box.insert("end", f"Course    : {student_courses[i]}\n")
            result_box.insert("end", f"Year Level: {student_year_levels[i]}\n")
        else:
            result_box.insert("end", "Student not found.")

    tk.Button(
        frame,
        text="SEARCH",
        font=("Arial", 14, "bold"),
        bg=MAROON,
        fg="white",
        width=15,
        command=do_search,
    ).pack(pady=10)


def open_delete_student(root):
    win = tk.Toplevel(root)
    win.title("Delete Student")
    win.geometry("500x350")
    win.configure(bg="white")

    frame = tk.Frame(win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="DELETE STUDENT",
        font=("Arial", 22, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=10)

    tk.Label(frame, text="Enter Student ID", bg="white").pack()

    id_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    id_entry.pack(pady=10)

    info_label = tk.Label(frame, text="", bg="white", font=("Arial", 12))
    info_label.pack(pady=5)

    def do_delete():
        sid = id_entry.get().strip()

        if sid not in student_ids:
            messagebox.showerror("Error", "Student not found.")
            return

        i = student_ids.index(sid)
        name = f"{student_first_names[i]} {student_last_names[i]}"

        if not messagebox.askyesno(
            "Confirm Delete", f"Delete student {name} (ID: {sid})?"
        ):
            return

        student_ids.pop(i)
        student_first_names.pop(i)
        student_last_names.pop(i)
        student_courses.pop(i)
        student_year_levels.pop(i)

        save_students()

        messagebox.showinfo("Success", "Student deleted successfully.")
        id_entry.delete(0, "end")

    tk.Button(
        frame,
        text="DELETE",
        font=("Arial", 14, "bold"),
        bg=MAROON,
        fg="white",
        width=15,
        command=do_delete,
    ).pack(pady=10)


def open_update_student(root):
    win = tk.Toplevel(root)
    win.title("Update Student")
    win.geometry("500x550")
    win.configure(bg="white")

    frame = tk.Frame(win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="UPDATE STUDENT",
        font=("Arial", 22, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=10)

    tk.Label(frame, text="Enter Student ID", bg="white").pack()
    id_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    id_entry.pack(pady=10)

    fields_frame = tk.Frame(frame, bg="white")

    first_entry = tk.Entry(fields_frame, font=("Arial", 14), width=25, justify="center")
    last_entry = tk.Entry(fields_frame, font=("Arial", 14), width=25, justify="center")
    course_entry = tk.Entry(fields_frame, font=("Arial", 14), width=25, justify="center")
    year_entry = tk.Entry(fields_frame, font=("Arial", 14), width=25, justify="center")

    def load_student():
        sid = id_entry.get().strip()

        if sid not in student_ids:
            messagebox.showerror("Error", "Student not found.")
            fields_frame.pack_forget()
            return

        i = student_ids.index(sid)

        for entry, value in (
            (first_entry, student_first_names[i]),
            (last_entry, student_last_names[i]),
            (course_entry, student_courses[i]),
            (year_entry, student_year_levels[i]),
        ):
            entry.delete(0, "end")
            entry.insert(0, value)

        fields_frame.pack(pady=10)
        messagebox.showinfo("Found", "Student loaded! You may edit the fields below.")

    tk.Button(
        frame, text="LOAD", command=load_student, bg=MAROON, fg="white", width=15
    ).pack(pady=5)

    tk.Label(fields_frame, text="FIRST NAME", bg="white").pack()
    first_entry.pack(pady=5)

    tk.Label(fields_frame, text="LAST NAME", bg="white").pack()
    last_entry.pack(pady=5)

    tk.Label(fields_frame, text="COURSE", bg="white").pack()
    course_entry.pack(pady=5)

    tk.Label(fields_frame, text="YEAR LEVEL (1-5)", bg="white").pack()
    year_entry.pack(pady=5)

    def save_update():
        sid = id_entry.get().strip()

        if sid not in student_ids:
            messagebox.showerror("Error", "Student not found.")
            return

        new_first = first_entry.get().strip()
        new_last = last_entry.get().strip()
        new_course = course_entry.get().strip()
        new_year = year_entry.get().strip()

        if not new_first or not new_last or not new_course or not new_year:
            messagebox.showerror("Error", "All fields are required.")
            return

        if not is_valid_name(new_first):
            messagebox.showerror("Error", "First name cannot contain numbers.")
            return

        if not is_valid_name(new_last):
            messagebox.showerror("Error", "Last name cannot contain numbers.")
            return

        if not is_valid_name(new_course):
            messagebox.showerror("Error", "Course cannot contain numbers.")
            return

        try:
            year_level = int(new_year)
            if not (1 <= year_level <= 5):
                messagebox.showerror("Error", "Year level must be between 1 and 5.")
                return
        except ValueError:
            messagebox.showerror("Error", "Year level must be a number.")
            return

        if not messagebox.askyesno("Confirm", "Save changes to this student?"):
            return

        i = student_ids.index(sid)
        student_first_names[i] = new_first.title()
        student_last_names[i] = new_last.title()
        student_courses[i] = new_course.upper()
        student_year_levels[i] = year_level

        save_students()

        messagebox.showinfo("Success", "Student updated successfully!")
        win.destroy()

    tk.Button(
        frame,
        text="SAVE UPDATE",
        font=("Arial", 14, "bold"),
        bg=MAROON,
        fg="white",
        width=18,
        command=save_update,
    ).pack(pady=20)
")