import tkinter

root = tkinter.Tk()
root.title("Password Checker")
root.geometry("400x300")

label1 = tkinter.Label(root, text="Enter your password:")
label1.pack()

entry = tkinter.Entry(root)
entry.pack()

user_result = tkinter.StringVar(root, value="Enter your password and press Enter")
label = tkinter.Label(root, textvariable=user_result)
label.pack()

def check_password(event=None):
    correct_password = "pass"
    if entry.get() == correct_password:
        user_result.set("Password Correct! Access Granted.")
    else:
        user_result.set("Incorrect Password. Try again.")



# TODO: Add label for instructions
# TODO: Add entry for instructions
# TODO: Add StringVar for instruction
# TODO: Add label using StringVar
    # TODO: Check if entry.get() has correct value
# TODO: Add key bindings for check_password

button = tkinter.Button(root, text="Submit", command=check_password)
button.pack()

root.bind("<Return>", check_password)
root.mainloop()
