import tkinter as tk
from tkinter import messagebox

from student_data import load_students
from student_gui import (
    open_add_student,
    open_view_students,
    open_search_student,
    open_delete_student,
    open_update_student,
)
from auth_gui import open_login, open_register

LIGHTBLUE = "#B0E2FF" 
LIGHTPINK = "#FFAEB9"

current_user = {"username": None, "role": None}


def exit_app(window):
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def show_welcome(window):
    clear_window(window)

    frame = tk.Frame(window, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="STUDENT INFORMATION SYSTEM",
        font=("Arial", 28, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=30)

    btn_frame = tk.Frame(frame, bg="white")
    btn_frame.pack(pady=10)
def on_login_success(username, role):
        current_user["username"] = username
        current_user["role"] = role
        show_dashboard(window)

    tk.Button(
        btn_frame,
        text="LOGIN",
        font=("Arial", 16, "bold"),
        width=15,
        height=2,
        bg=MAROON,
        fg="white",
        command=lambda: open_login(window, on_login_success),
    ).grid(row=0, column=0, padx=15, pady=10)

    tk.Button(
        btn_frame,
        text="REGISTER",
        font=("Arial", 16, "bold"),
        width=15,
        height=2,
        bg=GOLD,
        fg="black",
        command=lambda: open_register(window, on_login_success),
    ).grid(row=0, column=1, padx=15, pady=10)

    tk.Button(
        btn_frame,
        text="EXIT",
        font=("Arial", 16, "bold"),
        width=15,
        height=2,
        bg="red",
        fg="white",
        command=lambda: exit_app(window),
    ).grid(row=0, column=2, padx=15, pady=10)


def show_dashboard(window):
    clear_window(window)

    frame = tk.Frame(window, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="STUDENT INFORMATION SYSTEM",
        font=("Arial", 26, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=10)

    role = current_user["role"]

    tk.Label(
        frame,
        text=f"Logged in as: {current_user['username']} ({role})",
        font=("Arial", 12, "italic"),
        bg="white",
    ).pack(pady=5)

    btn_frame = tk.Frame(frame, bg="white")
    btn_frame.pack(pady=15)

    btn_style = {
        "font": ("Arial", 14, "bold"),
        "width": 20,
        "height": 2,
        "bg": MAROON,
        "fg": "white",
    }

    if role == "admin":
        tk.Button(
            btn_frame, text="ADD STUDENT", command=lambda: open_add_student(window), **btn_style
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            btn_frame, text="VIEW ALL STUDENTS", command=lambda: open_view_students(window), **btn_style
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            btn_frame, text="SEARCH STUDENT", command=lambda: open_search_student(window), **btn_style
        ).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(
            btn_frame, text="DELETE STUDENT", command=lambda: open_delete_student(window), **btn_style
        ).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(
            btn_frame, text="UPDATE STUDENT", command=lambda: open_update_student(window), **btn_style
        ).grid(row=2, column=0, padx=10, pady=10)

        tk.Button(
            btn_frame,
            text="LOGOUT",
            command=lambda: logout(window),
            font=("Arial", 14, "bold"),
            width=20,
            height=2,
            bg="orange",
            fg="white",
        ).grid(row=2, column=1, padx=10, pady=10)

    else:
        tk.Button(
            btn_frame, text="VIEW ALL STUDENTS", command=lambda: open_view_students(window), **btn_style
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            btn_frame, text="SEARCH STUDENT", command=lambda: open_search_student(window), **btn_style
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            btn_frame,
            text="LOGOUT",
            command=lambda: logout(window),
            font=("Arial", 14, "bold"),
            width=20,
            height=2,
            bg="orange",
            fg="white",
        ).grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    tk.Button(
        frame,
        text="EXIT APP",
        command=lambda: exit_app(window),
        font=("Arial", 12, "bold"),
        width=15,
        bg="red",
        fg="white",
    ).pack(pady=15)


def logout(window):
    if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
        current_user["username"] = None
        current_user["role"] = None
        show_welcome(window)


def main():
    load_students()

    window = tk.Tk()
    window.title("Student Information System")
    window.geometry("700x550")
    window.configure(bg="white")

    show_welcome(window)

    window.mainloop()


if __name__ == "__main__":
    main()

