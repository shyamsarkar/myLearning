import tkinter as tk
from tkinter import messagebox, GROOVE, SUNKEN, RAISED, FLAT, RIDGE, SOLID


def show_about():
    messagebox.showinfo("About", "This is a sample application.")


root = tk.Tk()
root.geometry('2660x1700+0+0')
root.title("Menu Example")

menu = tk.Menu(root)
root.config(menu=menu)
label = tk.Label(root, text="Enter your name:",
                 relief=GROOVE, pady=30, padx=30)
label.pack()

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

root.mainloop()
