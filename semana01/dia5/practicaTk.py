from curses import window
from tkinter import ttk 
from tkinter import *

class Product:
    def __init__(self,window):
        self.wind = window
        self.wind.title = "Product"

if __name__ == "__main__":
    window= Tk()
    application= Product()
    window.mainloop()