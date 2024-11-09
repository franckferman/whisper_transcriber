#!/usr/bin/env python3
# helpers.py

"""
Helpers Module

Description:
Utility functions including logging setup and a loading animation for processing feedback.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.1
"""

import time
import sys
import logging
from datetime import datetime
from typing import Callable

def start_logging(debug: bool) -> None:
    """
    Initializes logging with a timestamped log file if debug mode is enabled.

    Args:
        debug (bool): If True, logging is enabled with a timestamped file.
    """
    if debug:
        # Generate a timestamped filename for the log file
        log_filename = f'transcription_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        
        logging.basicConfig(
            filename=log_filename, 
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info("Debug mode activated. Logging to '%s'.", log_filename)


def display_loading_dots(active: Callable[[], bool]) -> None:
    """
    Displays a loading animation of dots while a process is active.

    Args:
        active (Callable): A function that returns True while the animation should run.
    """
    dots = ""
    while active():
        dots = "." * ((len(dots) + 1) % 4)
        sys.stdout.write(f"\rProcessing{dots} ")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\nProcess completed.\n")
