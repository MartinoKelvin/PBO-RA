import tkinter as tk
from tkinter import messagebox
import json
import os

USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file)

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.configure(bg="#309898")  # Background warna

        self.users = load_users()

        tk.Label(root, text="Username:", bg="#E0F7FA").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(root, bg="white")
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Password:", bg="#E0F7FA").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(root, show="*", bg="white")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(root, text="Login", command=self.validate_login, bg="#4FC3F7", fg="white").grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Register", command=self.open_register, bg="#81D4FA", fg="white").grid(row=3, column=0, columnspan=2)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Success", f"Welcome {username}!")
            self.root.destroy()
            open_main_window(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_register(self):
        reg_win = tk.Toplevel(self.root)
        reg_win.title("Register")
        reg_win.configure(bg="#B2C6D5")

        tk.Label(reg_win, text="Username:", bg="#E0F7FA").grid(row=0, column=0, padx=10, pady=5)
        username_entry = tk.Entry(reg_win, bg="white")
        username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(reg_win, text="Password:", bg="#E0F7FA").grid(row=1, column=0, padx=10, pady=5)
        password_entry = tk.Entry(reg_win, show="*", bg="white")
        password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(reg_win, text="Confirm Password:", bg="#E0F7FA").grid(row=2, column=0, padx=10, pady=5)
        confirm_entry = tk.Entry(reg_win, show="*", bg="white")
        confirm_entry.grid(row=2, column=1, padx=10, pady=5)

        def register():
            username = username_entry.get()
            password = password_entry.get()
            confirm = confirm_entry.get()

            if username in self.users:
                messagebox.showerror("Error", "Username already exists.")
            elif password != confirm:
                messagebox.showerror("Error", "Passwords do not match.")
            elif username == "" or password == "":
                messagebox.showerror("Error", "Fields cannot be empty.")
            else:
                self.users[username] = password
                save_users(self.users)
                messagebox.showinfo("Success", "Registration successful!")
                reg_win.destroy()

        tk.Button(reg_win, text="Register", command=register, bg="#4DB6AC", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

def open_main_window(username):
    main_win = tk.Tk()
    main_win.title("Main Window - Welcome")
    main_win.configure(bg="#FFFFFF")

    # Widget 1: Label besar berwarna
    label = tk.Label(main_win, text=f"Welcome, {username}!", font=("Arial", 24), bg="#4B9CD3", fg="white")
    label.pack(pady=20, fill="x")

    # Widget 2: Frame dengan Entry dan Label di dalamnya
    frame = tk.Frame(main_win, bg="#E6FFFA", bd=2, relief="groove", padx=10, pady=10)
    tk.Label(frame, text="Masukkan sesuatu:", bg="#E6FFFA").grid(row=0, column=0, padx=5, pady=5)
    tk.Entry(frame, width=20, bg="white").grid(row=0, column=1, padx=5, pady=5)
    frame.pack(pady=10)

    # Widget 3: Tombol interaktif
    def change_label():
        label.config(text="You clicked the button!", bg="#FF6F61")

    btn = tk.Button(main_win, text="Click Me!", bg="#FFD700", fg="black", font=("Helvetica", 14), command=change_label)
    btn.pack(pady=15)

    # Widget 4: Listbox berwarna
    listbox = tk.Listbox(main_win, bg="#FAFAD2", fg="black", font=("Arial", 12), height=4)
    for item in ["Item 1", "Item 2", "Item 3"]:
        listbox.insert(tk.END, item)
    listbox.pack(pady=10)

    main_win.mainloop()

# Run Aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
