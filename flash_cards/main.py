import tkinter as tk
import pandas as pd
import random as rd
import json
from tkinter import ttk, PhotoImage

# data files
data = pd.read_csv("french_data.csv")
french_words = data["French"].to_list()
english_words = data["English"].to_list()

# window part
window = tk.Tk()
window.title("flash cards")
window.minsize(width=500, height=500)

# canvas part(uploaded image)
canva = tk.Canvas(width=500, height=500, highlightthickness=1)
flag_img = tk.PhotoImage(file="france_flag.png")
canva.create_image(250, 250, image=flag_img)
canva.place(x=0, y=0)

# some variable for change language
lan_var = "fr"
fr_word = "Bonjour!"
en_word = "Good Morning!"


# some functions
def change_meaning():
    global lan_var
    if lan_var == "fr":
        lan_var = "en"
        main_button.configure(text=f"English Meaning\n\n{en_word}")
    else:
        lan_var = "fr"
        main_button.configure(text=f"French Meaning\n\n{fr_word}")


def mark_correct():
    global lan_var
    global fr_word
    global en_word

    index = rd.randint(1, 22)
    fr_word = french_words[index]
    en_word = english_words[index]

    lan_var = "fr"
    main_button.configure(text=f"French Meaning\n\n{fr_word}")

    new_data = {
        f"{index}": {
            "fr": fr_word,
            "en": en_word,
        }
    }

    try:
        with open("data.json", 'r') as json_data:
            initial_data = json.load(json_data)
            initial_data.update(new_data)

        with open("data.json", 'w') as json_data:
            json.dump(initial_data, json_data, indent=4)
    except FileNotFoundError:
        with open("data.json", 'w') as json_data:
            json.dump(new_data, json_data, indent=4)


def mark_wrong():
    global lan_var
    global fr_word
    global en_word

    index = rd.randint(1, 22)
    fr_word = french_words[index]
    en_word = english_words[index]

    lan_var = "fr"
    main_button.configure(text=f"French Meaning\n\n{fr_word}")


# input boxes and labels
font = ("Arial", 30)

# Define custom colors
dark_gray = "#444444"
light_gray = "#CCCCCC"

main_button = ttk.Button(text="French Meaning\n\nBonjour!", style="Custom.TButton", width=20, command=change_meaning)
canva.create_window(250, 150, window=main_button)

# Check PhotoImage
check_image = PhotoImage(file="check_mark.png")
check_image = check_image.subsample(6)

check_button = ttk.Button(canva, text="Find", style="Custom.TButton", image=check_image, command=mark_correct)
canva.create_window(400, 300, window=check_button)

# Cross PhotoImage
cross_image = PhotoImage(file="cross_mark.png")
cross_image = cross_image.subsample(6)

check_button = ttk.Button(canva, text="Find", style="Custom.TButton", image=cross_image, command=mark_wrong)
canva.create_window(100, 300, window=check_button)


# Define custom styles
style = ttk.Style()
style.configure("Custom.TButton", background=dark_gray, foreground="black", font=font, borderwidth=0, padding=0.5, highlightthickness=1, highlightcolor=dark_gray, highlightbackground=dark_gray)


# Run the main loop
window.mainloop()


