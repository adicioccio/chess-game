from tkinter import *
from PIL import Image, ImageTk
import math


root = Tk()

w_bishop = PhotoImage(file=r"images/WB.png")
b_bishop = PhotoImage(file=r"images/BB.png")

tiles = {}


def setup_tiles():
    index = 1
    alternate = True
    for i in range(8):
        for j in range(8):
            color = ['#769656', '#eeeed2']
            inverse = ['1', '8', '7', '6', '5', '4', '3', '2', '1']
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            pos = f"{letters[math.floor((index/8)-0.01)]}{inverse[index%8]}"
            btn = Button(root, text=pos, bg=color[alternate], activebackground="white", image=b_bishop)
            btn.grid(column=i, row=j)
            tiles.setdefault(pos, btn)
            tiles[pos].config(command=lambda key=tiles[pos]: select_tile(key))
            if (index%8!=0):
                alternate=not alternate
            index+=1

def select_tile(key):
    text = key.cget('text')
    tiles[text].config(image=w_bishop)
    print(text)


def new():
    print("reset_board()")


setup_tiles()
main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="New", command=new)
root.geometry("528x528")
root.title("Chess Game - 0.0.0")
root.config(bg="#111111")
root.resizable(height=False, width=False)
root.mainloop()


