import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe!")

current_player = "X"

board = [" " for _ in range(9)]

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return True
    return False

def check_tie():
    return " " not in board

def handle_click(index):
    global current_player

    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} Won!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Game Over", "Draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player
    board = [" " for _ in range(9)] 
    current_player = "X"             
    
    for button in buttons:           
        button.config(text="")

def handle_click(index):
    global current_player

    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} Won!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Game Over", "Draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"


buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: handle_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()



