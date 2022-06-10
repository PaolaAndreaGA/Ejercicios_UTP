import tkinter as tk
import time

root = tk.Tk()
root. title("my first window")
root.geometry("500x300")

def imprimiendo():
    label1 = tk.Label(root, text="IMPRIMIENDO...")
    label1.pack()
    return ("i'm here")
my_button = tk.Button(root, text="IMPRIMIENDO", command=lambda: print("Hello world", imprimiendo()))
my_button2 = tk.Button(root, text="minimize", command=root.iconify)
my_button.pack()
my_button2.pack()
root.mainloop()