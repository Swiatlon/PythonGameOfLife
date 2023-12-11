import pygame
from GameLogic import GameLogic
from FileManager import SaveConfigCommand, LoadConfigCommand, DeleteSaveCommand, ToggleStartStopCommand
from UIManager import UIManager, Button
from GridState import GridState
from GameState import GameState

# Constants
WIDTH, HEIGHT = 1000, 1000
BUTTON_WIDTH = 100
BUTTON_MARGIN = 20

# Colors
BLACK = (0, 0, 0)

def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    UI = UIManager(screen)
    grid = GridState(GameLogic.initialize_grid())
    game_is_running = GameState(False)

    buttonStart = Button(WIDTH - BUTTON_WIDTH - BUTTON_MARGIN,
                        "Start",
                        ToggleStartStopCommand,
                        game_is_running)
    
    buttonSave = Button(WIDTH - 2*BUTTON_WIDTH - 2*BUTTON_MARGIN,
                        "Save",
                        SaveConfigCommand,
                        grid)
    
    buttonLoad = Button(WIDTH - 3*BUTTON_WIDTH - 3*BUTTON_MARGIN,
                        "Load",
                        LoadConfigCommand,
                        grid)
    
    buttonDelete = Button(WIDTH - 4*BUTTON_WIDTH - 4*BUTTON_MARGIN,
                        "Delete",
                        DeleteSaveCommand)
                        
    UI.add_button(buttonStart)
    UI.add_button(buttonSave)
    UI.add_button(buttonLoad)
    UI.add_button(buttonDelete)

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                UI.handle_click(mouse_x, mouse_y) 

        screen.fill(BLACK)
        UI.draw_grid(grid.GetState())
        UI.draw_buttons()

        if game_is_running.GetState():
            buttonStart.text = "Stop"
            new_grid = GameLogic.evolve(grid.GetState())
            grid.SetState(new_grid)
        else: 
            buttonStart.text ="Start"    

        pygame.display.flip()
        clock.tick(5)  # Adjust the speed by changing the tick value

    pygame.quit()

if __name__ == "__main__":
    main()
