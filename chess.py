from tkinter import *


button_array={}


def setup_tiles(root):
    counter = 1
    for i in range(8):
        for j in range(8):
            def func(sq=counter):
                select_tile(sq)
            button_array[i] = Button(root, text=counter, command=func, height=4, width=9).grid(column=i, row=j)
            counter+=1


def select_tile(sq):
    print(sq)


def new():
    print("reset_board()")


root = Tk()
setup_tiles(root)
main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label='New', command=new)
root.geometry("586x570")
root.title("Chess Game")
root.config(bg="#111111")
root.resizable(height=False, width=False)
root.mainloop()


