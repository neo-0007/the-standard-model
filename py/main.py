'''
# Author List:      Hrishikesh_Gohain
# Filename:         main.py
# File Description: This is the root python file used by the index.html
                    Entry point for the PyScript application
'''

from pyscript import when, document
from controller import next_step, go_back, update

@when("click", "#next")
def handle_next(event):
    next_step()

@when("click", "#back")
def handle_back(event):
    go_back()

@when("keydown", document)
def handle_keyboard(event):
    if event.key == "ArrowRight":
        next_step()
    elif event.key == "ArrowLeft":
        go_back()

update()