from .controller_base import Controller_base
from userinterface.page_training_summary import Page_training_summary
import logging

logger = logging.getLogger(__name__)

class Controller_page_training_summary(Controller_base): 
    def __init__(self,model, userinterface):
        super().__init__(model,userinterface)
        self.page: Page_training_summary = self.userinterface.current_page
        self._bind_with_userinterface()
        self._update_view()
        
    def _bind_with_userinterface(self):
        self.page.button_to_main.config(command = lambda: self._moveto_page_main())
        
    def _moveto_page_main(self):
        logger.info("button go to main menu pressed, reset the state of all component")
        self.model.user_state.move_to_new_page("page_main")
        # Reset all component state
        self.model.pump.reset_pump()
        self.model.flow_sensor.reset_flow_sensor()
        self.model.stopwatch.reset_stopwatch()

    def _update_view(self):
        logger.info("renew all data in the page")
        # Update input debit view
        self.model.pump.trigger_event("update_setpoint_debit_view")
        # Update measured debit view
        self.model.flow_sensor.trigger_event("update_measured_debit_view")
        # Update stopwatch time view
        self.model.stopwatch.trigger_event("update_stopwatch_view")
        # Update suturing force summary
        self.model.force_sensor.trigger_event("update_summary_view")