import tkinter as ttk
from tkinter import messagebox
import random
import pyperclip
import json

FONT = "Arial"
DEFAULT_TEXT = "test@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(ttk.END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
data_list = []


def save_password():
    web = website_entry.get()
    ema = email_entry.get()
    pas = password_entry.get()
    data_list.append({
            "email": ema,
            "password": pas,
        })
    new_entry = {
        web: data_list
    }

    if len(web) == 0 or len(ema) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {ema}\nPass"
                                                          f"word: {pas}\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_entry)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_entry, data_file, indent=4)

            else:
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, ttk.END)
                email_entry.delete(0, ttk.END)
                password_entry.delete(0, ttk.END)
                email_entry.insert(ttk.END, DEFAULT_TEXT)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def find_password():
    searched_item = website_entry.get().capitalize()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=searched_item, message="No Data File found!")
    else:
        if searched_item in data:
            list_of_data = data[searched_item]
            for item in range(len(list_of_data)):
                output_message = f"Email: {list_of_data[item]['email']}\nPassword: {list_of_data[item]['password']}"
                messagebox.showinfo(title=searched_item, message=output_message)
        else:
            messagebox.showinfo(title="Error", message=f"No records for {searched_item} found!")

# ---------------------------- UI SETUP ------------------------------- #

window = ttk.Tk()
window.title("Password Manager")
window.config(padx=30, pady=20)

canvas = ttk.Canvas(window, width=200, height=200)
logo = ttk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels

website_label = ttk.Label(window, text="Website:")
website_label.grid(row=1, column=0)

email_label = ttk.Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = ttk.Label(window, text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = ttk.Entry(window, width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = ttk.Entry(window, width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(ttk.END, DEFAULT_TEXT)

password_entry = ttk.Entry(window, width=34)
password_entry.grid(row=3, column=1)

# Buttons

generate_button = ttk.Button(window, text="Generate Password", command=generate_password, width=14)
generate_button.grid(row=3, column=2)

add_button = ttk.Button(window, text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = ttk.Button(window, text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
