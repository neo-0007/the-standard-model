'''
# Author:           Hrishikesh Gohain
# Filename:         data.py
# Description:      Creates level objects with data and contains particle names
# Functions:        get_level
# Global variables: levels, all_particles
'''

from models import Level

# levels: list containing Level objects used in the sidebar UI
levels = [
    Level("question", "The Question", "assets/slide1.png", "An curious mind"),
    Level("atom", "The Atom", "assets/slide2.png", "Building block of matter"),
    Level("nucleus", "Inside the Atom", "assets/slide3.png", "The atomic structure"),
    Level("electron", "The Electron", "assets/slide4.png", "First fundamental particle", ["e"]),
    Level("proton_neutron", "Protons & Neutrons", "assets/slide5.png", "Inside the nucleus", ["u", "d"]),
    Level("collision", "Collision of particles", "assets/slide6.png", "Lots of energy"),
    Level("new_particles", "New particles", "assets/slide7.png", "Short lived",["c", "t", "s", "b", "mu", "tau"]),
    Level("leptons", "The Neutrino", "assets/slide8.png", "And its relatives",["ve", "vmu", "vtau"]),
    Level("forces", "Forces of Nature", "assets/slide9.png", "Interaction of particles"),
    Level("four_forces", "Four Forces", "assets/slide10.png", "The fundamental forces of nature"),
    Level("photon", "Electromagnetism", "assets/slide11.png", "Photon", ["photon"]),
    Level("gluon", "Strong Nuclear Force", "assets/slide12.png", "Gluon", ["g"]),
    Level("bosons", "Weak Nuclear Force", "assets/slide13.png", "W & Z Bosons", ["z", "w"]),
    Level("mass", "What is Mass", "assets/slide14.png", "How particles have mass"),
    Level("big_discovery", "The Big Discovery", "assets/slide15.png", "Understanding mass"),
    Level("higgs", "The Higgs Boson", "assets/slide16.png", "The God Particle", ["h"]),
]

# all_particles: List of all the fundamental particles used in the standard model table
all_particles = [
    "u","c","t","d","s","b",
    "e","mu","tau",
    "ve","vmu","vtau",
    "g","photon","z","w","h"
]

def get_level(index):
    """
    Returns the level object using the given index.

    Args:
        index (int): Index of the level

    Returns:
        Level | None
    """
    return levels[index]