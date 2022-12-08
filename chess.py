from tkinter import *
import math

button_array={}


def setup_tiles(root):
    index = 1
    alternate = True
    for i in range(8):
        for j in range(8):
            def func(num=index):
                select_tile(num)
            color = ['#769656', '#eeeed2']
            inverse = ['1', '8', '7', '6', '5', '4', '3', '2', '1']
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            display = f"{letters[math.floor((index/8)-0.01)]}{inverse[index%8]}"
            button_array[i] = Button(root, text=display, command=func, height=4, width=9, bg=color[alternate]).grid(column=i, row=j)
            if (index%8!=0):
                alternate=not alternate
            index+=1


def select_tile(num):
    inverse = ['1','8','7','6','5','4','3','2','1']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    sq = f"{letters[math.floor((num / 8) - 0.01)]}{inverse[num % 8]}"
    print(sq)


def new():
    print("reset_board()")


root = Tk()
setup_tiles(root)
main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="New", command=new)
root.geometry("586x570")
root.title("Chess Game")
root.config(bg="#111111")
root.resizable(height=False, width=False)
root.mainloop()


