import tkinter

root = tkinter.Tk()
root.title("Thermostat Vibe")
root.geometry("400x300")

warning = tkinter.StringVar(value="")
temperature = tkinter.IntVar(value=25)


def boiling_warning(event):
    boiling_point = 100
    if temperature.get() >= boiling_point:
        warning.set("Boiling point!")
    else:
        warning.set("")


tkinter.Label(root, text="Thermostat (Celsius)").pack()

# TODO: Add slider
slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    variable=temperature,
    command=boiling_warning,
)
slider.pack()

tkinter.Label(root, textvariable=warning).pack()

root.mainloop()
