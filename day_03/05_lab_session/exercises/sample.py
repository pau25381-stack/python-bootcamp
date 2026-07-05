import tkinter as tk
import json

root = tk.Tk()
root.title("Forms")
root.geometry("400x300")

# Variables
name_var = tk.StringVar()
age_var = tk.StringVar()
theme_var = tk.StringVar()
subscribe_var = tk.BooleanVar()
rating_var = tk.IntVar()

# Widgets with grid layout
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Theme:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root, textvariable=theme_var).grid(row=2, column=1, padx=5, pady=5)

tk.Checkbutton(root, text="Subscribe", variable=subscribe_var).grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)

tk.Label(root, text="Rating (1–5):").grid(row=4, column=0, sticky="w", padx=5, pady=5)
tk.Spinbox(root, from_=1, to=5, textvariable=rating_var).grid(row=4, column=1, padx=5, pady=5)

# Function to save values
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

# Submit button
tk.Button(root, text="Submit", command=save_to_json).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
