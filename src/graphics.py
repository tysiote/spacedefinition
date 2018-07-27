from tkinter import Tk, Canvas


class GraphicController(object):
    root = None
    canvas = None
    app = None

    def __init__(self, app):
        self.app = app
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.geometry('{}x{}'.format(720, 480))
        self.root.title("The Space Definition - " + app.version)
        self.canvas = Canvas(self.root, width=720, height=480, bg='black')
        self.canvas.pack()
        self.root.mainloop()
