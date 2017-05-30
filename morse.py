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

class S(Letter):
    def __init__(self):
        pattern = ['.', '_', '.']
        super().__init__(pattern)

