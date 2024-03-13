class user: 
    def init(self): self.secretDiary = None


class Diary:
    pass


def createDiary(self):
    self.secretDiary = Diary()
    self.secretDiary.lock()

def lockDiary(self):
    self.secretDiary.lock()

def unlockDiary(self):
    self.secretDiary.unlock()

def findEntryById(self, id):
    return self.secretDiary.findEntryById(id)

def addEntry(self, entry):
    self.secretDiary.addEntry(entry)

def updateEntry(self, entry):
    self.secretDiary.updateEntry(entry)

def deleteEntry(self, id):
    self.secretDiary.deleteEntry(id)
