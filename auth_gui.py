import tkinter as tk
from tkinter import messagebox

LIGHTBLUE = "#B0E2FF" 
LIGHTPINK = "#FFAEB9"
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
        fg=LIGHTBLUE,
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
        bg=LIGHTBLUE,
        fg="white",
        command=do_login,
    ).pack(pady=15)

    tk.Button(
        frame,
        text="REGISTER INSTEAD",
        font=("Arial", 10, "bold"),
        bg=LIGHTPINK,
        fg="black",
        command=lambda: (win.destroy(), open_register(root, on_success)),
    ).pack(pady=5)


def open_register(root, on_success=None):
    """If on_success is provided, opens the login window after registering."""

    win = tk.Toplevel(root)
    win.title("Register")
    win.geometry("450x450")
    win.configure(bg="white")

    frame = tk.Frame(win, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="REGISTER",
        font=("Arial", 28, "bold"),
        fg=LIGHTBLUE,
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

    role_var = tk.StringVar(value="user")

    tk.Label(frame, text="ROLE", bg="white", font=("Arial", 12)).pack(pady=(10, 0))

    tk.Radiobutton(
        frame,
        text="Admin",
        variable=role_var,
        value="admin",
        bg="white",
        font=("Arial", 11),
    ).pack()

    tk.Radiobutton(
        frame,
        text="User",
        variable=role_var,
        value="user",
        bg="white",
        font=("Arial", 11),
    ).pack()

    def do_register():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        role = role_var.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required.")
            return

        try:
            with open(ACCOUNT_FILE, "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) == 3 and data[0] == username:
                        messagebox.showerror("Error", "Username already exists!")
                        return
        except FileNotFoundError:
            pass

        if not messagebox.askyesno("Confirm", "Create this account?"):
            return

        with open(ACCOUNT_FILE, "a") as f:
            f.write(f"{username},{password},{role}\n")

        messagebox.showinfo("Success", "Account created! You can now log in.")
        win.destroy()

        if on_success:
            open_login(root, on_success)

    tk.Button(
        frame,
        text="REGISTER",
        font=("Arial", 14, "bold"),
        width=18,
        bg=LIGHTBLUE,
        fg="white",
        command=do_register,
    ).pack(pady=15)

    if on_success:
        tk.Button(
            frame,
            text="LOGIN INSTEAD",
            font=("Arial", 10, "bold"),
            bg=LIGHTPINK,
            fg="black",
            command=lambda: (win.destroy(), open_login(root, on_success)),
        ).pack(pady=5)