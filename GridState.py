from Memento import Memento

class GridState:
    def __init__(self, value):
        self.state = value
            
    def SetState(self, value):
        self.state = value
    
    def GetState(self):
        return self.state
    
    def CreateMemento(self):
        return Memento(self.state)
    
    def SetMemento(self, memento):
        self.state = memento.GetState()    