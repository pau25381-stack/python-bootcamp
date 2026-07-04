import tkinter

root = tkinter.Tk()
root.title("Check Box")
root.geometry("400x300")

label_value = tkinter.StringVar(value="")
check_value = tkinter.BooleanVar()


def greeting():
    if check_value.get():
        label_value.set("Hello")
    else:
        label_value.set("")


# TODO: Add checkbox button buttons

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    root,
    text="Enable",
    variable=check_value,
    command=greeting
)
checkbox.pack()

label = tkinter.Label(root, textvariable=label_value)
label.pack()

root.mainloop()
