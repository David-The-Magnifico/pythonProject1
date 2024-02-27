def __init__(self, title, body):
    self.id = Entry.nextId
    Entry.nextId += 1
    self.title = title
    self.body = body

def getId(self):
    return self.id

def setId(self, id):
    self.id = id

def getTitle(self):
    return self.title

def setTitle(self, title):
    self.title = title

def getBody(self):
    return self.body

def setBody(self, body):
    self.body = body
