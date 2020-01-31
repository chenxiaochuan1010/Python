from random import randint

class Die():
    """A basic model of a multiple-sided die"""

    def __init__(self, side=6):
        """Initialize the die"""
        self.side = side

    def roll_die(self):
        """Act as rolling of a die and print out the result."""
        if self.side >= 3:
            num = randint(1, self.side)
            print("\nResult (%i-sided): %i " % (self.side, num))
        else:
            print("\nToo less sides. Sides number must be larger than 3!")

six_sided_die = Die()
six_sided_die.roll_die()

ten_sided_die = Die(10)
ten_sided_die.roll_die()

twenty_sided_die = Die(20)
twenty_sided_die.roll_die()

two_sided_die = Die(2)
two_sided_die.roll_die()
