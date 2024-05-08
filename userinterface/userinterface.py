import logging
from tkinter import Tk, Canvas
from .window import Window
from .page_main import Page_main
from .page_anastomosis import Page_anastomosis
from .page_confirmation_anastomosis_to_main import Page_confirmation_anastomosis_to_main
from .page_confirmation_anastomosis_to_pump import Page_confirmation_anastomosis_to_pump
from .page_confirmation_pump_to_anastomosis import Page_confirmation_pump_to_anastomosis
from .page_confirmation_pump_to_training_summary import Page_confirmation_pump_to_training_summary
from .page_pump import Page_pump
from .page_enter_debit import Page_enter_debit
from .page_training_summary import Page_training_summary

logger = logging.getLogger(__name__)

class Userinterface:
    def __init__(self,title,dimension,fullscreen: bool = False):
        self.window = Window(title,dimension,fullscreen)
        self.page_classes = {
            "page_main" : Page_main,
            "page_anastomosis" : Page_anastomosis,
            "page_confirmation_anastomosis_to_main" : Page_confirmation_anastomosis_to_main,
            "page_confirmation_anastomosis_to_pump" : Page_confirmation_anastomosis_to_pump,
            "page_confirmation_pump_to_anastomosis" : Page_confirmation_pump_to_anastomosis,
            "page_confirmation_pump_to_training_summary" : Page_confirmation_pump_to_training_summary,
            "page_pump" : Page_pump,
            "page_enter_debit" : Page_enter_debit,
            "page_training_summary" : Page_training_summary
        }
        self.current_page = None
    
    def switch_to(self, name):
        logger.debug("Switch to "+str(name))
        new_frame: Canvas = self.page_classes[name](self.window)
        if self.current_page is not None:
            self.current_page.place_forget()
        self.current_page = new_frame
        self.current_page.place(x=0, y=0)

    def start_mainloop(self):
        self.window.mainloop()

    def exit_app(self):
        self.window.destroy()