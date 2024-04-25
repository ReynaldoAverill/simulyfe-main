import logging
import os
from tkinter import Tk

logger = logging.getLogger(__name__)

class Window(Tk):
    def __init__(self,title,size):
        """_summary_

        Args:
            title (string): Title of the application
            size (integer,integer): Dimension of the application (width,height)
        """
        super().__init__()
        if os.environ.get('DISPLAY','') == '':
            logger.debug('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')
        logger.debug('Initiate window for user interface')
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.configure(bg = "#F2F2F2")
        # Set window into full screen
        # self.wm_overrideredirect(True)


