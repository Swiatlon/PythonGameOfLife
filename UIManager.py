import pygame
from FileManager import ButtonActionInvoker

# Constants
WIDTH, HEIGHT = 1000, 1000
ROWS, COLS = 50, 50
CELL_SIZE = WIDTH // COLS
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 40
BUTTON_MARGIN = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)


class Button:
    def __init__(self, x, text, command_class, *args):
        self.x = x
        self.y = HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN
        self.width = BUTTON_WIDTH
        self.height = BUTTON_HEIGHT
        self.color = GRAY
        self.command_class = command_class
        self.args = args
        self.text = text
        self.invoker = ButtonActionInvoker()

    def is_clicked(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            command_instance = self.command_class(*self.args)
            self.invoker.set_command(command_instance)
            self.invoker.execute_command()
            return True
        return False

        

class UIManager:
    # Singleton
    _instance = None
    def __new__(cls, screen):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.screen = screen
            cls._instance.buttons = []
        return cls._instance

    def add_button(self, button):
        self.buttons.append(button)

    def handle_click(self, x, y):
        for button in self.buttons:
            result = button.is_clicked(x, y)
            if result:
                return result

    def draw_grid(self, grid):
        for i in range(ROWS):
            for j in range(COLS):
                color = WHITE if grid[i][j] else BLACK
                pygame.draw.rect(self.screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_button(self, x, y, text, color):
        pygame.draw.rect(self.screen, color, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
        font = pygame.font.Font(None, 36)
        button_text = font.render(text, True, BLACK)
        self.screen.blit(button_text, (x + 10, y + 10))

    def draw_buttons(self):
        for button in self.buttons:
            self.draw_button(button.x, button.y, button.text, button.color)