import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("500x600")
window.config (background="papayawhip")

# Цветовая палитра
BG_COLOR = "papayawhip"
X_COLOR = "red1"
O_COLOR = "violetred4"


frame = tk.Frame(window, bg=BG_COLOR)
frame.place(relx=0.5, rely=0.4, anchor="center")

buttons = []

def on_click(row, col):
    pass

def clear_all():
    pass

def set_player_choice(symbol):
    pass

for i in range(3):
   row = []
   for j in range(3):
       btn = tk.Button(frame, text="", font=("Arial", 25), width=6, height=3, bg=BG_COLOR, command=lambda r=i, c=j: on_click(r, c))
       btn.grid(row=i, column=j,padx=5, pady=5)
       row.append(btn)
   buttons.append(row)


# Выбор символа
select_symbol_label = tk.Label(window, text="Выберите, за кого будете играть (Х или 0): ", font=("Arial", 10), bg="papayawhip")
select_symbol_label.place(relx=0.5, rely=0.84, anchor="center")

# Счет игры
score_label = tk.Label(window, text="Счет игры - Игрок: 0  |  Компьютер: 0", font=("Arial", 12), bg="papayawhip")
score_label.place(relx=0.5, rely=0.80, anchor="center")

# Фрейм для кнопок
button_frame = tk.Frame(window, bg="papayawhip")
button_frame.place(relx=0.5, rely=0.9, anchor="center")

#Кнопка выбора символа
x_button = tk.Button(button_frame, text="Играть за X", font=("Arial", 12), bg=X_COLOR, fg="white",
                     width=10, height=2, command=lambda: set_player_choice("X"))
x_button.grid(row=0, column=0, padx=10)

o_button = tk.Button(button_frame, text="Играть за 0", font=("Arial", 12), bg=O_COLOR, fg="white",
                     width=10, height=2, command=lambda: set_player_choice("0"))
o_button.grid(row=0, column=1, padx=10)

#Кнопка сброса
reset_button = tk.Button(button_frame, text="Сбросить", font=("Arial", 12), bg="lightcoral", fg="white",
                         command=clear_all, width=10, height=2)
reset_button.grid(row=0, column=2, padx=10)


window.mainloop()