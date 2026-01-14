import tkinter as tk
from tkinter import messagebox
import math

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Tic Tac Toe AI")
root.geometry("360x480")
root.config(bg="#0f1222")
root.resizable(False, False)

board = [' ' for _ in range(9)]
buttons = []

# 🌈 BRIGHT COLORS
PLAYER_COLOR = "#ff2e88"   # Neon Pink ❌
AI_COLOR = "#00ff9c"       # Neon Green ⭕
BTN_BG = "#1a1d3a"
BTN_HOVER = "#272b5c"
GRID_COLOR = "#3a3f7a"

# ---------------- GAME LOGIC ----------------
def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in w) for w in wins)

def is_draw():
    return ' ' not in board

def minimax(is_max):
    if check_winner('O'): return 1
    if check_winner('X'): return -1
    if is_draw(): return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'
    buttons[move].config(
        text='O',
        fg=AI_COLOR,
        state='disabled'
    )

def on_click(i):
    if board[i] == ' ':
        board[i] = 'X'
        buttons[i].config(
            text='X',
            fg=PLAYER_COLOR,
            state='disabled'
        )

        if check_winner('X'):
            messagebox.showinfo("Game Over", "🎉 You Win!")
            reset()
            return

        if is_draw():
            messagebox.showinfo("Game Over", "🤝 Draw!")
            reset()
            return

        ai_move()

        if check_winner('O'):
            messagebox.showinfo("Game Over", "🤖 AI Wins!")
            reset()
        elif is_draw():
            messagebox.showinfo("Game Over", "🤝 Draw!")
            reset()

def reset():
    global board
    board = [' ' for _ in range(9)]
    for btn in buttons:
        btn.config(
            text=' ',
            fg="white",
            state='normal',
            bg=BTN_BG
        )

# ---------------- UI ----------------
title = tk.Label(
    root,
    text="TIC TAC TOE AI",
    font=("Segoe UI", 24, "bold"),
    fg="#ffffff",
    bg="#0f1222"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Neon Human ❌ vs AI ⭕",
    font=("Segoe UI", 11),
    fg="#aab0ff",
    bg="#0f1222"
)
subtitle.pack(pady=5)

frame = tk.Frame(root, bg="#0f1222")
frame.pack(pady=10)

def on_enter(e):
    if e.widget['state'] == 'normal':
        e.widget['bg'] = BTN_HOVER

def on_leave(e):
    if e.widget['state'] == 'normal':
        e.widget['bg'] = BTN_BG

for i in range(9):
    btn = tk.Button(
        frame,
        text=' ',
        font=("Segoe UI", 22, "bold"),
        width=5,
        height=2,
        bg=BTN_BG,
        fg="white",
        activebackground=BTN_HOVER,
        relief="flat",
        highlightbackground=GRID_COLOR,
        highlightthickness=1,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i//3, column=i%3, padx=6, pady=6)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    buttons.append(btn)

reset_btn = tk.Button(
    root,
    text="RESET GAME",
    font=("Segoe UI", 12, "bold"),
    bg="#ffd166",
    fg="#000000",
    relief="flat",
    command=reset
)
reset_btn.pack(pady=15)

root.mainloop()


