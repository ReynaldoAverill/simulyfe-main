from userinterface.userinterface import Userinterface
import logging

logger = logging.getLogger(__name__)

class Controller_page_anastomosis: 
    def __init__(self,userinterface:Userinterface):
        userinterface.switch_to("page_anastomosis")
        self.page = userinterface.current_page
        # self.page = self.userinterface.page_classes["page_main"](self.userinterface)
        self.bind_with_userinterface(userinterface)
    def bind_with_userinterface(self,userinterface):
        self.page.button_exit.config(command = lambda: self.moveto_page_anastomosis(userinterface))
    def moveto_page_anastomosis(self,userinterface:Userinterface):
        logger.debug("button start_pressed")
        userinterface.switch_to("page_anastomosis")
        userinterface.start_mainloop()