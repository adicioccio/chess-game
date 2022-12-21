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
dot = PhotoImage(file=r"images/DOT.png")

b_pieces = ['pyimage7', 'pyimage8', 'pyimage9', 'pyimage10', 'pyimage11', 'pyimage12']
w_pieces = ['pyimage1', 'pyimage2', 'pyimage3', 'pyimage4', 'pyimage5', 'pyimage6']

tiles = {}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


class Select:
    swap = ''
    image = None
    bg = ''
    moves = []
    moveImages = []
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
    tiles['b4'].config(image=bb)
    tiles['d4'].config(image=bb)


def legal_move(text, image):
    if image == 'pyimage6': # white pawn
        if text[1] == "2":
            num = int(text[1])
            if tiles[f'{text[0]}{num + 1}'].cget('image') == 'pyimage13':
                select.moves.append(f'{text[0]}{num + 1}')
                select.moveImages.append(tiles[f'{text[0]}{num + 1}'].cget('image'))
                tiles[f'{text[0]}{num + 1}'].config(image=dot)
            if tiles[f'{text[0]}{num + 2}'].cget('image') == 'pyimage13':
                select.moves.append(f'{text[0]}{num + 2}')
                select.moveImages.append(tiles[f'{text[0]}{num + 2}'].cget('image'))
                tiles[f'{text[0]}{num + 2}'].config(image=dot)
        else:
            num = int(text[1])
            if tiles[f'{text[0]}{num + 1}'].cget('image') == 'pyimage13':
                select.moves.append(f'{text[0]}{num + 1}')
                select.moveImages.append(tiles[f'{text[0]}{num + 1}'].cget('image'))
                tiles[f'{text[0]}{num + 1}'].config(image=dot)
        move1 = letters[letters.index(text[0])+1]+f'{num+1}'
        move2 = letters[letters.index(text[0])-1]+f'{num+1}'
        if tiles[move1].cget('image') in b_pieces:
            select.moves.append(move1)
            select.moveImages.append(tiles[move1].cget('image'))
        if tiles[move2].cget('image') in b_pieces:
            select.moves.append(move2)
            select.moveImages.append(tiles[move2].cget('image'))
            

def select_tile(key):
    text = key.cget('text')
    image = key.cget('image')
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
            legal_move(text, image)
    # after player selects first selection
    else:
        if text == select.swap:
            tiles[select.swap].config(bg=select.bg)
            for move in select.moves:
                tiles[move].config(image=empty)
            select.swap = ''
            select.moves.clear()
            select.moveImages.clear()
        if text in select.moves:
            tiles[text].config(image=select.image)
            tiles[select.swap].config(image=empty)
            tiles[select.swap].config(bg=select.bg)
            count = 0
            for move in select.moves:
                if move != text:
                    tiles[move].config(image=select.moveImages[count])
                count=count+1
            select.swap = ''
            select.moves.clear()
            select.moveImages.clear()


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


