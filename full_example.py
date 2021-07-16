from tkinter import END
# Défini la variable END dans le contexte du fichier
import tkinter as tk
from tkinter.constants import LAST

FONT = ('Arial', 28)

main = tk.Tk()
# WM => Window manager => Même effet que la méthode normale
# 'str' object is not callable
"""
# Invalide car j'écrase le comportement d'une méthode
main.wm_title = "Animalerie"
main.title = "My app"
"""

main.wm_title("Animalerie 2.0")
# Geometry
# Resize

frame = tk.Frame(main)
# frame.pack(fill='both', expand=True)
frame.grid(row=0)
"""
Les enfants de frame sont : 
- tk.Label
- tk.Entry
=> Si un élément utilise grid => TOUS DOIVENT UTILISER GRID DANS FRAME
"""
"""
Master de listbox : main
Enfants de main :
- frame (PACK)
- listbox (PACK)
"""

tk.Label(frame, text="Nom : ", font=FONT).grid(row = 1, column=1, sticky='E')
entry_nom = tk.Entry(frame, font=FONT)
entry_nom.grid(row=1, column=2)

frame2 = tk.LabelFrame(main, text="Custom label", font=FONT)
# Informations générales
# frame2.pack(fill='both', expand=True)
frame2.grid(row=1, sticky='NEWS')

# Listbox => Select (option)
listbox = tk.Listbox(frame2, font=FONT, fg="green", selectbackground="salmon", selectmode=tk.MULTIPLE)
listbox.pack(fill='both', expand=True)

# append, insert, add, push
# end, bottom, len + 1
# tk.END existe toujours mais il préférable d'utiliser END dans ce cas ci car il a été importé.
listbox.insert(END, "A")
listbox.insert(END, "B")
listbox.insert(END, "C")
listbox.insert(END, "D")
listbox.insert(END, "E")

listbox.insert(1, "F")

"""
Event applicatif : 
- Click 
- Input (shortcut)
- Dblclick
- Click droit
- Enter
En JS : element.addEventListener('event', function() {})
En python : C'est similaire 
widget.bind(event, handler)
"""

def callback_nom(event: tk.Event):
    # get / value / val
    # set / value / val
    print(entry_nom.get())
# Button-1 => Click GAUCHE
# Button-2 => Click Molette
# Button-3 => Click DROIT
entry_nom.bind("<Button-1>", callback_nom)
entry_nom.bind("<Button-2>", callback_nom)
entry_nom.bind("<Button-3>", callback_nom)

def save():
    print(listbox.curselection())

tk.Button(frame2, text="Sauver", font=FONT, command=save).pack()

# DELETE item : del, destroy, delete, clear (FULL), remove
# listbox.delete(2, 3) # B, C
# listbox.delete(1)

# How to empty listbox : delete => 0, END
# listbox.delete(0, END)
# Calcul longueur listbox : len, length, size
# print(len(listbox)) -> Widget et non une ckasse qui implémente __len__
print(listbox.size())

# tk.Frame         => Frame
# tk.LabelFrame    => Label frame

frame3 = tk.LabelFrame(main, text="Animal")
frame3.grid(row=10)
# frame3.pack()

tk.Label(frame3, text="Nom").pack()
tk.Label(frame3, text="Prénom").pack()

frame4 = tk.LabelFrame(main, text="Propriétaire")
frame4.grid(row=11)
# frame4.pack()

tk.Label(frame4, text="Nom").pack()
tk.Label(frame4, text="Prénom").pack()

# UX => Ergonomie WEB /Logicielle
"""
Monsieur
Madame
Mr.
Mme
Mevrowww
"""
# Frame, FrameLabel => PACK (FILL='both', expand=True)
# Widgets (Entry, Label) => GRID
# main.grid_columnconfigure(0, weight=1)
main.mainloop()

print("Ceci est un message de flora")