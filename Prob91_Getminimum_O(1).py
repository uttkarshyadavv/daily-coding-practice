class Node:
    def __init__(self):
        self.items = []
        self.mini = None

    def push(self, value):
        if len(self.items) == 0:
            self.items.append(value)
            self.mini = value
        else:
            self.items.append(value) 
            if value < self.mini:
                self.mini = value
        return self.mini
