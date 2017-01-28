import tkinter


class Floater(tkinter.Toplevel):
    def __init__(self, parent, x, y, width, height):
        tkinter.Toplevel.__init__(self)
        self.xVal = x
        self.yVal = y
        self.width = width
        self.height = height

        print("creating floating window at: ", x, ",", y, "size: ", width, ",", height)

        self._set_window_size()
        self.windowGrip = self._add_window_grip()
        self.label = self._add_label()
        self.destroyButton = self._add_destroy_button()

    def _set_window_size(self):
        self.overrideredirect(True)
        self.grid()
        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.xVal, self.yVal))
        self.configure(bg='gray')

    def _add_window_grip(self):
        grip = tkinter.Label(self, bitmap="gray25")
        grip.grid(column=0, row=0)
        grip.bind("<ButtonPress-1>", self.StartMove)
        grip.bind("<ButtonRelease-1>", self.StopMove)
        grip.bind("<B1-Motion>", self.OnMotion)
        return grip

    def _add_label(self):
        label = tkinter.Label(self, text="Click on the grip to move")
        label.grid(column=1, row=0)
        return label

    def _add_destroy_button(self):
        destroybutton = tkinter.Button(self, text="x")
        destroybutton.grid(column=2, row=0)
        destroybutton.bind("<ButtonPress-1>", self.Destroy)
        return destroybutton

    def Destroy(self, event):
        self.DestroyMe()

    def DestroyMe(self):
        print("destroying floating window at: ", self.xVal, ",", self.yVal)
        self.destroy()

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))