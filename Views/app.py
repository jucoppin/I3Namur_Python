from Views.button import Button, ButtonImage
from Views.label import Label
from Views.frame import LabelFrame
import tkinter as tk

# https://www.tutorialspoint.com/python/tk_messagebox.htm

# Application
# InterfaceNamur
# Séparer (les classes) votre application non pas en Frame mais en Window
class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.top_level = None

        # A vous de choisir la solution que vous préférez
        # custom = CustomFrame(self)
        # custom.pack(fill='both', expand=True)

        frame2 = LabelFrame(self, text="Tkinter")
        frame2.pack(fill='both', expand=True)

        tk.Label(frame2, text='Label DEUX').grid()

        frame = tk.LabelFrame(self, text="Tkinter")
        frame.pack(fill='both', expand=True)

        tk.Label(frame, text='Label simple').grid()

        # tk.Button(frame, text='NAC')
        # Button(frame, 'NAC')
        ButtonImage(frame2, None, r"C:\Users\Hard\Pictures\random.gif").grid()
        # ButtonImage(frame2, None, r"C:\Users\Hard\Pictures\random.jpg").grid(sticky='NEWS')

        Button(self, 'Destroy frame 2', frame2.destroy).pack()

        # tk.messagebox.showinfo("Impossible de faire ", "Raison")
        """
        # Solution la plus simple
        custom = LabelFrame(self, "Custom")
        tk.Label(custom, text='Label simple').grid()
        Label(custom, text='Label custom').grid()
        Button(custom, "Bouton perso", None).grid()
        Button(custom, "Bouton perso", None).grid()
        """

        Button(self, 'Ouvrir', self.create_window).pack()

    def create_window(self):
        if self.top_level is not None:
            try:
                self.top_level.destroy()
            except:
                pass
        # https://www.tutorialspoint.com/python/tk_toplevel.htm
        self.top_level = tk.Toplevel(self)


    """
    # Solution la plus simple sans faire de classe supplémentaire mais en
    # gardant tout de même une certaine clarté
        self._create_custom()
    
    def _create_custom(self):
        custom = LabelFrame(self, "Custom")
        tk.Label(custom, text='Label simple').grid()
        Label(custom, text='Label custom').grid()
        Button(custom, "Bouton perso", None).grid()
        Button(custom, "Bouton perso", None).grid()
    """

"""
# Solution Orienté Object mais overkill dans ce cas ci
# Eviter dans un premier temps 
class CustomFrame(LabelFrame):
    def __init__(self, master) -> None:
        super().__init__(master, "Custom")

        tk.Label(self, text='Label simple').grid()
        Label(self, text='Label custom').grid()
        Button(self, "Bouton perso", None).grid()
        Button(self, "Bouton perso", None).grid()
"""
