import logging
from .window import Window
from .page_main import Page_main
from .page_anastomosis import Page_anastomosis
from .page_confirmation_anastomosis_to_main import Page_confirmation_anastomosis_to_main
from .page_confirmation_anastomosis_to_pump import Page_confirmation_anastomosis_to_pump
from .page_pump import Page_pump

logger = logging.getLogger(__name__)

class Userinterface:
    def __init__(self,title,dimension):
        self.window = Window(title,dimension)
        self.page_classes = {
            "page_main" : Page_main,
            "page_anastomosis" : Page_anastomosis,
            "page_confirmation_anastomosis_to_main" : Page_confirmation_anastomosis_to_main,
            "page_confirmation_anastomosis_to_pump" : Page_confirmation_anastomosis_to_pump,
            "page_pump" : Page_pump
        }
        self.current_page = None
    
    def switch_to(self, name):
        logger.debug("Switch to "+str(name))
        new_frame = self.page_classes[name](self.window)
        if self.current_page is not None:
            self.current_page.place_forget()
        self.current_page = new_frame
        self.current_page.place(x=0, y=0)

    def start_mainloop(self):
        self.window.mainloop()

    def exit_app(self):
        self.window.destroy()