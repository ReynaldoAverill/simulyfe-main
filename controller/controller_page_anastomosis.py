from .controller_base import Controller_base
from userinterface.page_anastomosis import Page_anastomosis
import logging

logger = logging.getLogger(__name__)

class Controller_page_anastomosis(Controller_base): 
    def __init__(self,model,userinterface):
        super().__init__(model,userinterface)
        self.page: Page_anastomosis = self.userinterface.current_page
        self._bind_with_userinterface()
        # Update stopwatch view
        self.model.stopwatch.trigger_event("update_stopwatch_view")
        # check camera connection
        self.model.camera.activate()
        # Update camera status
        self.model.camera.trigger_event("update_connection_status")

    def _bind_with_userinterface(self):
        # pass
        self.page.button_confirmation_to_main.config(command = lambda: self._moveto_page_main_confirmation())
        self.page.button_confirmation_to_pump.config(command = lambda: self._moveto_page_pump_confirmation())

        self.page.button_to_anastomosis_camera.config(command = lambda: self._moveto_page_anastomosis_camera())
        self.page.button_to_anastomosis_suturing_force.config(command = lambda: self._moveto_page_anastomosis_suturing_force())

        self.page.button_start_stopwatch.config(command = lambda: self.model.stopwatch.change_stopwatch_state())
        self.page.button_stop_stopwatch.config(command = lambda: self.model.stopwatch.change_stopwatch_state())
        self.page.button_reset_stopwatch.config(command = lambda: self.model.stopwatch.reset_stopwatch())
        
    def _moveto_page_main_confirmation(self):
        logger.info("button back to main menu pressed")
        self.model.user_state.move_to_new_page("page_confirmation_anastomosis_to_main")

    def _moveto_page_pump_confirmation(self):
        logger.info("button go to pump pressed")
        self.model.user_state.move_to_new_page("page_confirmation_anastomosis_to_pump")

    def _moveto_page_anastomosis_camera(self):
        logger.info("button camera pressed")
        self.model.user_state.move_to_new_page("page_anastomosis_camera")
    
    def _moveto_page_anastomosis_suturing_force(self):
        logger.info("button suturing_force pressed")
        self.model.user_state.move_to_new_page("page_anastomosis_suturing_force")