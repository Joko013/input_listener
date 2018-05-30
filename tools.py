import tkinter
from PIL import ImageTk, Image


def make_popup():
    """ Make a popup window with an image. """

    # basic object that represents the window
    root = tkinter.Tk()

    # widget for storing the actual image
    img = ImageTk.PhotoImage(Image.open("Pics\chill.jpg"))
    widget = tkinter.Label(root, image=img)
    widget.pack()

    # make window popup on top; make window disappear after 1,5s
    root.attributes("-topmost", True)
    root.after(1500, lambda: root.destroy())

    root.mainloop()


class TextAnalyzer:
    """ Object to analyze the text and based on the result call an appropriate function. """

    def __init__(self):
        # define your set of bad words
        self.bw_set = set()
        with open('Bad_words/bad_words_eng.txt', mode='r') as f:
            for line in f:
                self.bw_set.add(line.replace('\n', ''))

    def analyze_text(self, text):
        """ Check the text and call function. """
        if text.lower() in self.bw_set:
            make_popup()
        else:
            print(text)





