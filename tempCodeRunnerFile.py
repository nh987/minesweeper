def reveal_cell(buttons, btn, revealed, i, j):
    """
    Shows the revealed cell for the clicked button
    Input: 
        btn (tkinter.Button): the button that has been clicked
        revealed (list): a list of lists representing the revealed grid
        i, j (int): the integer coordinates of the button
    Returns:
        n/a
          
    """
    if revealed[i][j] == '':
        # pygame.mixer.Sound.play(pygame.mixer.Sound("assets/button.wav"))
        btn.config(text=revealed[i][j], relief=tk.SUNKEN, state=tk.DISABLED, bg='#e0e0e0')
        if j-1 >= 0:
            reveal_cell(buttons, buttons[i][j-1], revealed, i, j-1)
        if j+1 <= len(revealed)-1:
            reveal_cell(buttons, buttons[i][j+1], revealed, i, j+1)
        if i-1 >= 0:
            reveal_cell(buttons, buttons[i-1][j], revealed, i-1, j)
        if i+1 <= len(revealed)-1:
            reveal_cell(buttons, buttons[i+1][j], revealed, i+1, j)
        # k = 1
        # a = True
        # while a:
        #     if j-k >= 0:
        #         if revealed[i][j-k] == '':
        #             buttons[i][j-k].config(text=revealed[i][j-k], relief=tk.SUNKEN, state=tk.DISABLED, bg='#e0e0e0')
        #         elif type(revealed[i][j-k]) is int:
        #             a = False

        #     if j+k <= len(revealed)-1:
        #         if revealed[i][j+k] == '':
        #             buttons[i][j+k].config(text=revealed[i][j+k], relief=tk.SUNKEN, state=tk.DISABLED, bg='#e0e0e0')
        #         elif type(revealed[i][j+k]) is int:
        #             a = False

        #     if i-k >= 0:
        #         if revealed[i-k][j] == '':
        #             buttons[i-k][j].config(text=revealed[i-k][j], relief=tk.SUNKEN, state=tk.DISABLED, bg='#e0e0e0')
        #         elif type(revealed[i-k][j]) is int:
        #             a = False

        #     if i+k <= len(revealed)-1:
        #         if revealed[i+k][j] == '':
        #             buttons[i+k][j].config(text=revealed[i+k][j], relief=tk.SUNKEN, state=tk.DISABLED, bg='#e0e0e0')
        #         elif type(revealed[i+k][j]) is int:
        #             a = False
        #     k += 1
    if revealed[i][j] == '💣':
        pygame.mixer.Sound.play(pygame.mixer.Sound("assets/boom.wav"))
        btn.config(text=revealed[i][j], relief=tk.SUNKEN, state=tk.DISABLED, bg='#ff6459')
    elif type(revealed[i][j]) == int:
        pygame.mixer.Sound.play(pygame.mixer.Sound("assets/button.wav"))
        btn.config(text=revealed[i][j], relief=tk.SUNKEN, state=tk.DISABLED, bg='#e0e0e0')
        
    
    btn.update_idletasks()