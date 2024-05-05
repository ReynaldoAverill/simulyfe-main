from .controller_base import Controller_base
from userinterface.page_main import Page_main
import logging

logger = logging.getLogger(__name__)

class Controller_page_main(Controller_base): 
    def __init__(self,model,userinterface):
        super().__init__(model,userinterface)
        self.page: Page_main = self.userinterface.current_page
        # self.page = self.userinterface.page_classes["page_main"](self.userinterface)
        self._bind_with_userinterface()
        # print(self.page.x)

    def _bind_with_userinterface(self):
        # pass
        self.page.button_start.config(command = lambda: self._moveto_page_anastomosis())
        self.page.button_exit.config(command = lambda: self._exit_app())
        # self.page.button_exit.config(command = lambda: self._exit_app())

    def _moveto_page_anastomosis(self):
        logger.info("button start_pressed, change app state")
        self.model.user_state.move_to_new_page("page_anastomosis")

    def _exit_app(self):
        logger.info("button exit pressed, change app state")
        self.model.user_state.exit()
