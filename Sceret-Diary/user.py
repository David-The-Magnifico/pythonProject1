class user: def init(self): self.secretDiary = None

def createDiary(self):
    self.secretDiary = Diary()
    self.secretDiary.lock()

def lockDiary(self):
    self.secretDiary.lock()

def unlockDiary(self):
    self.secretDiary.unlock()

