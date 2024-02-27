
def addEntry(self, entry):
    self.entries.append(entry)

def findEntryById(self, id):
    for entry in self.entries:
        if entry.getId() == id:
            return entry
    return None

