import tkinter

root = tkinter.Tk()
root.title("Forms")
root.geometry("400x300")

# TODO: Create StringVar for name
# TODO: Create StringVar for name
entry = tkinter.Entry(root)
entry.pack()

name = tkinter.StringVar(root, value="Enter your name")
label = tkinter.Label(root, textvariable=name)
label.pack()

def show_name(event):

#
# TODO: Create StringVar for age
# TODO: Create StringVar for age
age = tkinter.StringVar(root, value="Enter your age")
label = tkinter.Label(root, textvariable=age)
label.pack()

# TODO: Create StringVar for theme
# TODO: Create StringVar for theme
theme = tkinter.StringVar(root, value="Enter your age")
label = tkinter.Label(root, textvariable=theme)
label.pack()


# TODO: Create BooleanVar for subscribe
# TODO: Create BooleanVar for subscribe

# TODO: Create IntVar for rating
# TODO: Create IntVar for rating

# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save

root.mainloop()
