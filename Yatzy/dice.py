import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        is not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randInt(1, sides)
    
    def __int__(self):
        return self.value
    
    def __eq__(self, other):
        return int(self) == other
    
    def __ne__(self, other):
        return not int(self) == other
    
    def __gt__(self, other):
        return int(self) > other
    
    def __lt__(self, other):
        return int(self) < other
    
    def __ge__(self, other):
        return int(self) > other or int(self) == other
    
    def __le__(self, other):
        return int(self) < other or int(self) == other

    
class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
