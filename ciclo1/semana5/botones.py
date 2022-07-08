import tkinter as tk
import time

root = tk.Tk()
root. title("my first window")
root.geometry("500x300")

my_button = tk.Button(root, text="Click me", command=lambda: print("Hello world"))
my_button2 = tk.Button(root, text="minimize", command=root.iconify)
my_button.pack()
my_button2.pack()
root.mainloop()
