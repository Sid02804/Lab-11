# E22MCAG0023
# Siddhi Bhardwaj
from Duck import Duck
from fly_no_way import FlyNoWay
from Quack import Quack

class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())

    def display(self):
        print("I'm decoy duck")
