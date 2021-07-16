from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text="Red", fg="red", font=("Helvetica", 36))
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text="Brown", fg="brown", font=("Helvetica", 36))
greenbutton.pack(side=RIGHT)

bluebutton = Button(frame, text="Blue", fg="blue", font=("Helvetica", 36))
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack(side=BOTTOM)

root.mainloop()
