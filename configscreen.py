import tkinter


class ConfigScreen(tkinter.Tk):
    def __init__(self, parent, floatermanager):
        tkinter.Tk.__init__(self, parent)
        self.overrideredirect(1)
        self.geometry('500x250+500+200')
        self.grid()

        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")

        button = tkinter.Button(self, text=u"Quit", command=self.OnButtonClick)
        button.grid(column=1, row=0)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="blue")
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.labelVariable.set(u"Welcome to Floaters !")

        self.destroyAllButton = tkinter.Button(self, text="Destroy All Floaters")
        self.destroyAllButton.grid(column=0, row=1)
        self.destroyAllButton.bind("<ButtonPress-1>", floatermanager.destroy_all)

        self.grid_columnconfigure(0, weight=1)
        # self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonClick(self):
        quit()

    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get() + " (You pressed ENTER)")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def quit(self):
        self.root.destroy()
