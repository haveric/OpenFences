#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import configscreen
import eventhandler
import floatermanager


class FloatersApp:
    def __init__(self, parent):
        floater_manager = floatermanager.FloaterManager()
        self.floaterManager = floater_manager
        self.configScreen = configscreen.ConfigScreen(None, floater_manager)
        self.configScreen.title('Floaters')
        self.eventHandler = eventhandler.EventHandler(self.configScreen, floater_manager)
        self.configScreen.mainloop()


if __name__ == "__main__":
    app = FloatersApp(None)