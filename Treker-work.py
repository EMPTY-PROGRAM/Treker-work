from tkinter import *

window = Tk()
window.title("Мой трекер учебы")
window.state("zoomed")  # Максимизировать окно

# Можно добавить меню для управления
menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Выход", command=window.destroy)
menubar.add_cascade(label="Файл", menu=file_menu)

window.config(menu=menubar)


window.mainloop()