import tkinter as tk
from tkinter import *

window = Tk()
class Mspaint:
    def __init__(self, window):
        self.window = window
        self.window.title("MS Paint")
        self.window.geometry("800x450")
        self.window.resizable(TRUE, FALSE)
        self.window.configure(bg="grey")
        self.pen_color = "black"
        self.brush_size = 5
        self.pen_type = "line"
        self.brush_on = False
        self.eraser_on = False
        self.canvas = Canvas(self.window, bg="white", width=800, height=450)
        self.canvas.pack()
        self.x = None
        self.y = None


    def Create_buttons(self):
      self.button_frame = Frame(self.window)
      self.button_frame.pack(pady=20)
      self.pen_button = Button(self.button_frame, text="Pen", command=self.pen)
      self.pen_button.grid(row=0, column=0)
      self.brush_button = Button(self.button_frame, text="Brush", command=self.brush)
      self.brush_button.grid(row=0, column=1)
      self.color_button = Button(self.button_frame, text="Color", command=self.color)
      self.color_button.grid(row=0, column=2)
      self.eraser_button = Button(self.button_frame, text="Eraser", command=self.eraser)
      self.eraser_button.grid(row=0, column=3)
      self.size_button = Button(self.button_frame, text="Size", command=self.size)
      self.size_button.grid(row=0, column=4)