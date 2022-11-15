class thing():
    pass


class example(thing):
    pass


class Thing2():
    def __init__(self, letters):
        self.letters = letters

    @property
    def name(self):
        return self.letters

    @name.setter
    def name(self, letters):
        self.letters = letters

class Thing3():
    def __init__(self, letters):
        self.letters = letters
    def get_name(self):
        print(self.letters)

th = Thing2('dsadas')
th.letters = 'fdsadfs'
print(th.letters)
