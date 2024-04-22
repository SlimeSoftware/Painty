import tkinter as tk
import tkinter.ttk as ttk
import tkinter.colorchooser as colorchooser
from tkinter import filedialog
from PIL import Image, ImageTk

def start_paint(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def paint(event):
    global last_x, last_y
    x, y = event.x, event.y
    canvas.create_line(last_x, last_y, x, y, fill=brush_color, width=brush_size, capstyle=tk.ROUND, joinstyle=tk.ROUND)
    last_x, last_y = x, y

def clear_canvas():
    canvas.delete("all")

def change_color(new_color):
    global brush_color
    brush_color = new_color

def change_brush_size(new_size):
    global brush_size
    brush_size = new_size

def choose_custom_color():
    global brush_color
    new_color = colorchooser.askcolor()[1]
    if new_color:
        brush_color = new_color

def save_as_png():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        canvas.postscript(file=file_path + '.eps')  # Save as EPS first
        img = Image.open(file_path + '.eps')
        img.save(file_path)  # Convert EPS to PNG
        clear_canvas()

root = tk.Tk()
root.title("Painty")

frame_left = tk.Frame(root, bg="white")
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame_left, width=600, height=400, bg="white")
canvas.pack(expand=True, fill="both")
canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", paint)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, fill=tk.Y)

clear_button = ttk.Button(frame_right, text="Clear Canvas", command=clear_canvas)
clear_button.pack(pady=5)

colors_frame = ttk.LabelFrame(frame_right, text="Colors", padding=5)
colors_frame.pack(pady=5)

colors = ["black", "red", "blue", "green", "orange", "yellow"]

for color in colors:
    color_image = Image.new('RGB', (20, 20), color)
    color_photo = ImageTk.PhotoImage(color_image)
    color_button = ttk.Button(colors_frame, image=color_photo, command=lambda c=color: change_color(c))
    color_button.image = color_photo
    color_button.pack(side="left", padx=2)

size_frame = ttk.LabelFrame(frame_right, text="Brush Size", padding=5)
size_frame.pack(pady=5)

brush_sizes = [2, 4, 6, 8, 10]
for size in brush_sizes:
    size_button = ttk.Button(size_frame, text=str(size), width=2, command=lambda s=size: change_brush_size(s))
    size_button.pack(side="left", padx=2)

custom_color_button = ttk.Button(frame_right, text="Custom Color", command=choose_custom_color)
custom_color_button.pack(pady=5)

save_button = ttk.Button(frame_right, text="Save as PNG", command=save_as_png)
save_button.pack(pady=5)


brush_color = "black"
brush_size = 4

last_x, last_y = None, None

root.mainloop()
