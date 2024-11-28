import tkinter as tk


def print_config(widget, name):
    """ Print tkinter widget configuration """
    print(name + " Config:")
    widget_config = widget.config()
    for item in widget_config:
        print(item, widget_config[item])
        print("\n")

# Print the Widget

button = tk.Button(text="Click me!")
print_config(button, "button")

# Print the class public attributes

print(f"{dir(tk.Button)=}\n")

# Print the class help

help(tk.Frame)
