'''
# Author:           Hrishikesh Gohain
# Filename:         controller.py
# Description:      Handles application logic and state transitions.
# Functions:        update, next_step, go_back
# Global variables: None
'''

from data import levels
from state import *
from state import unlocked as global_unlocked
from renderer import *


def update():
    '''
    Purpose:
    ---
    Updates the application state and refreshes the UI based on the current level.

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    update()
    '''
    
    level = levels[get_current_index()]

    add_unlocked(level.unlock)

    render_level()
    render_progress()
    render_progress_dots()
    render_standard_model()
    update_buttons()


def next_step():
    '''
    Purpose:
    ---
    Moves the application to the next level if not at the last level,
    and updates the UI accordingly.

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    next_step()
    '''
    
    index = get_current_index()

    if index < len(levels) - 1:
        set_current_index(index + 1)
        update()


def go_back():
    '''
    Purpose:
    ---
    Moves the application to the previous level if not at first level.
    Updates the unlocked particles up to the current level and updates the UI.

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    go_back()
    '''

    index = get_current_index()

    if index > 0:
        set_current_index(index - 1)

        unlocked = set()
        for i in range(get_current_index() + 1):
            for p in levels[i].unlock:
                unlocked.add(p)

        global_unlocked.clear()
        global_unlocked.update(unlocked)

        update()