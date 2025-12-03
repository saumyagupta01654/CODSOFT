import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=25, borderwidth=3, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2,
                        command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2,
                        command=lambda val=text: click(val))

    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(root, text="C", width=22, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()

