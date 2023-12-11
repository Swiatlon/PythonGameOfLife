class Memento:
    def __init__(self, value):
        self.state = value
    
    def SetState(self, value):
        self.state = value

    def GetState(self):
        return self.state