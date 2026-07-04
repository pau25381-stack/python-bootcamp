import tkinter

root = tkinter.Tk()
label =tkinter.Label(
    root,
    text="Hello",
    font=("Arial", "14", "bold italic"),
    fg="red",
    bg="yellow",
    width=100,
    height=20,
    padx=10,
    pady=200,
)

label.pack()
root.mainloop()

#message = """
#Loops within loops spin
#"""


#label1 = tkinter.Label(root, text=message)
#label1.pack()

#root.mainloop()
