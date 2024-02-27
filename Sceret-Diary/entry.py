def __init__(self, title, body):
    self.id = Entry.nextId
    Entry.nextId += 1
    self.title = title
    self.body = body

def getId(self):
    return self.id

