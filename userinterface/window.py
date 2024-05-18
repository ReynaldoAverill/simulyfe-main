import logging
import os
from tkinter import Tk
from .page_main import Page_main
import model.constant as const

logger = logging.getLogger(__name__)

class Window(Tk):
    def __init__(self,title,size):
        """_summary_

        Args:
            title (string): Title of the application
            size (integer,integer): Dimension of the application (width,height)
        """
        super().__init__()
        logger.debug('Initiate window for user interface')
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.configure(bg = "#000000")
        # Set window into full screen
        self.wm_overrideredirect(const.FULLSCREEN)
        self.resizable(False, False)


