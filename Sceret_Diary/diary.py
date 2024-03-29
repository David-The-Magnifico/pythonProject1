
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

def getUsername(self):
    return self.username

def setUsername(self, username):
    self.username = username

def getPassword(self):
    return self.password

def setPassword(self, password):
    self.password = password

def getEntries(self):
    return self.entries

@staticmethod
def findDiaryByUsername(username):
    for diary in Diary.getAllDiaries():
        if diary.getUsername() == username:
            return diary
    return None

@staticmethod
def deleteDiary(username):
    diary = Diary.findDiaryByUsername(username)
    if diary:
        diary.setEntries([])

def setEntries(self, entries):
    self.entries = entries

@staticmethod
def getAllDiaries():
    diaries = []
    for diary in diaries:
        if diary.getUsername():
            diaries.append(diary)
    return diaries

def lock(self):
    return None

def unlock(self):
    return None

def updateEntry(self, entry):
    for i in range(len(self.entries)):
        if self.entries[i].getId() == entry.getId():
            self.entries[i] = entry


