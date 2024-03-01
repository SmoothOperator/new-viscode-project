import tkinter as tk
from tkinter import ttk

# Function to update the label with the slider value
def update_value(slider, label):
    value = f"{slider.get():.0f}"  # Get the current value of the slider
    label.config(text=value)  # Update the label with the current value

root = tk.Tk()
root.title("Stylized Resume")

# CAD Skills Slider
cad_label = tk.Label(root, text="CAD Skills")
cad_label.pack()
cad_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal")
cad_slider.pack()
cad_value_label = tk.Label(root, text="0")
cad_value_label.pack()
cad_slider.bind("<Motion>", lambda event: update_value(cad_slider, cad_value_label))

# Programming Skills Slider
programming_label = tk.Label(root, text="Programming Skills")
programming_label.pack()
programming_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal")
programming_slider.pack()
programming_value_label = tk.Label(root, text="0")
programming_value_label.pack()
programming_slider.bind("<Motion>", lambda event: update_value(programming_slider, programming_value_label))

# Design Skills Slider
design_label = tk.Label(root, text="Design Skills")
design_label.pack()
design_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal")
design_slider.pack()
design_value_label = tk.Label(root, text="0")
design_value_label.pack()
design_slider.bind("<Motion>", lambda event: update_value(design_slider, design_value_label))

root.mainloop()
