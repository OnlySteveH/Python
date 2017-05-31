class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        output = []
        for c in self.pattern:
            if c == '.':
                output.append('dot')
            elif c == '_':
                output.append('dash')
        return "-".join(output)

    @classmethod
    def from_string(cls, dotdash):
        output = []
        array = dotdash.split('-')
        for item in array:
            if item == 'dot':
                output.append('.')
            if item == 'dash':
                output.append('_')
        return cls(output)

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

