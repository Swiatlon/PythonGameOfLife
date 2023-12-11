import os
from GameLogic import GameLogic
from abc import ABC, abstractmethod

# Define an abstract base class for commands
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class SaveConfigCommand(Command):
    def __init__(self, grid):
        self.grid = grid

    def execute(self):
        with open("saved_config.txt", "w") as file:
            for row in self.grid.GetState():
                file.write(" ".join(map(str, row)) + "\n")

class LoadConfigCommand(Command):
    def __init__(self,grid):
        self.grid = grid

    def execute(self):
        filename = "saved_config.txt"
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                new_grid = [[int(cell) for cell in line.strip().split()] for line in lines]
                self.grid.SetState(new_grid)
        except FileNotFoundError:
            return self.grid.SetState(GameLogic.initialize_grid())

class DeleteSaveCommand(Command):
    def execute(self):
        try:
            os.remove("saved_config.txt")
        except FileNotFoundError:
            pass

class ToggleStartStopCommand(Command):
    def __init__(self,gameState):
        self.gameState = gameState

    def execute(self):
        self.gameState.SetState(not self.gameState.GetState())    

class ButtonActionInvoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command:
            self.command.execute()
