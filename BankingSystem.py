import sqlite3
from tkinter import *

# DB setup
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    acc_no TEXT PRIMARY KEY,
    name TEXT,
    pin TEXT,
    balance INTEGER
)
""")
conn.commit()

# Main window
root = Tk()
root.title("Banking System")
root.geometry("400x400")

# Functions
def create_account():
    acc = acc_entry.get()
    name = name_entry.get()
    pin = pin_entry.get()
    bal = int(balance_entry.get())

    cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?)",
                   (acc, name, pin, bal))
    conn.commit()

    result_label.config(text="Account Created ✅")

def login():
    acc = acc_entry.get()
    pin = pin_entry.get()

    cursor.execute("SELECT * FROM accounts WHERE acc_no=? AND pin=?",
                   (acc, pin))
    data = cursor.fetchone()

    if data:
        result_label.config(text="Login Success ✅")
    else:
        result_label.config(text="Login Failed ❌")

# UI Elements
Label(root, text="Account No").pack()
acc_entry = Entry(root)
acc_entry.pack()

Label(root, text="Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="PIN").pack()
pin_entry = Entry(root, show="*")
pin_entry.pack()

Label(root, text="Balance").pack()
balance_entry = Entry(root)
balance_entry.pack()

Button(root, text="Create Account", command=create_account).pack(pady=10)
Button(root, text="Login", command=login).pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()