import tkinter


class Selection(tkinter.Toplevel):
    def __init__(self, parent, x, y):
        tkinter.Toplevel.__init__(self, parent)
        self.overrideredirect(True)
        self.withdraw()
        self.geometry('+{}+{}'.format(x, y))
        self.configure(width=1, height=1, bg='white', highlightbackground='black', highlightthickness=2)
        self.attributes("-transparentcolor", "white")
        self.attributes("-alpha", "1")
        self.startX = x
        self.startY = y
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1

    def UpdatePosition(self, endX, endY):
        if (endX < self.startX):
            x1 = endX
            x2 = self.startX
        else:
            x1 = self.startX
            x2 = endX

        if (endY < self.startY):
            y1 = endY
            y2 = self.startY
        else:
            y1 = self.startY
            y2 = endY

        self.width = x2 - x1
        self.height = y2 - y1

        self.x = x1
        self.y = y1
        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
