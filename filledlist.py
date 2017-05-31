import copy

class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))

class Liar(list):
    def __len__(self, item):
        number = super().__len__(item)
        return number + 7