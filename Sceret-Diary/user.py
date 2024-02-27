class user: def init(self): self.secretDiary = None

def createDiary(self):
    self.secretDiary = Diary()
    self.secretDiary.lock()


