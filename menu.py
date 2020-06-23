import tkinter as tk
from tkinter import ttk
import os


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/BG.gif")
        btn_open_dialog = tk.Button(toolbar, text='Начать игру', command=self.start_game, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.BOTTOM)

    def start_game(self):
        os.system(r'C:\\"Python Games"\\"Aliens_Game"\\alien_invasion.py')





if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Главное Меню")
    root.geometry("650x450")
    root.resizable(True, True)
    root.mainloop()