import tkinter as tk
from tkinter import messagebox

class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.entries = []

