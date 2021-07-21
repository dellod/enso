#!/usr/bin/env python3
# @file     run.py
# @brief    Main entry point for program
# Daryl Dang - 2021

###########
# IMPORTS #
###########
import pygame

from main_window.main_window import MainWindow
from logger.logger import Logger

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