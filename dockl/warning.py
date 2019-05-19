from tkinter import *
from tkinter import messagebox as me

class warn:
    def __init__(self,tex):
        self.text=tex
    def invalid_user(self):
        me.showerror("Error",self.text)