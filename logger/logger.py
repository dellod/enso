#!/usr/bin/env python3
# @file     logger.py
# @brief    Logging system class
# Daryl Dang - 2021

###########
# IMPORTS #
###########
import logging

#############
# CONSTANTS #
#############

###########
# GLOBALS #
###########

class Logger:
    """
    Singleton class of the logger system that will handle the logging system of the game.
    ...

    Attributes
    ----------
    _logger_instance : Logger
        Represents the current running instance of Logger, this will only be created once.
    """
    _logger_instance = None

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