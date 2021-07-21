#!/usr/bin/env python3
# @file     logger.py
# @brief    Logging system class
# Daryl Dang - 2021

###########
# IMPORTS #
###########
import logging

from enum import IntEnum, auto

#############
# CONSTANTS #
#############

###########
# GLOBALS #
###########

#####################
# Class Definitions #
#####################
class VerbosityLevel(IntEnum):
    """
    Enum for verbosity levels.
    """
    VERBOSITY_LEVEL0 = 0
    VERBOSITY_LEVEL1 = auto()
    VERBOSITY_LEVEL2 = auto()

class Logger:
    """
    Singleton class of the logger system that will handle the logging system of the game.
    ...

    Attributes
    ----------
    _logger_instance: Logger
        Represents the current running instance of Logger, this will only be created once (by default set to None).
    _verbosity_level: int
        Represents the verbosity level (by default set to VERBOSITY_LEVEL0).
    """
    _logger_instance = None
    _verbosity_level = int(VerbosityLevel.VERBOSITY_LEVEL0)

    @staticmethod
    def get_instance():
        """
        Obtains instance of Logger.
        """
        if Logger._logger_instance is None:
            Logger()
        return Logger._logger_instance

    def __init__(self) -> None:
        """
        Default constructor.
        """
        if Logger._logger_instance != None:
            raise Exception("{}: Cannot construct, an instance is already running.".format(__file__))
        else:
            Logger._logger_instance = self

    def set_verbosity_level(self, verbosity_level: int) -> bool:
        """
        Sets the verbosity level of logger.

        Args:
            verbosity_level (int): Level of verbosity that will be set to logger.

        Returns:
            bool: Returns if verbosity level was set successfully.
        """
        _enum_values = [item.value for item in VerbosityLevel]
        if verbosity_level in _enum_values:
            self._verbosity_level = verbosity_level
            return True
        else:
            return False

    def print_console(self, message: str="", src_file: str="") -> None:
        """
        Prints to console if verbosity level 1 or more set.

        Args:
            message (str, optional)     : Message to print to console. Defaults to "".
            src_file (str, optional)    : [description]. Defaults to "".
        """
        if self._verbosity_level >= int(VerbosityLevel.VERBOSITY_LEVEL1):
            print(message)

if __name__ == "__main__":
    pass
    # logger = Logger.get_instance()

    # #Testing verbosity level 0
    # logger.set_verbosity_level(0)
    # logger.print_console("testing logger verbosity level 0")

    # #Testing verbosity level 1
    # logger.set_verbosity_level(1)
    # logger.print_console("testing logger verbosity level 1")