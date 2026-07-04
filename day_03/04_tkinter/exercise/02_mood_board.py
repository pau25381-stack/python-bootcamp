import tkinter

root = tkinter.Tk()
root.title("Mood Board")
root.geometry("400x300")

# TODO: Add properties to design
label1 = tkinter.Label(root,
    text=":) Happy",
    bg="green",
    fg="white",
    font=("Arial", 20),
    width=20,
    height=10
)

# TODO: Apply side property
label1.pack(side="left", fill="both", expand=True)


# TODO: Add properties to design
label2 = tkinter.Label(root,
    text=":( Sad",
    bg="blue",
    fg="white",
    font=("Arial", 20),
    width=20,
    height=10
)

# TODO: Apply side property
label2.pack(side="left", fill="both", expand=True)

root.mainloop()
