import floater


class FloaterManager:
    def __init__(self):
        self.floaters = []

    def add_floater(self, parent, x, y, width, height):
        self.floaters.append(floater.Floater(parent, x, y, width, height))

    def destroy_all(self, event):
        for floater in self.floaters:
            floater.Destroy(event)
        self.floaters = []