import random

from characters import Character


class Thief(Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))