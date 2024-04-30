from userinterface.userinterface import Userinterface
import logging

logger = logging.getLogger(__name__)

class Controller_page_main: 
    def __init__(self,userinterface:Userinterface):
        userinterface.switch_to("page_main")
        self.page = userinterface.page_classes["page_main"]
        # self.page = self.userinterface.page_classes["page_main"](self.userinterface)
        self.bind_with_userinterface(userinterface)
    def _bind_with_userinterface(self,userinterface):
        self.page.button_start.config(command = lambda: self.moveto_page_anastomosis(userinterface))
        self.page.button_exit.config(command = lambda: self.exit_app(userinterface))
    def _moveto_page_anastomosis(self, userinterface:Userinterface):
        logger.debug("button start_pressed")
        userinterface.switch_to("page_anastomosis")
        userinterface.start_mainloop()
    def _exit_app(self,userinterface:Userinterface):
        logger.debug("button exit pressed")
        userinterface.exit_app()
