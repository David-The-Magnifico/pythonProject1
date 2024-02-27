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

