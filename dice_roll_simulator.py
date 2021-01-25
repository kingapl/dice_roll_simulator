import tkinter as tk
from PIL import ImageTk, Image

from random import choice

dice = ["images/dice1.png", "images/dice2.png", "images/dice3.png", 
        "images/dice4.png", "images/dice5.png", "images/dice6.png"]

class DiceRollSimulator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.geometry("600x400")
        master.title("Dice Roll Simulator")

        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.text_label = tk.Label(self, text="Hello, roll the dice!", 
                                font="Arial 24 bold", pady=20, fg="#991006")
        self.text_label.pack(side="top")

        self.roll_the_dice = tk.Button(self, text="Roll the dice", command=self.dice_roll)
        self.roll_the_dice.pack()
        self.label = tk.Label(self, image="")


    def dice_roll(self):
        die = choice(dice)

        self.original = Image.open(die) # 640x628
        resized = self.original.resize((320, 314), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        #self.label = tk.Label(self, image=self.image)
        self.label.config(image=self.image)
        self.label.pack()


root = tk.Tk()
dice_roll_simulator = DiceRollSimulator(master=root)
dice_roll_simulator.mainloop()