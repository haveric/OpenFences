#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import pyHook
import tkinter

class simpleapp_tk(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent;
        self.dragging = False
        self.startX = -1
        self.startY = -1
        self.endX = -1
        self.endY = -1
        self.initialize()
        
    def initialize(self):
        self.overrideredirect(1)
        self.geometry('500x250+500+200')
        self.grid()
        
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")
        
        button = tkinter.Button(self, text=u"Quit!", command=self.OnButtonClick)
        button.grid(column=1, row=0)
        
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="blue")
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.labelVariable.set(u"Hello !")
        
        self.grid_columnconfigure(0, weight=1)
        #self.resizable(True, False)
        self.update()
        self.geometry(self.geometry()) 
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        
        hm = pyHook.HookManager()
        hm.SubscribeMouseRightDown(self.MouseRightDown)
        hm.SubscribeMouseRightUp(self.MouseRightUp)
        hm.SubscribeMouseMove(self.MouseMove)
        hm.HookMouse()

    def OnButtonClick(self):
        quit()
        
    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get() + " (You pressed ENTER)")
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def quit(self):
        self.root.destroy()

    def MouseRightDown(self, event):
        if (event.WindowName == None):
            self.dragging = True
            self.startX = event.Position[0]
            self.startY = event.Position[1]
            self.endX = self.startX
            self.endY = self.startY
            
            self.rect = Rect(self.parent, self.startX, self.startY)
            self.rect.deiconify()
            
        return True

    def MouseRightUp(self, event):
        if (self.dragging == True):
            self.dragging = False
            
            x = self.rect.x
            y = self.rect.y
            width = self.rect.width
            height = self.rect.height
            
            self.rect.destroy()
            self.floater = FloatingWindow(self.parent, x, y, width, height)

            '''            
            # called when mouse events are received
            print('MessageName:', event.MessageName)
            print('Message:', event.Message)
            print('Time:', event.Time)
            print('Window:', event.Window)
            print('WindowName:', event.WindowName)
            print('Position:', event.Position)
            print('Wheel:', event.Wheel)
            print('Injected:', event.Injected)
            print('---')
            '''

        return True
        
    def MouseMove(self, event):
        if (self.dragging == True):
            self.endX = event.Position[0]
            self.endY = event.Position[1]
            
            self.rect.UpdatePosition(self.endX, self.endY)
        return True

class Rect(tkinter.Toplevel):
    def __init__(self, parent, x, y):
        tkinter.Toplevel.__init__(self, parent)
        self.overrideredirect(True)
        self.withdraw()
        self.geometry('+%d+%d' % (x, y))
        self.configure(width=1,height=1,bg='white', highlightbackground='black', highlightthickness=1)
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
        self.geometry('+%d+%d' % (self.x, self.y))
        self.configure(width=self.width, height=self.height)

class FloatingWindow(tkinter.Toplevel):
    def __init__(self, parent, x, y, width, height):
        tkinter.Toplevel.__init__(self)
        self.overrideredirect(True)

        self.geometry('+%d+%d' % (x, y))
        self.configure(width=width, height=height)

        self.label = tkinter.Label(self, text="Click on the grip to move")
        self.grip = tkinter.Label(self, bitmap="gray25")
        self.grip.pack(side="left", fill="y")
        self.label.pack(side="right", fill="both", expand=True)

        self.grip.bind("<ButtonPress-1>", self.StartMove)
        self.grip.bind("<ButtonRelease-1>", self.StopMove)
        self.grip.bind("<B1-Motion>", self.OnMotion)

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

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()