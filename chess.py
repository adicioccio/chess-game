from tkinter import *
import math

button_array={}


# def setup_tiles(root):
#     index = 1
#     alternate = True
#     for i in range(8):
#         for j in range(8):
#             def func(num=index):
#                 select_tile(num)
#             color = ['#769656', '#eeeed2']
#             inverse = ['1', '8', '7', '6', '5', '4', '3', '2', '1']
#             letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#             display = f"{letters[math.floor((index/8)-0.01)]}{inverse[index%8]}"
#             button_array[index-1] = Button(root, text=display, command=func, height=4, width=9, bg=color[alternate]).grid(column=i, row=j)
#             if (index%8!=0):
#                 alternate=not alternate
#             index+=1

def setup_tiles(root):
    index = 1
    alternate = True
    for i in range(8):
        for j in range(8):
            color = ['#769656', '#eeeed2']
            inverse = ['1', '8', '7', '6', '5', '4', '3', '2', '1']
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            pos = f"{letters[math.floor((index/8)-0.01)]}{inverse[index%8]}"
            btn = Button(root, text=pos, bg=color[alternate], activebackground="white", height=4, width=9)
            btn.grid(column=i, row=j)
            button_array.setdefault(pos, btn)
            button_array[pos].config(command=lambda key=button_array[pos]: select_tile(key))
            if (index%8!=0):
                alternate=not alternate
            index+=1

def select_tile(key):
    key['text'] = 'new'
    text = key.cget('text')
    print(key)


def new():
    print("reset_board()")


root = Tk()
setup_tiles(root)
main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="New", command=new)
root.geometry("586x570")
root.title("Chess Game - 0.0.0")
root.config(bg="#111111")
root.resizable(height=False, width=False)
root.mainloop()


