'''
# Author:           Hrishikesh Gohain
# Filename:         models.py
# Description:      Defines data models used in the application
# Functions:        None
# Global variables: None
'''

class Level:
    """
    Represents a single level shown in the UI

    Attributes:
        id (str): Unique identifier for the level
        title (str): Title displayed in UI
        image (str): Path to the image slide
        subtitle (str): Description of the level
        unlock (list): List of particles unlocked at this level
    """

    def __init__(self, id, title, image=None, subtitle="", unlock=None):
        self.id = id
        self.title = title
        self.image = image
        self.subtitle = subtitle
        self.unlock = unlock or []