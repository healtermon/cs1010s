##########################
# Game graphic interface #
##########################

from tkinter import *
from math import *

SIZE = 500
GRID_LEN = 4

GRID_PADDING = max(1, 20 // GRID_LEN)
WHITE_COLOR = "#ffffff"
BLACK_COLOR = "#000000"
BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {   2**1:"#eee4da", 2**2:"#ede0c8", 2**3:"#f2b179", 2**4:"#f59563", \
                            2**5:"#f67c5f", 2**6:"#f65e3b", 2**7:"#edcf72", 2**8:"#edcc61", \
                            2**9:"#edc850", 2**10:"#edc53f", 2**11:"#edc22e", 2**12:"#be98b5", \
                            2**13:"#b77dac", 2**14:"#ac63aa", 2**15:"#91018f", 2**16:"#710172", \
                            2**17:"#7a7ec7", 2**18:"#6c70ca", 2**19:"#5964c9", 2**20:"#4b5ace", \
                            2**21:"#3a4bcd", 2**22:"#7e7b76", 2**23:"#5f5c57", 2**24:"#4c4743", \
                            2**25:"#3f3e38", 2**26:"#363330", 2**27:"#2b2823", 2**28:"#1f1e1d", \
                            2**29:"#151412", 2**30:"#090809"}
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65" }
DEFAULT_CELL_COLOR = "#f9f6f2"
FONT = ("Verdana", max(1, 160 // GRID_LEN), "bold")
SCORE_FONT = ("Verdana", max(15, 80 // GRID_LEN), "bold")
DISPLAY_STR_DICT = {    '0':8304, '1':185, '2':178, '3':179, '4':8308, \
                        '5':8309, '6':8310, '7':8311, '8':8312, '9':8313 }

KEY_UP_ALT = "\'\\uf700\'"
KEY_DOWN_ALT = "\'\\uf701\'"
KEY_LEFT_ALT = "\'\\uf702\'"
KEY_RIGHT_ALT = "\'\\uf703\'"

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"
KEY_UNDO = "'z'"

def display(number):
    if number <= 1e4:
        return str(number)
    return "2" + "".join(list(map(lambda x: chr(DISPLAY_STR_DICT[x]), str(int(log2(number))))))

class GameGrid(Frame):
    
    def __init__(self, logic):
        Frame.__init__(self)
        self.l = logic
        self.win = False
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        self.commands = {   KEY_UP: self.l['up'],
                            KEY_DOWN: self.l['down'],
                            KEY_LEFT: self.l['left'],
                            KEY_RIGHT: self.l['right'],
                            KEY_UNDO: self.l['undo'], 
                            KEY_UP_ALT: self.l['up'],
                            KEY_DOWN_ALT: self.l['down'],
                            KEY_LEFT_ALT: self.l['left'],
                            KEY_RIGHT_ALT: self.l['right'] }
        self.grid_cells = []
        self.init_grid()
        self.init_score()
        self.game_state = self.l['make_new_game'](GRID_LEN)
        self.update_grid_cells()
        self.mainloop()
        
    def init_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        background.grid()

        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background,
                             bg=BACKGROUND_COLOR_CELL_EMPTY,
                             width=SIZE / GRID_LEN,
                             height=SIZE / GRID_LEN)
                
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text='', bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_score(self):
        score_container = Frame(self, width=SIZE, height=50)
        score_container.grid()

        score_label = Frame(score_container, bg=WHITE_COLOR, width=SIZE / 2, height=20)
        score_label.grid(row=0, column=0, columnspan=1, padx=GRID_PADDING, pady=GRID_PADDING)
        self.score_label = Label(master=score_label, text="Score ", bg=WHITE_COLOR, justify=RIGHT, font=SCORE_FONT, width=10, height=1)
        self.score_label.pack()

        score_text = Frame(score_container, bg=WHITE_COLOR, width=SIZE / 2, height=20)
        score_text.grid(row=0, column=1, columnspan=1, padx=GRID_PADDING, pady=GRID_PADDING)
        self.score_text = Label(master=score_text, text="0000", bg=WHITE_COLOR, justify=RIGHT, font=SCORE_FONT, width=10, height=1)
        self.score_text.pack()

    def update_grid_cells(self):
        current_score = self.l['get_score'](self.game_state)
        current_matrix = self.l['get_matrix'](self.game_state)
        self.score_text.configure(width=max(10, len(str(current_score))), text=str(current_score))
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = current_matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=display(new_number), bg=BACKGROUND_COLOR_DICT.get(new_number, BLACK_COLOR), fg=CELL_COLOR_DICT.get(new_number, DEFAULT_CELL_COLOR))
        self.update_idletasks()
       
    def key_down(self, event):
        def display_end_game(word1, word2):
            mid = GRID_LEN // 2
            if GRID_LEN % 2:
                self.grid_cells[mid][mid].configure(text=f'{word1}\n{word2}', bg=BACKGROUND_COLOR_CELL_EMPTY, fg=WHITE_COLOR)                
            else:
                self.grid_cells[1][mid - 1].configure(text=word1, bg=BACKGROUND_COLOR_CELL_EMPTY, fg=WHITE_COLOR)
                self.grid_cells[1][mid].configure(text=word2, bg=BACKGROUND_COLOR_CELL_EMPTY, fg=WHITE_COLOR)

        key = repr(event.char.lower())
        if key in self.commands:
            self.game_state, is_valid_move = self.commands[key](self.game_state)
            if is_valid_move:
                self.update_grid_cells()
                current_matrix = self.l['get_matrix'](self.game_state)
                current_status = self.l['game_status'](current_matrix)
                if current_status == "win" and not self.win:
                    display_end_game('You', 'Win?')
                    self.win = True
                if current_status == "lose":
                    display_end_game('You','Lose!')
