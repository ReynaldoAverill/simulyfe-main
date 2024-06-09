from .controller_base import Controller_base
from userinterface.page_anastomosis_camera import Page_anastomosis_camera
import logging

logger = logging.getLogger(__name__)

class Controller_page_anastomosis_camera(Controller_base): 
    def __init__(self,model,userinterface):
        super().__init__(model,userinterface)
        self.page: Page_anastomosis_camera = self.userinterface.current_page
        self._bind_with_userinterface()
        # Update stopwatch view
        self.model.stopwatch.trigger_event("update_stopwatch_view")

    def _bind_with_userinterface(self):
        # pass
        self.page.button_confirmation_to_main.config(command = lambda: self._moveto_page_main_confirmation())
        self.page.button_confirmation_to_pump.config(command = lambda: self._moveto_page_pump_confirmation())

        self.page.button_to_anastomosis_stopwatch.config(command = lambda: self._moveto_page_anastomosis_stopwatch())
        self.page.button_to_anastomosis_suturing_force.config(command = lambda: self._moveto_page_anastomosis_suturing_force())

        self.page.button_start_recording.config(command = lambda: self._start_recording())
        self.page.button_stop_recording.config(command = lambda: self._pause_recording())
        self.page.button_reset_recording.config(command= lambda: self._reset_recording())
        # self.page.button_reset_stopwatch.config(command = lambda: self.model.stopwatch.reset_stopwatch())
        
    def _moveto_page_main_confirmation(self):
        logger.info("button back to main menu pressed")
        self.model.user_state.move_to_new_page("page_confirmation_anastomosis_to_main")

    def _moveto_page_pump_confirmation(self):
        logger.info("button go to pump pressed")
        self.model.user_state.move_to_new_page("page_confirmation_anastomosis_to_pump")

    def _moveto_page_anastomosis_stopwatch(self):
        logger.info("button stopwatch pressed")
        self.model.user_state.move_to_new_page("page_anastomosis")
    
    def _moveto_page_anastomosis_suturing_force(self):
        logger.info("button suturing_force pressed")
        self.model.user_state.move_to_new_page("page_anastomosis_suturing_force")

    def _start_recording(self):
        logger.info("button start recording pressed")
        self.model.camera.start_recording()

    def _pause_recording(self):
        logger.info("button pause/stop recording pressed")
        self.model.camera.pause()

    def _reset_recording(self):
        logger.info("button reset recording pressed")
        self.model.camera.reset()