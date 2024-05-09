from .controller_base import Controller_base
from userinterface.page_enter_debit import Page_enter_debit
import logging

logger = logging.getLogger(__name__)

class Controller_page_enter_debit(Controller_base): 
    def __init__(self,model, userinterface):
        super().__init__(model,userinterface)
        self.page: Page_enter_debit = self.userinterface.current_page
        self._bind_with_userinterface()
        self.model.pump.trigger_event("update_setpoint_debit_view")
        
    def _bind_with_userinterface(self):
        # self.page.button_to_anastomosis.config(command = lambda: self._moveto_page_anastomosis())
        self.page.button_finalize_debit.config(command = lambda: self._moveto_page_pump())
        self.page.button_number_0.config(command = lambda: self._update_value_from_button(0))
        self.page.button_number_1.config(command = lambda: self._update_value_from_button(1))
        self.page.button_number_2.config(command = lambda: self._update_value_from_button(2))
        self.page.button_number_3.config(command = lambda: self._update_value_from_button(3))
        self.page.button_number_4.config(command = lambda: self._update_value_from_button(4))
        self.page.button_number_5.config(command = lambda: self._update_value_from_button(5))
        self.page.button_number_6.config(command = lambda: self._update_value_from_button(6))
        self.page.button_number_7.config(command = lambda: self._update_value_from_button(7))
        self.page.button_number_8.config(command = lambda: self._update_value_from_button(8))
        self.page.button_number_9.config(command = lambda: self._update_value_from_button(9))
        self.page.button_delete.config(command = lambda: self._delete_value_from_button())
        # for i in range (9):
            # exec("self.page.button_number_{digit}.config(command = lambda: self._update_value_from_button())".format(digit=i))
        
    def _moveto_page_pump(self):
        logger.info("button go to pump menu pressed, change app state")
        self.model.user_state.move_to_new_page("page_pump")

    def _update_value_from_button(self,number):
        logger.info("button number "+str(number)+" pressed")
        self.model.pump.get_pump_setpoint_debit(number)

    def _delete_value_from_button(self):
        logger.info("button delete pressed, delete last input")
        self.model.pump.delete_digit_setpoint_debit()
