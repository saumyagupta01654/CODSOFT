import tkinter as tk
from tkinter import simpledialog, messagebox

# --------------------------
#   To-Do List App (Simple)
# --------------------------

tasks = []  # Each task is stored as a dictionary: {"task": "text", "done": False}

def refresh_list():
    """Refresh the Listbox every time task updates"""
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t["done"] else "✗"
        listbox.insert(tk.END, f"[{status}]  {t['task']}")

def add_task():
    task_text = task_entry.get()
    if task_text.strip() == "":
        messagebox.showwarning("Warning", "Enter a task!")
        return
    
    tasks.append({"task": task_text, "done": False})
    task_entry.delete(0, tk.END)
    refresh_list()

def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        refresh_list()
    except:
        messagebox.showwarning("Warning", "Select a task to mark as complete!")

def edit_task():
    try:
        index = listbox.curselection()[0]
        old_text = tasks[index]["task"]
        
        new_text = simpledialog.askstring("Edit Task", "Update task:", initialvalue=old_text)
        if new_text:
            tasks[index]["task"] = new_text
            refresh_list()
    except:
        messagebox.showwarning("Warning", "Select a task to edit!")

# --------------------------
#   GUI Layout
# --------------------------

root = tk.Tk()
root.title("Simple To-Do List App")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", width=20, command=add_task)
btn_add.pack(pady=5)

btn_done = tk.Button(root, text="Mark As Done", width=20, command=mark_done)
btn_done.pack(pady=5)

btn_edit = tk.Button(root, text="Edit Task", width=20, command=edit_task)
btn_edit.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()
