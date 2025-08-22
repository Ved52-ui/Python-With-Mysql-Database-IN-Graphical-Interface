------------
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


def submit_data():
    name = entry_name.get()
    number = entry_number.get()

    if name == "" or number == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="127.0.0.1",       # Replace with your host
            user="root",            # Replace with your MySQL username
            password="5544",        # Replace with your MySQL password
            database="testdb"       # Replace with your database name
        )
        cursor = conn.cursor()
        query = "INSERT INTO users (name, number) VALUES (%s, %s)"
        values = (name, number)
        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Success", "Data submitted successfully")

        # Clear input fields
        entry_name.delete(0, tk.END)
        entry_number.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# Create the GUI window
root = tk.Tk()
root.title("User Form")
root.geometry("400x300")
root.minsize(320, 240)
root.configure(bg="#f0f4f8")

# Style configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#ffffff")
style.configure("TLabel", background="#ffffff", font=("Segoe UI", 11))
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11, "bold"), foreground="#ffffff", background="#0078d7")
style.map("TButton", background=[("active", "#005fa3")])

# Main frame
main_frame = ttk.Frame(root, padding=20, style="TFrame")
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Configure grid weights for responsiveness
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=0)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_rowconfigure(3, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Title label
title_label = ttk.Label(main_frame, text="User Registration", font=("Segoe UI", 16, "bold"), foreground="#0078d7")
title_label.grid(row=0, column=0, pady=(0, 15), sticky="ew")

# Name label and entry
name_label = ttk.Label(main_frame, text="Name:")
name_label.grid(row=1, column=0, sticky="w", pady=(0, 2))
entry_name = ttk.Entry(main_frame, width=30, font=("Segoe UI", 11))
entry_name.grid(row=2, column=0, sticky="ew", pady=(0, 10), ipady=8)  # Increased ipady

# Number label and entry
number_label = ttk.Label(main_frame, text="Number:")
number_label.grid(row=3, column=0, sticky="w", pady=(0, 2))
entry_number = ttk.Entry(main_frame, width=30, font=("Segoe UI", 11))
entry_number.grid(row=4, column=0, sticky="ew", pady=(0, 15), ipady=8)  # Increased ipady

# Submit button
submit_btn = ttk.Button(main_frame, text="Submit", command=submit_data, style="TButton")
submit_btn.grid(row=5, column=0, pady=5, ipadx=10, ipady=2, sticky="ew")

# "Made By Ved..." label at the bottom
footer_label = ttk.Label(
    root,
    text="Made By Ved...",
    font=("Segoe Script", 12, "bold"),
    foreground="#ff69b4",
    background="#f0f4f8"
)
footer_label.grid(row=1, column=0, pady=(0, 10), sticky="ew")

# Make footer stick to the bottom on resize
root.grid_rowconfigure(1, weight=0)

root.mainloop()
