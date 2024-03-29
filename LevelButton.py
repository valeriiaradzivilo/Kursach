import tkinter as tk

import funcs_logic
import regular_game
from CheckButton import CheckButton


class LevelButton(CheckButton):
    def __init__(self, level_name=None, amount_dots=0, amounts=[], plus_pos=0, window=None):
        self.level_name = level_name
        self.plus_pos = plus_pos
        self.amount_dots = amount_dots
        self.amounts = amounts
        self.window = window
        super().__init__(self)
        self['text'] = level_name
        # function that will check user input after user presses the button
        self['command'] = lambda: LevelButton.pressed(self)
        self.place(x=580, y=180 + self.plus_pos)

    def pressed(self):
        funcs_logic.generate_yel_dots(self.amount_dots)
        self.amounts.append(self.amount_dots)
        self.window.destroy()
        print("Level: ", self.level_name)
        regular_game.regular_game(create=[], replay=['n'], all_coords=[], amounts=self.amounts)

    def create_level_title(self):
        # text "Level" on right of the game
        tk.Label(
            text="Level",
            foreground="white",
            bg=self.window.bg_color,
            font=("Calibri Light", 25)
        ).place(
            x=615,
            y=150,
            anchor='center'
        )
