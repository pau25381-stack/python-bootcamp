import tkinter
import json
import tkinter as tk

root = tkinter.Tk()
root.title("Forms")
root.geometry("400x300")

# TODO: Create StringVar for name
# TODO: Create StringVar for name
name_var = tk.StringVar()

# TODO: Create StringVar for age
# TODO: Create StringVar for age
age_var = tk.StringVar()

# TODO: Create StringVar for theme
# TODO: Create StringVar for theme
theme_var = tk.StringVar()


# TODO: Create BooleanVar for subscribe
# TODO: Create BooleanVar for subscribe
subscribe_var = tk.BooleanVar()

# TODO: Create IntVar for rating
# TODO: Create IntVar for rating
rating_var = tk.IntVar()

tk.Label(root,text="Name:").grid(row=0, column=0, sticky="w", padx=3, pady=3)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=3, pady=3)

tk.Label(root,text="Age:").grid(row=1, column=0, sticky="w", padx=3, pady=3)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1, padx=3, pady=3)

tk.Label(root,text="Theme:").grid(row=2, column=0, sticky="w", padx=3, pady=3)
tk.Entry(root, textvariable=theme_var).grid(row=2, column=1, padx=3, pady=3)

tk.Checkbutton(root, text="Subscribe", variable=subscribe_var).grid(row=3, column=0, columnspan=2, sticky="w", padx=3, pady=3)

tk.Label(root, text="Rate (1-5):").grid(row=4, column=0, sticky="w", padx=3, pady=3)
tk.Spinbox(root, from_=1, to=5, textvariable=rating_var).grid(row=4, column=1, padx=3, pady=3)

# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save

def save_to_json():
    data = {
        "name": name_var.get(),
        "age": age_var.get(),
        "theme": theme_var.get(),
        "subscribe": subscribe_var.get(),
        "rating": rating_var.get()
    }
    with open("form_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Saved:", data)

submit_btn = tk.Button(root, text="Submit", command=save_to_json)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10)
root.mainloop()
