# from tkinter import * # Pas recommandé car la librairie est complexe
# https://docs.python.org/3/library/tk.html

import tkinter as tk # Way to go

"""
Input
Label
Frame -> Cadre / Fenetre
Button -> Button (Click avec action)
Tk -> HTML
Frame -> Div / body
"""

"""
Tout widget, va avoir un parent direct
-> POSITION
-> Si le parent est détruit, les enfants le sont aussi 
"""


fenetre_principale = tk.Tk()
# TODO Code logique
# https://www.tutorialspoint.com/python3/tk_frame.htm
frame = tk.Frame(fenetre_principale, width=100, height=100, bg="red")
frame.pack()

# https://www.tutorialspoint.com/python/tk_label.htm
# https://pythonbasics.org/tkinter-label/
etiquette = tk.Label(frame, text="Hello, World!", font=("Helvetica", 36))
etiquette.pack()
# Comment modifier les options via du code => EN LIVE
fenetre_principale.mainloop()
