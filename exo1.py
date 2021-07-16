import tkinter as tk

fenetre = tk.Tk()

cadre = tk.Frame(fenetre, width=500, height=500, bg='blue')
cadre.pack(fill="both", expand=True)

label1 = tk.Label(cadre, text="Bienvenue", foreground="red", font=("Helvetica", 24))
label1.pack()

fenetre.mainloop()
