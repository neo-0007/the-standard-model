'''
# Author:           Hrishikesh Gohain
# Filename:         renderer.py
# Description:      Handles all UI rendering logic by using the DOM elements API
#                   basis of the current application state.
# Functions:        render_level, render_progress, render_progress_dots,
#                   render_standard_model, update_buttons
# Global variables: None
'''

from pyscript import document
from data import levels, all_particles
from state import get_current_index, get_unlocked


def render_level():
    '''
    Purpose:
    ---
    Updates the main content area with the current level's title and image.

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    render_level()
    '''

    level = levels[get_current_index()]
    document.getElementById("title").innerText = level.title
    img = document.getElementById("main-image")
    img.src = level.image


def render_progress():
    '''
    Purpose:
    ---
    Renders the left sidebar timeline showing all levels and highlights
    completed and active steps.

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    render_progress()
    '''
    container = document.getElementById("progress")
    container.innerHTML = ""

    current_index = get_current_index()

    for i, level in enumerate(levels):
        div = document.createElement("div")
        div.className = "step"

        # Mark completed and active steps
        if i < current_index:
            div.classList.add("completed")
        elif i == current_index:
            div.classList.add("active")

        circle = document.createElement("div")
        circle.className = "step-circle"

        content = document.createElement("div")
        content.className = "step-content"

        title = document.createElement("div")
        title.className = "step-title"
        title.innerText = level.title

        subtitle = document.createElement("div")
        subtitle.className = "step-subtitle"

        content.appendChild(title)

        subtitle.innerText = level.subtitle
        content.appendChild(subtitle)

        div.appendChild(circle)
        div.appendChild(content)
        container.appendChild(div)


def render_progress_dots():
    '''
    Purpose:
    ---
    Renders the progress indicator dots showing the user's position

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    render_progress_dots()
    '''

    container = document.getElementById("progress-dots")
    container.innerHTML = ""

    current_index = get_current_index()

    for i in range(len(levels)):
        dot = document.createElement("div")
        dot.className = "progress-dot"

        if i < current_index:
            dot.classList.add("completed")
        elif i == current_index:
            dot.classList.add("active")

        container.appendChild(dot)


def render_standard_model():
    '''
    Purpose:
    ---
    Updates the Standard Model table by marking unlocked particles as visible

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    render_standard_model()
    '''

    for particle_id in all_particles:
        el = document.getElementById(particle_id)

        if not el:
            continue

        # Show or hide particle based on unlocked state
        if particle_id in get_unlocked():
            if not el.classList.contains("visible"):
                el.classList.add("visible")
        else:
            el.classList.remove("visible")


def update_buttons():
    '''
    Purpose:
    ---
    Enables or disables navigation buttons based on the current index

    Input Arguments:
    ---
    None

    Returns:
    ---
    None

    Example call:
    ---
    update_buttons()
    '''

    back_btn = document.getElementById("back")
    next_btn = document.getElementById("next")

    index = get_current_index()

    # Disable back button at first level
    back_btn.disabled = (index == 0)

    # Disable next button at last level
    next_btn.disabled = (index >= len(levels) - 1)