import model.constant as const
from model.base import ObservableModel
import threading
import socket

from subprocess import Popen, PIPE, STDOUT

import logging
logger = logging.getLogger(__name__)

class Flow_sensor(ObservableModel):
    def __init__(self):
        super().__init__()
        self.state          = "init"
        # Other states are idle, and listening
        self.measured_debit = 0
        self.raw_debit: str = None
        self.debit_accuracy = 0
        self.subprocess: Popen      = None
        self.socket: socket.socket  = None
        self.connection: socket.socket = None
        self.address        = None
        self.connected      = False
    
    def calculate_accuracy(self):
        if self.state:
            self.trigger_event("calculate_accuracy")
    
    def reset_flow_sensor(self):
        """Reset flow sensor to its initial condition
        """
        if self.state != "init":
            self.state = "init"
        self.trigger_event("terminate_and_close")
        self.measured_debit = 0
        self.debit_accuracy = 0
        self.subprocess     = None
        self.socket         = None
        self.address        = None
        self.connected      = False

    def activate(self):
        if self.state == "init":
            self.trigger_event("start_subprocess")
        if not self.connected:
            self.trigger_event("open_connection")
            self.connected = True
        self.state = "idle"
        self.retrieve_data()
    
    def generate_executable(self):
        self.trigger_event("generate_executable")

    def retrieve_data(self):
        logger.info("create thread for flow sensor")
        thread_flow_sensor = threading.Thread(target= lambda: self.trigger_event("retrieve_data"))
        # Auto close thread when main program ends
        thread_flow_sensor.daemon = True
        thread_flow_sensor.start()

    def change_listening_state(self):
        if self.state == "listening":
            logger.info("Flow sensor state changed into idle")
            self.state = "idle"
        elif self.state == "idle":
            self.state = "listening"
            logger.info("Flow sensor state changed into listening")
