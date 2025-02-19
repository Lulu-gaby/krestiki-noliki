import tkinter as tk
from tkinter import messagebox
import random


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

player_wins = 0
computer_wins = 0

player_choice = None
computer_choice = None

def check_winner():
   for i in range(3):
       if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
           return True
       if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
           return True

   if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
       return True
   if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
       return True

   return False

def is_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True


def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]["text"] == ""]

    if empty_cells:
        row, col = random.choice(empty_cells)
        buttons[row][col]["text"] = computer_choice
        buttons[row][col].config(fg=O_COLOR if computer_choice == "0" else X_COLOR)

        if check_winner():
            global computer_wins
            computer_wins +=1
            messagebox.showinfo("Игра окончена", f"Компьютер ({computer_choice}) победил!")
            update_score()
            clear_all()
            return

        if is_draw():
            messagebox.showinfo("Игра окончена", "Ничья!")
            clear_all()


def on_click(row, col):
    global player_choice

    if buttons[row][col]['text'] != "" or player_choice is None:
        return

    buttons[row][col]['text'] = player_choice
    buttons[row][col].config(fg=X_COLOR if player_choice == "X" else O_COLOR)

    if check_winner():
        global player_wins
        player_wins += 1
        messagebox.showinfo("Игра окончена", f"Игрок ({player_choice}) победил!")
        update_score()
        clear_all()
        return

    if is_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        clear_all()
        return

    window.after(500, computer_move)


def clear_all():
    global player_choice, computer_choice
    player_choice = None
    computer_choice = None
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", fg="black")
    select_symbol_label.config(text="Выберите, за кого играть:")
    x_button.config(state="normal")
    o_button.config(state="normal")


def set_player_choice(symbol):
    global player_choice, computer_choice
    player_choice = symbol
    computer_choice = "0" if player_choice == "X" else "X"

    x_button.config(state="disabled")
    o_button.config(state="disabled")
    select_symbol_label.config(text=f"Вы играете за {player_choice}")

    if computer_choice == "X":
        window.after(500, computer_move)


def update_score():
    score_label.config(text=f"Игрок: {player_wins}  |  Компьютер: {computer_wins}")
    if player_wins == 3:
        messagebox.showinfo("Игра завершена", "Поздравляем! Игрок выиграл 3 раза!")
        reset_game()
    elif computer_wins == 3:
        messagebox.showinfo("Игра завершена", "Компьютер выиграл 3 раза!")
        reset_game()


def reset_game():
    global player_wins, computer_wins
    player_wins = 0
    computer_wins = 0
    update_score()
    clear_all()


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