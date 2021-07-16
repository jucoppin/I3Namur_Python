import tkinter as tk

class Button(tk.Button):
    def __init__(self, master, text, command) -> None:
        super().__init__(master=master, text=text, command=command, font=("Arial", 18), fg="#ff0062")

class ButtonImage(tk.Button):
    def __init__(self, master, command, image) -> None:
        photo_image = tk.PhotoImage(file=image)
        super().__init__(master=master, command=command, image=photo_image)
