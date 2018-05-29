import tkinter


def make_popup(text):
    top = tkinter.Tk()
    content = tkinter.Text(top)
    content.insert(tkinter.INSERT, text)
    content.pack()
    top.attributes("-topmost", True)
    top.after(1500, lambda: top.destroy())

    top.mainloop()


class TextAnalyzer:
    def __init__(self):
        bad_words = ['fuck', 'shit', 'dick']
        self.bad_words_set = set(bad_words)

    def analyze_text(self, text):
        if text in self.bad_words_set:
            make_popup('Ouch, chill dude!')
        else:
            make_popup('Everything cool here.')


