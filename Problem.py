class Problem:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.isSolved = False

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def isSolved(self):
        return self.isSolved

    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setSolved(self, isSolved):
        self.isSolved = isSolved

       def __str__(self):
        return f"Problem: {self.name}, Type: {self.type.name}, Status: {'Solved' if self.isSolved else 'Unsolved'}"
