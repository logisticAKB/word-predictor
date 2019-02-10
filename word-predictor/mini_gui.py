import tkinter as tk
from prefix_trie import PrefixTree


WINDOW_WIDTH = 450
WINDOW_HEIGHT = 250


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


class GUI():
    def __init__(self):
        pass

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

    def get_word(self, string):
        string = string[::-1]
        word = ""
        for char in string:
            if char == ' ': break
            word += char
        return word[::-1]


def print_words(event):
    new_string = text.get(1.0, tk.END)
    word = gui.get_word(new_string)
    pt.query(pt.root, word.strip(), '')
    print("|---------------------------------------|")


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    pt = PrefixTree()
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
