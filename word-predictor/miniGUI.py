import tkinter as tk
import src.prefixTree as tree


WINDOW_WIDTH = 450
WINDOW_HEIGHT = 250


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


class GUI():
    def __init__(self):
        self.cur_word = ''

    def center(self, win):
        win.update_idletasks()

        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x = screen_width / 2 - WINDOW_WIDTH / 2
        y = screen_height / 2 - WINDOW_HEIGHT / 2

        win.geometry("%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, x, y))

    def resize_text(self, win, txt):
        win.update_idletasks()
        txt.config(width=win.winfo_width(), height=win.winfo_height())

    def get_cur_word(self):
        return self.cur_word

    def set_cur_word(self, cur_word):
        self.cur_word = cur_word


def print_words(event):
    new_char = chr(event.keycode).lower()
    if new_char.isalpha():
        gui.set_cur_word(gui.get_cur_word() + new_char)
    elif new_char.isspace():
        gui.set_cur_word('')
    elif event.keycode == 8:
        word = gui.get_cur_word()
        gui.set_cur_word(word[:len(word) - 1])
    pt.query(pt.root, gui.get_cur_word(), '')
    print("|---------------------------------------|")
    #print(gui.get_cur_word())


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    pt = tree.PrefixTree()
    gui = GUI()

    root.title("Word predictor")
    gui.center(root)
    # root.resizable(False, False)

    text = tk.Text(root, wrap=tk.WORD)
    text.pack()
    text.focus()

    root.bind("<Configure>", gui.resize_text(root, text))
    root.bind("<Key>", print_words)

    root.mainloop()
