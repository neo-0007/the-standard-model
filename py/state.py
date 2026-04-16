'''
# Author:           Hrishikesh Gohain
# Filename:         state.py
# Description:      Mantains the state of application such as current level index
#                   and unlocked particles
# Functions:        get_current_index, set_current_index, add_unlocked,
#                   reset_unlocked, get_unlocked
# Global variables: current_index, unlocked
'''

# current_index: mantains the current index
current_index = 0

# unlocked: contains the ,list of all the unlocked particles
unlocked = set()


def get_current_index():
    '''
    Purpose:
    ---
    Returns the current level index.

    Input Arguments:
    ---
    None

    Returns:
    ---
    `current_index` : [int]
        Index of the current level

    Example call:
    ---
    get_current_index()
    '''
    return current_index


def set_current_index(value):
    '''
    Purpose:
    ---
    Sets the current level index

    Input Arguments:
    ---
    `value` : [int]
        New index value to be set

    Returns:
    ---
    None

    Example call:
    ---
    set_current_index(3)
    '''
    global current_index

    # Ensure index is not negative
    if value >= 0:
        current_index = value


def add_unlocked(particles):
    '''
    Purpose:
    ---
    Adds new particles to the unlocked set

    Input Arguments:
    ---
    `particles` : [list]
        List of particle identifiers to unlock

    Returns:
    ---
    None

    Example call:
    ---
    add_unlocked(["e", "u"])
    '''

    for p in particles:
        unlocked.add(p)


def reset_unlocked(levels, index):
    '''
    Purpose:
    ---
    Recomputes unlocked particles from scratch up to a given level index.

    Input Arguments:
    ---
    `levels` : [list]
        List of all Level objects

    `index` : [int]
        Current level index

    Returns:
    ---
    None

    Example call:
    ---
    reset_unlocked(levels, 3)
    '''

    unlocked.clear()

    for i in range(index + 1):
        for p in levels[i].unlock:
            unlocked.add(p)


def get_unlocked():
    '''
    Purpose:
    ---
    Returns the set of unlocked particles.

    Input Arguments:
    ---
    None

    Returns:
    ---
    `unlocked` : [set]
        Set of unlocked particle identifiers

    Example call:
    ---
    get_unlocked()
    '''

    return unlocked