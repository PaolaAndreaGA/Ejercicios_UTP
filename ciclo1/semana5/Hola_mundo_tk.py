import tkinter as tk


mi_window = tk.Tk()
mi_window.title("Hola mundo")
mi_window.geometry("500x500")
texto = tk.Label(mi_window, text="HOLA MUNDO, AQUI ESTOY")
texto.pack()

mi_window.mainloop()


