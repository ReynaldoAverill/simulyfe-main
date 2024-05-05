from model.model import Model
from userinterface.userinterface import Userinterface

class Controller_base:
    def __init__(self, model: Model, userinterface: Userinterface) -> None:
        self.model = model
        self.userinterface = userinterface