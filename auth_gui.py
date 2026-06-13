import tkinter as tk
from tkinter import messagebox

MAROON = "#800000"
GOLD = "#FFD700"
ACCOUNT_FILE = "accounts.txt"


def open_login(root, on_success):
    """on_success(username, role) is called after a successful login."""

    win = tk.Toplevel(root)
    win.title("Login")
    win.geometry("450x400")
    win.configure(bg="white")

    frame = tk.Frame(win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="LOGIN",
        font=("Arial", 28, "bold"),
        fg=MAROON,
        bg="white",
    ).pack(pady=15)

    tk.Label(frame, text="USERNAME", bg="white", font=("Arial", 12)).pack()
    username_entry = tk.Entry(frame, font=("Arial", 14), width=25, justify="center")
    username_entry.pack(pady=8)

    tk.Label(frame, text="PASSWORD", bg="white", font=("Arial", 12)).pack()
    password_entry = tk.Entry(
        frame, font=("Arial", 14), width=25, show="*", justify="center"
    )
    password_entry.pack(pady=8)

    def do_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Fill all fields.")
            return

        try:
            with open(ACCOUNT_FILE, "r") as f:
                for line in f:
                    data = line.strip().split(",")

                    if len(data) == 3:
                        user, pwd, role = data

                        if username == user and password == pwd:
                            messagebox.showinfo(
                                "Success", f"Login successful!\nRole: {role}"
                            )
                            win.destroy()
                            on_success(user, role.lower())
                            return

            messagebox.showerror("Error", "Invalid username or password.")

        except FileNotFoundError:
            messagebox.showerror("Error", "No accounts found. Please register first.")

    tk.Button(
        frame,
        text="LOGIN",
        font=("Arial", 14, "bold"),
        width=18,
        bg=MAROON,
        fg="white",
        command=do_login,
    ).pack(pady=15)

    tk.Button(
        frame,
        text="REGISTER INSTEAD",
        font=("Arial", 10, "bold"),
        bg=GOLD,
        fg="black",
        command=lambda: (win.destroy(), open_register(root, on_success)),
    ).pack(pady=5)
