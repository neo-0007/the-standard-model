'''
# Author:           Hrishikesh_Gohain
# Filename:         main.py
# Description:      Entry point for the PyScript application.
#                   Handles user button interactions and initializes the UI.
# Functions:        handle_next, handle_back, handle_keyboard, init_app
# Global variables: None
'''

from pyscript import when, document
from controller import next_step, go_back, update


@when("click", "#next")
def handle_next(event):
    '''
    Purpose:
    ---
    Handles click for the "Next" button and moves to the next level.

    Input Arguments:
    ---
    `event` : [object]
        Click event triggered by the user

    Returns:
    ---
    None

    Example call:
    ---
    Triggered automatically on button click
    '''
    next_step()


@when("click", "#back")
def handle_back(event):
    '''
    Purpose:
    ---
    Handles click event for the "Previous" button and moves to the previous level.

    Input Arguments:
    ---
    `event` : [object]
        Click event triggered by the user

    Returns:
    ---
    None

    Example call:
    ---
    Triggered automatically on button click
    '''
    go_back()


@when("keydown", document)
def handle_keyboard(event):
    '''
    Purpose:
    ---
    Handles keyboard navigation using arrow keys.

    Input Arguments:
    ---
    `event` : [object]
        Keyboard event triggered by the user

    Returns:
    ---
    None

    Example call:
    ---
    Triggered automatically on key press
    '''

    if event.key == "ArrowRight":
        next_step()
    elif event.key == "ArrowLeft":
        go_back()


def init_app():
    '''
    Purpose:
    ---
    Initializes the application by rendering the initial UI state
    and handling the loading screen logic.

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    init_app()
    '''

    # Render initial state
    update()

    # Show application UI
    document.getElementById("app").style.display = "block"

    # Hide loading screen
    document.getElementById("loader").style.display = "none"


# Initialize application
init_app()