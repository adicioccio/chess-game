from tkinter import *


squares = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]


def setup_tiles(root):
    for x in range(8):
        for y in range(8):
            btn = Button(root, command=lambda : tile_clicked("click"), height=2, width=5)
            btn.grid(column=x, row=y)


def tile_clicked(sq):
    print(sq)


def new():
    print("New button pressed!")


root = Tk()
setup_tiles(root)
main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label='New', command=new)
root.geometry("900x580")
root.title("Chess Game")
root.config(bg="#111111")
root.resizable(height=False, width=False)
root.mainloop()


