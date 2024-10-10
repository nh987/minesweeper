# Minesweeper solver
import random
import copy
import tkinter as tk
from tkinter import font
import pygame

def create_grid(size):
    """
    Creates the game board, and allocates bombs randomly

    Input: 
        size (int): the size of the grid (n x n)
    Returns:
        grid (list): a list of lists representing the grid the player will see
        revealed (list): a list of lists representing the revealed grid
    """
    grid = []
    for i in range(size):
        row = []
        rdm = random.randint(0,size)
        for j in range(size):
            row.append('')
        grid.append(row)
    cells = expand_grid(size,grid)
    mine_pos = random.sample(cells, 10)
    revealed = copy.deepcopy(grid)
    for (i,j) in mine_pos:
        revealed[i][j] = '💣'
    calc_cell_num(grid, revealed, size)
    return grid, revealed

def calc_cell_num(grid, revealed, size):
    """
    Calculates the number of mines close to a cell, within one cell's distance in any direction

    Input: 
        grid (list): a list of lists representing the grid the player will see
        revealed (list): a list of lists representing the revealed grid
        size (int): the size of the grid (n x n)
    Returns:
        n/a

    """
    for i in range(len(revealed)):
        for j in range(len(revealed[i])):
            if revealed[i][j] == '💣':
                if i > 0:
                    # top of mine
                    if revealed[i-1][j] != '💣' and type(revealed[i-1][j]) == int:
                        revealed[i-1][j] += 1
                    else:
                        revealed[i-1][j] = 1
                if i < size-1:
                    # bottom of mine
                    if revealed[i+1][j] != '💣' and type(revealed[i+1][j]) == int:
                        revealed[i+1][j] += 1
                    else:
                        revealed[i+1][j] = 1
                if j > 0:
                    # left of mine
                    if revealed[i][j-1] != '💣' and type(revealed[i][j-1]) == int:
                        revealed[i][j-1] += 1
                    else:
                        revealed[i][j-1] = 1
                if j < size-1:
                    # right of mine
                    if revealed[i][j+1] != '💣' and type(revealed[i][j+1]) == int:
                        revealed[i][j+1] += 1
                    else:
                        revealed[i][j+1] = 1
                if i > 0 and j > 0:
                    # top left of mine
                    if revealed[i-1][j-1] != '💣' and type(revealed[i-1][j-1]) == int:
                        revealed[i-1][j-1] += 1
                    else:
                        revealed[i-1][j-1] = 1
                if i > 0 and j < size-1:
                    # top right of mine
                    if revealed[i-1][j+1] != '💣' and type(revealed[i-1][j+1]) == int:
                        revealed[i-1][j+1] += 1
                    else:
                        revealed[i-1][j+1] = 1
                if i < size-1 and j > 0:
                    # bottom left of mine
                    if revealed[i+1][j-1] != '💣' and type(revealed[i+1][j-1]) == int:
                        revealed[i+1][j-1] += 1
                    else:
                        revealed[i+1][j-1] = 1
                if i < size-1 and j < size-1:
                    # bottom right of mine
                    if revealed[i+1][j+1] != '💣' and type(revealed[i+1][j+1]) == int:
                        revealed[i+1][j+1] += 1
                    else:
                        revealed[i+1][j+1] = 1

def expand_grid(size, grid):
    """
    Expands the grid into just cells, so they can be accessed
    Input: 
        size (int): the size of the grid (n x n)
        grid (list): a list of lists representing the grid the player will see
    Returns:
        expanded (list): a list of tuples representing each cell in the grid
          
    """
    expanded = [(i,j) for i in range(size) for j in range(size)]
    return expanded

def display_grid(grid):
    """
    Displays the grid line by line in a clean way, no commas or brackets surrounding the board
    Input: 
        grid (list): a list of lists representing the grid the player will see
    Returns:
        n/a
          
    """
    for i in range(len(grid)):
        print(grid[i])

def create_gui(grid, revealed):
    """
    Creates the gui for the game with clickable buttons, starts the game loop
    Input: 
        grid (list): a list of lists representing the grid the player will see
        revealed (list): a list of lists representing the revealed grid
    Returns:
        n/a
          
    """
    pygame.init()
    root = tk.Tk()
    root.title("Minesweeper")
    root.iconbitmap('assets/spong.ico')

    custom_font = font.Font(family="Helvetica", size=12, weight="bold")

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            btn = tk.Button(root, text=grid[i][j], width=2, height=1, font=custom_font)
            btn.grid(row=i, column=j)
            btn.config(command=lambda btn=btn, i=i, j=j: reveal_cell(btn, revealed, i, j))
            btn.bind("<Button-3>", lambda event, btn=btn: right_click(btn, i, j))
    
    root.mainloop()

def reveal_cell(btn, revealed, i, j):
    """
    Shows the revealed cell for the clicked button
    Input: 
        btn (tkinter.Button): the button that has been clicked
        revealed (list): a list of lists representing the revealed grid
        i, j (int): the integer coordinates of the button
    Returns:
        n/a
          
    """
    if revealed[i][j] == '💣':
        pygame.mixer.Sound.play(pygame.mixer.Sound("assets/boom.wav"))
        btn.config(text=revealed[i][j], relief=tk.SUNKEN, state=tk.DISABLED, bg='#ff6459')
    else:
        pygame.mixer.Sound.play(pygame.mixer.Sound("assets/button.wav"))
        btn.config(text=revealed[i][j], relief=tk.SUNKEN, state=tk.DISABLED, bg='#e0e0e0')
    btn.update_idletasks()

def right_click(btn, i, j):
    """
    Right clicking places a flag on an unclicked button, marking it and rendering it unclickable
    Input: 
        btn (tkinter.Button): the button that has been clicked
        i, j (int): the integer coordinates of the button
    Returns:
        n/a
    """
    if btn.cget("text") == "⚑":
        btn.config(text="", state=tk.NORMAL)
    elif btn.cget("text") == '' and btn.cget("relief") != "sunken":
        btn.config(text="⚑", state=tk.DISABLED)

size = 8
grid, revealed = create_grid(size)
create_gui(grid, revealed)
