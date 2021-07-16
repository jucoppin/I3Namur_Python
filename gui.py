from Views.app import App
from Views.label import Label
import tkinter as tk
from Views.frame import Frame, LabelFrame
from Views.button import Button
# Start application

"""
Architecture application :
- point d'entreé => gui.py
- Classe custom => Héritée de Tkinter pour mettre une surcouche :
    - Frame, Label, Button, LabelFrame
- Classe applicative => Utilise la classe custom (hérite) :
    - Surcouche logique des classes custom
"""

if __name__ == "__main__":
    root = App()
    root.mainloop()