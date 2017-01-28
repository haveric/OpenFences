import selection
import pyHook


class EventHandler:
    def __init__(self, parent, floater_manager):
        self.uiParent = parent
        self.dragging = False
        self.startX = -1
        self.startY = -1
        self.endX = -1
        self.endY = -1
        self.currentSelection = None
        self.floater_manager = floater_manager

        hm = pyHook.HookManager()

        hm.SubscribeMouseMiddleDown(self.MouseMiddleDown)
        hm.SubscribeMouseMiddleUp(self.MouseMiddleUp)
        hm.SubscribeMouseMove(self.MouseMove)
        hm.HookMouse()

    def MouseMiddleDown(self, event):
        if (event.WindowName == None or event.WindowName == "FolderView"):
            self.dragging = True
            print("mouse right down while dragging")
            self.startX = event.Position[0]
            self.startY = event.Position[1]
            self.endX = self.startX
            self.endY = self.startY

            self.currentSelection = selection.Selection(self.uiParent, self.startX, self.startY)
            self.currentSelection.deiconify()

        return True

    def MouseMiddleUp(self, event):
        if (self.dragging == True):
            self.dragging = False
            print("mouse right up while dragging")
            x = self.currentSelection.x
            y = self.currentSelection.y
            width = self.currentSelection.width
            height = self.currentSelection.height

            self.currentSelection.destroy()
            print("{} {} {} {} {}".format(self.uiParent, x, y, width,height))
            if width > 10 and height > 10:
                self.floater_manager.add_floater(self.uiParent, x, y, width, height)

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

            self.currentSelection.UpdatePosition(self.endX, self.endY)
        return True