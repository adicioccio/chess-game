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


# helper class to have volatile variables
class Select:
    turn = True
    loc = ''
    image = None
    bg = ''
    moves = []
    moveImages = []

select = Select()


# create the grid of tiles with alternating colors
def setup_tiles():
    index = 1
    alternate = True
    color = ['#769656', '#eeeed2']
    inverse = ['1', '8', '7', '6', '5', '4', '3', '2', '1']
    for i in range(8):
        for j in range(8):
            pos = f"{letters[math.floor((index / 8) - 0.01)]}{inverse[index % 8]}"
            btn = Button(root, text=pos, bg=color[alternate], activebackground="white")
            btn.grid(column=i, row=j)
            tiles.setdefault(pos, btn)
            tiles[pos].config(command=lambda key=tiles[pos]: select_tile(key))
            if (index % 8 != 0):
                alternate = not alternate
            index += 1


# setting pieces on start
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
    tiles['e4'].config(image=wb)
    tiles['a3'].config(image=bb)


# helper function for rooks, bishops and queens
def tile_checker(tile, piece, image):
    if piece == 'pyimage13':
        select.moves.append(tile)
        select.moveImages.append(piece)
        tiles[tile].config(image=dot)
        return 0
    elif (image in w_pieces and piece in w_pieces) or (image in b_pieces and piece in b_pieces):
        return 1
    else:
        select.moves.append(tile)
        select.moveImages.append(piece)
        return 1


# append legal moves based on piece selected
def legal_move(text, image):
    if image == 'pyimage6':  # white pawn
        if text[1] == "2":
            num = int(text[1])
            blocking = False
            if tiles[f'{text[0]}{num + 1}'].cget('image') == 'pyimage13':
                select.moves.append(f'{text[0]}{num + 1}')
                select.moveImages.append(tiles[f'{text[0]}{num + 1}'].cget('image'))
                tiles[f'{text[0]}{num + 1}'].config(image=dot)
            elif tiles[f'{text[0]}{num + 1}'].cget('image') in w_pieces+b_pieces:
                blocking = True
            if tiles[f'{text[0]}{num + 2}'].cget('image') == 'pyimage13' and not blocking:
                select.moves.append(f'{text[0]}{num + 2}')
                select.moveImages.append(tiles[f'{text[0]}{num + 2}'].cget('image'))
                tiles[f'{text[0]}{num + 2}'].config(image=dot)
        else:
            num = int(text[1])
            if tiles[f'{text[0]}{num + 1}'].cget('image') == 'pyimage13':
                select.moves.append(f'{text[0]}{num + 1}')
                select.moveImages.append(tiles[f'{text[0]}{num + 1}'].cget('image'))
                tiles[f'{text[0]}{num + 1}'].config(image=dot)
        try:
            move1 = letters[letters.index(text[0]) + 1] + f'{num + 1}'
            if tiles[move1].cget('image') in b_pieces:
                select.moves.append(move1)
                select.moveImages.append(tiles[move1].cget('image'))
        except:
            move1 = 'a0'
        try:
            move2 = letters[letters.index(text[0]) - 1] + f'{num + 1}'
            if tiles[move2].cget('image') in b_pieces:
                select.moves.append(move2)
                select.moveImages.append(tiles[move2].cget('image'))
        except:
            move2 = 'a0'
    if image == 'pyimage12':  # black pawn
        if text[1] == "7":
            num = int(text[1])
            blocking = False
            if tiles[f'{text[0]}{num - 1}'].cget('image') == 'pyimage13':
                select.moves.append(f'{text[0]}{num - 1}')
                select.moveImages.append(tiles[f'{text[0]}{num - 1}'].cget('image'))
                tiles[f'{text[0]}{num - 1}'].config(image=dot)
            elif tiles[f'{text[0]}{num - 1}'].cget('image') in w_pieces+b_pieces:
                blocking = True
            if tiles[f'{text[0]}{num - 2}'].cget('image') == 'pyimage13' and not blocking:
                select.moves.append(f'{text[0]}{num - 2}')
                select.moveImages.append(tiles[f'{text[0]}{num - 2}'].cget('image'))
                tiles[f'{text[0]}{num - 2}'].config(image=dot)
        else:
            num = int(text[1])
            if tiles[f'{text[0]}{num - 1}'].cget('image') == 'pyimage13':
                select.moves.append(f'{text[0]}{num - 1}')
                select.moveImages.append(tiles[f'{text[0]}{num - 1}'].cget('image'))
                tiles[f'{text[0]}{num - 1}'].config(image=dot)
        try:
            move1 = letters[letters.index(text[0]) + 1] + f'{num - 1}'
            if tiles[move1].cget('image') in w_pieces:
                select.moves.append(move1)
                select.moveImages.append(tiles[move1].cget('image'))
        except:
            move1 = 'a0'
        try:
            move2 = letters[letters.index(text[0]) - 1] + f'{num - 1}'
            if tiles[move2].cget('image') in w_pieces:
                select.moves.append(move2)
                select.moveImages.append(tiles[move2].cget('image'))
        except:
            move2 = 'a0'
    if image == 'pyimage3' or image == 'pyimage9': # rooks
        for i in range(8-int(text[1])): # up
            tile = f"{text[0]}{i+int(text[1])+1}"
            piece = tiles[tile].cget('image')
            if tile_checker(tile, piece, image) == 1:
                break
        for i in range(int(text[1])-1, 0, -1): # down
            tile = f"{text[0]}{i}"
            piece = tiles[tile].cget('image')
            if tile_checker(tile, piece, image) == 1:
                break
        for letter in letters: # right
            if letters.index(letter) > letters.index(text[0]):
                tile = f"{letter}{text[1]}"
                piece = tiles[tile].cget('image')
                if tile_checker(tile, piece, image) == 1:
                    break
        for letter in reversed(letters): # left
            if letters.index(letter) < letters.index(text[0]):
                tile = f"{letter}{text[1]}"
                piece = tiles[tile].cget('image')
                if tile_checker(tile, piece, image) == 1:
                    break
    if image == 'pyimage10' or image == 'pyimage4': # bishops
        index = letters.index(text[0])
        for i in range(8-int(text[1])):
            try:
                tile = f"{letters[index+1]}{i + int(text[1]) + 1}"
            except:
                break
            index += 1
            piece = tiles[tile].cget('image')
            if tile_checker(tile, piece, image) == 1:
                break
        index = letters.index(text[0])
        for i in range(int(text[1]) - 1, 0, -1):
            try:
                tile = f"{letters[index + 1]}{i}"
            except:
                break
            piece = tiles[tile].cget('image')
            index += 1
            if tile_checker(tile, piece, image) == 1:
                break
        index = letters.index(text[0])
        for i in range(8 - int(text[1])):
            try:
                if index > 0:
                    tile = f"{letters[index-1]}{i + int(text[1]) + 1}"
                else:
                    break
            except:
                break
            index -= 1
            piece = tiles[tile].cget('image')
            if tile_checker(tile, piece, image) == 1:
                break
        index = letters.index(text[0])
        for i in range(int(text[1]) - 1, 0, -1):
            try:
                if index > 0:
                    tile = f"{letters[index - 1]}{i}"
                else:
                    break
            except:
                break
            index -= 1
            piece = tiles[tile].cget('image')
            if tile_checker(tile, piece, image) == 1:
                break


# function attached to individual buttons and called when clicked
def select_tile(key):
    text = key.cget('text')
    image = key.cget('image')
    if select.loc == '':
        # player chose square thats empty
        if image == 'pyimage13':
            select.loc = ''
        # player chose square with piece
        else:
            if select.turn == True:
                if image in w_pieces:
                    select.loc = text
                    select.image = image
                    select.bg = key.cget('bg')
                    tiles[text].config(bg='#E0CD66')
                    legal_move(text, image)
                else:
                    select.loc = ''
            else:
                if image in b_pieces:
                    select.loc = text
                    select.image = image
                    select.bg = key.cget('bg')
                    tiles[text].config(bg='#E0CD66')
                    legal_move(text, image)
                else:
                    select.loc = ''
    # after player selects first selection
    else:
        if text == select.loc:
            tiles[select.loc].config(bg=select.bg)
            count = 0
            for move in select.moves:
                if move != text:
                    tiles[move].config(image=select.moveImages[count])
                count = count + 1
            select.loc = ''
            select.moves.clear()
            select.moveImages.clear()
        if text in select.moves:
            tiles[text].config(image=select.image)
            tiles[select.loc].config(image=empty)
            tiles[select.loc].config(bg=select.bg)
            count = 0
            for move in select.moves:
                if move != text:
                    tiles[move].config(image=select.moveImages[count])
                count = count + 1
            select.loc = ''
            select.moves.clear()
            select.moveImages.clear()
            select.turn = not select.turn
            if select.turn is True:
                root.title("Chess Game - White to Move")
            else:
                root.title("Chess Game - Black to Move")


# new game menu option
def new():
    setup_pieces()
    select.turn = True
    if select.loc != '':
        tiles[select.loc].config(bg=select.bg)
        select.loc = ''


# info menu option
def info():
    new = Toplevel(root)
    new.geometry("200x65")
    new.config(bg="#111111")
    new.title("Info")
    label = Label(new, text="VERSION 0.0.1", bg="#111111", fg='#eeeed2')
    label.pack(pady=20)


# main setup on start
setup_tiles()
setup_pieces()

main_menu = Menu(root)
main_menu.add_command(label="New", command=new)
main_menu.add_command(label="Info", command=info)
root.config(menu=main_menu)
root.geometry("528x528")
root.title("Chess Game - White to Move")
root.config(bg="#111111")
root.resizable(height=False, width=False)
root.mainloop()


