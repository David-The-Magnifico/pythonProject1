
def addEntry(self, entry):
    self.entries.append(entry)

def findEntryById(self, id):
    for entry in self.entries:
        if entry.getId() == id:
            return entry
    return None

def deleteEntry(self, id):
    self.entries = [entry for entry in self.entries if entry.getId() != id]

def isLocked(self):
    return self.locked

def lockDiary(self):
    self.locked = True

def unlockDiary(self, password):
    if self.password == password:
        self.locked = False

