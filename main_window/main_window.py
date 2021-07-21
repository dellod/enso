# main_window.py
# Main window for game.
# 2021

###########
# IMPORTS #
###########
import pygame

#############
# CONSTANTS #
#############
WIDTH, HEIGHT = 900, 500
SCREEN_SIZE = (WIDTH, HEIGHT)
CAPTION = "Enso"
FPS = 60

###########
# GLOBALS #
###########

#####################
# Class Definitions #
#####################
class MainWindow:
    def __init__(self):
        """
        Constructor
        """
        # Set window size
        WIN = pygame.display.set_mode(SCREEN_SIZE)

        # Set window title
        pygame.display.set_caption("Enso")

    def run(self):
        """
        Runs the main window.
        """
        _is_window_running = True
        clock = pygame.time.Clock()

        while _is_window_running:
            clock.tick(FPS) # Keep clock refresh rate at consisten frame rate
            for event in pygame.event.get():
                # User clicks the exit button at the top right of the window, break from this loop
                if event.type == pygame.QUIT:
                    _is_window_running = False