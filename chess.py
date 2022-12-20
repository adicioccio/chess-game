from tkinter import *
from PIL import Image, ImageTk
import math


root = Tk()

wk = PhotoImage(file=r"images/WK.png")
wq = PhotoImage(file=r"images/WQ.png")
wr = PhotoImage(file=r"images/WR.png")
wb = PhotoImage(file=r"images/WB.png")
wh = PhotoImage(file=r"images/WH.png")
wp = PhotoImage(file=r"images/WP.png")
bk = PhotoImage(file=r"images/BK.png")
bq = PhotoImage(file=r"images/BQ.png")
br = PhotoImage(file=r"images/BR.png")
bb = PhotoImage(file=r"images/BB.png")
bh = PhotoImage(file=r"images/BH.png")
bp = PhotoImage(file=r"images/BP.png")
empty = PhotoImage(file=r"images/EMPTY.png")

tiles = {}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

class Select:
    swap = ''
    image = None
    bg = ''
select = Select()


def setup_tiles():
    index = 1
    alternate = True
    color = ['#769656', '#eeeed2']
    inverse = ['1', '8', '7', '6', '5', '4', '3', '2', '1']
    for i in range(8):
        for j in range(8):
            pos = f"{letters[math.floor((index/8)-0.01)]}{inverse[index%8]}"
            btn = Button(root, text=pos, bg=color[alternate], activebackground="white")
            btn.grid(column=i, row=j)
            tiles.setdefault(pos, btn)
            tiles[pos].config(command=lambda key=tiles[pos]: select_tile(key))
            if (index%8!=0):
                alternate=not alternate
            index+=1


def setup_pieces():
    for tile in tiles:
        tiles[tile].config(image=empty)
    b_setup = [['a8', br], ['b8', bh], ['c8', bb], ['d8', bq], ['e8', bk], ['f8', bb], ['g8', bh], ['h8', br]]
    w_setup = [['a1', wr], ['b1', wh], ['c1', wb], ['d1', wq], ['e1', wk], ['f1', wb], ['g1', wh], ['h1', wr]]
    for i in range(8):
        tiles[b_setup[i][0]].config(image=b_setup[i][1])
        tiles[w_setup[i][0]].config(image=w_setup[i][1])
    for i in range(8):
        tiles[f"{letters[i]}7"].config(image=bp)
        tiles[f"{letters[i]}2"].config(image=wp)


def select_tile(key):
    text = key.cget('text')
    image = key.cget('image')
    print(image)
    if select.swap == '':
        # player chose square thats empty
        if image == 'pyimage13':
            select.swap = ''
        # player chose square with piece
        else:
            select.swap = text
            select.image = image
            select.bg = key.cget('bg')
            tiles[text].config(bg='#E0CD66')
    # after player selects first selection
    else:
        if text == select.swap:
            tiles[select.swap].config(bg=select.bg)
        else:
            tiles[text].config(image=select.image)
            tiles[select.swap].config(image=empty)
            tiles[select.swap].config(bg=select.bg)
        select.swap = ''

def new():
    setup_pieces()
    if select.swap != '':
        tiles[select.swap].config(bg=select.bg)
        select.swap = ''


setup_tiles()
setup_pieces()

main_menu = Menu(root)
main_menu.add_command(label="New", command=new)
root.config(menu=main_menu)
root.geometry("528x528")
root.title("Chess Game - 0.0.0")
root.config(bg="#111111")
root.resizable(height=False, width=False)
root.mainloop()


