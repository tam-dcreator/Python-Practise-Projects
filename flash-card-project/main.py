import tkinter as tk
import pandas as pd
import random as r
from tkinter import messagebox

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CARD SETUP ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
except pandas.errors.EmptyDataError:
    data = pd.read_csv("data/french_words.csv")
finally:
    # noinspection PyUnboundLocalVariable
    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    try:
        current_card = r.choice(to_learn)
    except IndexError:
        messagebox.showinfo(title="Congratulation", message="You now know all the words in our dictionary")
        exit()
    else:
        french_text = current_card['French']
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(card_word, text=french_text, fill="black")
        canvas.itemconfig(card_title, text="French", fill="black")
        timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- FLIP CARD SETUP ------------------------------- #


def flip_card():
    global current_card
    english_text = current_card["English"]
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_text, fill="white")
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="./images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
wrong_img = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(window, image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


next_card()

window.mainloop()
