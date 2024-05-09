from .controller_base import Controller_base
from model.component.pump.pump import Pump
import logging

logger = logging.getLogger(__name__)

class Controller_userinterface(Controller_base):
    def __init__(self, model, userinterface):
        super().__init__(model,userinterface)
        self.model.pump.add_event_listener("get_setpoint_debit",self.get_setpoint_debit)

    def get_setpoint_debit(self, pump: Pump):
        pass
