import tkinter as tk
from tkinter import font

class Label(tk.Label):
    def __init__(self, master, text) -> None:
        super().__init__(master=master, text=text, font=("Helvetica", 24), fg='blue')