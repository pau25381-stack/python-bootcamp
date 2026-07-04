import tkinter

root = tkinter.Tk()
root.title("Mood Board")
root.geometry("400x300")

# TODO: Add properties to design
label1 = tkinter.Label(root, text=":) Happy")

# TODO: Apply side property
label1.pack(side="left")

# TODO: Add properties to design
label2 = tkinter.Label(root, text=":( Sad")

# TODO: Apply side property
label2.pack(side="right")

root.mainloop()
