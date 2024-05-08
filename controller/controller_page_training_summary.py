from .controller_base import Controller_base
from userinterface.page_training_summary import Page_training_summary
import logging

logger = logging.getLogger(__name__)

class Controller_page_training_summary(Controller_base): 
    def __init__(self,model, userinterface):
        super().__init__(model,userinterface)
        self.page: Page_training_summary = self.userinterface.current_page
        self._bind_with_userinterface()
        
    def _bind_with_userinterface(self):
        self.page.button_to_main.config(command = lambda: self._moveto_page_main())
        
    def _moveto_page_main(self):
        logger.info("button go to main menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_main")