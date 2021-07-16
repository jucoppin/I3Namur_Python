import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master=master, bg='pink')

class LabelFrame(tk.LabelFrame):
    def __init__(self, master, text) -> None:
        # Les options sont en MINISCULES
        super().__init__(master=master, text=text, bg='salmon', font=("Arial", 42), labelanchor='n')
