from random import randint

import funcs_logic
import funcs_interface

from WindowMaker import WindowMaker
from AnswerButton import AnswerButton
from ExitButton import ExitButton
from SolveButton import SolveButton
from CheckButton import CheckButton
from RulesButton import RulesButton
from CreateTask import CreateTask
from LevelButton import LevelButton


def regular_game(create=[], replay=[], all_coords=[], amounts=[]):
    game_rules = "Rules:\nLerogram is a logic game on a field of 15x15 cells for one player.\nThere are numbers on " \
                 "the left, right, bottom, and top.\nThe numbers on the left and top indicate which the longest block " \
                 "of black\ncells is present in this row or column.\nSimilarly, the numbers on the right and bottom " \
                 "indicate which the longest\nblock of yellow cells is present in a given column or row.\nThere may be " \
                 "several such blocks, but the length of none of them should not exceed the maximum value.\nThere " \
                 "must also be a block equal in length to this value.\nIf the player does not exceed the maximum " \
                 "length in all blocks – he wins,\nif not – loses. To check the correctness of the input,you need to " \
                 "click 'Check'.\nAnd to get a hint – 'Answer'.\nIf the task is too difficult, the computer can solve " \
                 "it " \
                 "for you.\nTo do this, simply press the 'Solve' button.\nTo close the game, you need to click on the " \
                 "red button with a cross\nnext to the title.If you try to exit the game in the usual way -\nthe game " \
                 "will reboot." \
                 "There is also a possibility to choose level using buttons on the right.\n" \
                 "\nIf you want to create your own task - click 'Create Task'.\nMake sure to completely fill the " \
                 "field.\nGood luck : ) \n" \
                 "About:\nMade by Radzivilo Valeriia IP-14 2022 "
    game_name = "Lerogram"  # title
    bg_color = '#0049b8'  # game's background color
    # create main window with the game
    main_window = WindowMaker(game_name, bg_color, replay)
    # levels
    LevelButton("Easy", randint(1, 20), amounts, 0, main_window).create_level_title()
    LevelButton("Medium", randint(190, 220), amounts, 50, main_window)
    LevelButton("Hard", randint(100, 200), amounts, 100, main_window)
    # button to quit game
    ExitButton(main_window)
    # button to open the rules
    RulesButton(game_rules, bg_color)
    # make label bg and rules sections
    funcs_interface.make_window_label_board(main_window)
    # make black and yellow boxes in the corners
    funcs_interface.make_two_color_boxes()
    # button for user to create personal task
    CreateTask(main_window, bg_color, all_coords, create, main_window)
    # if level is not chosen
    if not amounts:
        print("Level: Random")
        amounts.append(randint(10, 220))
    # if user did not choose CreateTask - the task will be random
    if not create or create.pop() != 1:
        print("Random:")
        # generate yellow dots in amount of random range
        yel_dots = funcs_logic.generate_yel_dots(amounts.pop())
    else:
        if len(all_coords) == 225:
            print("Created:")
            yel_dots = funcs_logic.take_yels(all_coords)
            print(yel_dots)
        else:
            print("Random:")
            # generate yellow dots in amount of random range
            yel_dots = funcs_logic.generate_yel_dots(amounts.pop())
    # solution to any task
    funcs_logic.print_answer(yel_dots)
    # depending on the placement of yellow dots count maximum amounts for boxes
    bl_horiz, yel_horiz = funcs_logic.find_max_hor(yel_dots)
    bl_vert, yel_vert = funcs_logic.find_max_vert(yel_dots)
    # create vertical and horizontal lines of numbers
    funcs_interface.make_num_horiz_board(bl_horiz, yel_horiz)
    funcs_interface.make_num_vert_board(bl_vert, yel_vert)
    # create field with buttons
    all_coords.clear()
    funcs_interface.create_button_field(all_coords)
    # work with an array all_coords
    # create the right answer
    right_answer = funcs_logic.right_answer(yel_dots)
    # button to solve task
    SolveButton(all_coords, right_answer, main_window)
    # button to check user input
    CheckButton(all_coords, bl_horiz, yel_horiz, bl_vert, yel_vert, main_window)
    # button to show right answer
    AnswerButton(yel_dots)
    if replay and replay.pop() == 'n':
        main_window.destroy()
    # if the answer is correct right_answer window will appear
    # otherwise fail_window

    main_window.mainloop()


