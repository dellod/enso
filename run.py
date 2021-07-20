# run.py
# Main entry point for program
# 2021

###########
# IMPORTS #
###########
import pygame
from main_window.main_window import MainWindow

#############
# CONSTANTS #
#############


###########
# GLOBALS #
###########

# MAIN
def main():
    pygame.init()
    _main_window = MainWindow()
    _main_window.run()
    pygame.quit()

if __name__ == "__main__":
    main()