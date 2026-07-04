import tkinter

root = tkinter.Tk()
root.geometry("400x300")

entry = tkinter.Entry(root)
entry.pack()

user_input = tkinter.StringVar(root, value="Enter any text here")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input(event):
    given_text = entry.get()
    user_input.set(given_text)

root.bind("<Return>", show_input)
root.bind("<space>", show_input)
root.mainloop()