import tkinter as tk
def update_mouse_position(event):
    mouse_position_label.config(text=f"Mouse Position: {event.x}, {event.y}")
def on_left_click(event):
    mouse_click_label.config(text=f"Left Mouse Button Clicked")
def on_right_click(event):
    mouse_click_label.config(text=f"Right Mouse Button Clicked")

def main():
    root = tk.Tk()
    root.title("Mouse Event Tracker")
    root.geometry("400x400")
    global mouse_position_label
    mouse_position_label = tk.Label(root, text="Mouse Position: 0, 0",font=("Helvetica" , 16))
    mouse_position_label.pack(pady=20)
    global mouse_click_label
    mouse_click_label = tk.Label(root, text="No Mouse Button Clicked", font=("Helvetica", 16))
    mouse_click_label.pack(pady=20)
    root.bind('<Motion>', update_mouse_position)
    root.bind('<Button-1>', on_left_click)
    root.bind('<Button-3>', on_right_click)
    root.mainloop()
if __name__ == "__main__":
    main()