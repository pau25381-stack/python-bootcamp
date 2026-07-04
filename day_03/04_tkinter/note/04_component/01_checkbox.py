import tkinter

root = tkinter.Tk()
root.title("Check Box")
root.geometry("400x300")

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    root,
    text="Enable",
    variable=check_value
)
checkbox.pack()

root.mainloop()
