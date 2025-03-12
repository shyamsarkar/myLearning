from tkinter import Tk, Label, GROOVE, RAISED, SUNKEN, X, Menu, messagebox, Toplevel, Button, LEFT, LabelFrame, Entry, StringVar
from datetime import date
bg_color = "#009999"
current_date = date.today()

root = Tk()
root.configure(bg="#f0f0f0")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the window size based on screen size
window_width = int(screen_width * 1)
window_height = int(screen_height * 1)
# Set the window position to the center of the screen
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2


root.geometry(
    f"{window_width}x{window_height}+{x_position}+{y_position}")

root.title("Billing Software")


title = Label(root, text="Restaurant", bd=4, relief=RAISED, font=(
    "times new roman", 20, "bold"), padx=20, pady=2, width=15)
title.pack(anchor='w')  # sending this to west side(left alignment)


def open_dashboard():
    messagebox.showinfo("Dashboard", "All the Dashboard data will come here")


def description_about_us():
    about_window = Toplevel(root)
    about_window.title("About Us")
    about_window.geometry("900x300")
    about_message = "Developed by Shyam Sarkar\n\n" \
                    "github link : https://github.com/shyamsarkar"

    about_label = Label(about_window, text=about_message, padx=10, pady=10)
    about_label.pack()
    close_button = Button(about_window, text="Close",
                          command=about_window.destroy)
    close_button.pack(pady=10)


menu = Menu(root)
menu.add_command(label="Dashboard", command=open_dashboard)
menu.add_command(label="About", command=description_about_us)
menu.add_command(label="Quit", command=root.quit)

root.config(menu=menu)  # show the menu


customer_box = LabelFrame(root, text="Customer Details", bd=10, relief=GROOVE, font=(
    "times new roman", 15, "bold"), bg=bg_color, fg="#191970")
customer_box.place(x=0, y=100, relwidth=0.19, relheight=0.9)


def handleCustomerBtn():
    print("Customer Selected")


for i in range(10):
    button = Button(customer_box, text=f"{current_date.day}/{current_date.month}/000{i+1}",
                    command=handleCustomerBtn, anchor='w', width=20, height=2)
    button.grid(row=i, column=0)


item_box = LabelFrame(root, text="Select Item", bd=10, relief=GROOVE, font=(
    "times new roman", 15, "bold"), bg=bg_color, fg="#191970")
item_box.place(relx=0.2, y=100, relwidth=0.33, relheight=0.9)


orders_box = LabelFrame(root, text="Orders", bd=10, relief=GROOVE, font=(
    "times new roman", 15, "bold"), bg=bg_color, fg="#191970")
orders_box.place(relx=0.54, y=100, relwidth=0.45, relheight=0.9)

root.mainloop()
