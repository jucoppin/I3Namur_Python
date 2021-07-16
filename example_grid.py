import tkinter as tk


def je_sais_pas_callback():
    print("CLICK")
    print(entry.get())
    # a = Animal()
    # prenom = entry.get()
    # nom = entry.get()
    # p = Personne(prenom, nom)



main = tk.Tk()

font = ("Helvetica", 28)

"""
Le grid n'a pas de valeur spécifique à utiliser
Par défaut tout commence à 0 (row et col)
Mais les lignes / colonnes non utilsée -> ignorée

tabindex => JS
"""
# Pour de la maintenance c'est le pied
row, col = 1, 1
label1 = tk.Label(main, text="Label 1", font=font)
label1.grid(row=row, column=col, columnspan=10)
row, col = row + 1, 1

tk.Label(main, text="Label 2", font=font).grid(row=row, column=col, sticky='e')
col += 1
tk.Label(main, text="Label 2 bis", font=font).grid(row=row, column=col)  # col + 1
col += 1  # 3
# Plein de choses
tk.Label(main, text="Label 2 multi", font=font).grid(row=row, rowspan=2, column=col + 3, sticky='s')
col += 3  # 6

# Un label en col 5 de la row 2 à 3

row, col = row + 1, 1

tk.Label(main, text="Label 2/3", font=font).grid(row=row, column=col)
row, col = row + 1, 1

# ICI
tk.Label(main, text="Label 3", font=font).grid(row=row, column=col)
col += 1
# NOUVEAUTE
tk.Label(main, text="a", font=font).grid(row=row, column=col + 1 + 3, rowspan=2, sticky='S,E')
row, col = row + 1, 1

tk.Label(main, text="Label 4", font=font).grid(row=row, column=col, columnspan=2)
row, col = row + 1, 1

sub_frame = tk.Frame(main, bg="salmon")
sub_frame.grid(row=row, column=col, columnspan=10)
# tk.Label(sub_frame, text="sub", font=font).grid(row=1, column=1)
tk.Label(sub_frame, text="sub", font=font).pack()
entry = tk.Entry(sub_frame, font=font)
entry.pack()
# https://www.tutorialspoint.com/python3/tk_button.htm
tk.Button(sub_frame, text="Je sais pas", fg="cyan", font=("Arial", 42), command=je_sais_pas_callback).pack()  # _tkinter.TclError: cannot use geometry manager grid inside .!frame which already has slaves managed by pack
tk.Button(sub_frame, text="Fermer", fg="red", font=("Arial", 26), command=main.destroy).pack()  # _tkinter.TclError: cannot use geometry manager grid inside .!frame which already has slaves managed by pack
# destroy / quit
# https://stackoverflow.com/questions/47378715/tkinter-how-to-get-the-value-of-an-entry-widget


# (<class '_tkinter.TclError'>, TclError('ambiguous option "-col": must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky'), <traceback object at 0x0000023666340C40>)
# colum(0,1) => (<class '_tkinter.TclError'>, TclError('bad column value "0 1": must be a non-negative integer'), <traceback object at 0x000001EA5CF20DC0>)
# Changements qui viennent via un event par exemple
print(label1.grid_info())  # {'in': <tkinter.Tk object .>, 'column': 1, 'row': 1, 'columnspan': 1, 'rowspan': 1, 'ipadx': 0, 'ipady': 0, 'padx': 0, 'pady': 0, 'sticky': ''}
# A droite du label 1
# ipad => PADDING
# pad => MARGIN
# Sticky => N W S E
label1_info = label1.grid_info()
# {'in': <tkinter.Tk object .>, 'column': 1, 'row': 1, 'columnspan': 10, 'rowspan': 1, 'ipadx': 0, 'ipady': 0, 'padx': 0, 'pady': 0, 'sticky': ''}
tk.Label(main, text="Label 1 et quelque", font=font).grid(row=label1_info['row'], column=label1_info['column'] + label1_info['columnspan'] + 1)  # row = 1, column = 2 # hardcodé

main.mainloop()
