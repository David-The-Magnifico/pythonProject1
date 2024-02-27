import tkinter as tk
from tkinter import messagebox

class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.entries = []

    def addEntry(self, entry):
        self.entries.append(entry)

    def findEntryById(self, id):
        for entry in self.entries:
            if entry.getId() == id:
                return entry
        return None

    def deleteEntry(self, id):
        self.entries = [entry for entry in self.entries if entry.getId() != id]

    def getEntries(self):
        return self.entries

class Entry:
    nextId = 1

    def __init__(self, title, body):
        self.id = Entry.nextId
        Entry.nextId += 1
        self.title = title
        self.body = body

    def getId(self):
        return self.id

root = tk.Tk()
root.title("Diary Application")

diary = None
entry = None

def create_diary():
    global diary
    username = username_entry.get()
    password = password_entry.get()
    diary = Diary(username, password)
    messagebox.showinfo("Success", "Diary created successfully.")

# Create GUI elements
