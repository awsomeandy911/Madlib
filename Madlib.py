# Program that prints out a madlib based on users input
# string concatenation (how to put strings together)
# used for randomizing madlib
from madlibs import LoveMadlib, SadMadlib, JobInterview, WackyAdventure
import random

if __name__ == "__main__":
    m = random.choice([LoveMadlib, SadMadlib, JobInterview, WackyAdventure])
    m.madlib()