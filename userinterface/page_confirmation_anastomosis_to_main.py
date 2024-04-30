import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets
from model.model import Model

page_name = "page_confirmation_anastomosis_to_main"
logger = logging.getLogger(__name__)

class Page_confirmation_anastomosis_to_main(Canvas):
    def __init__(self,parent, model: Model):
        super().__init__(parent)
        logger.debug("Create "+str(page_name)+" canvas")
        self.config(
            bg = "#F2F2F2",
            height = 480,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.place(x = 0, y = 0)
        self.create_text(
            400,70,
            anchor="c",
            text="CONFIRMATION PAGE",
            fill="#1C666F",
            font=("Inter", 40 * -1,"bold"),
            justify="center"
        )

        self.create_text(
            400,215,
            anchor="c",
            text="Are you sure you want to go back to the main menu?\nAll the data obtained from this current training (camera recording, timestamp, etc) will be deleted",
            fill="#000000",
            font=("Inter",-30,"bold"),
            justify='center',
            width=760
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        self.button_to_anastomosis = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_to_anastomosis.place(
            x=410.0,
            y=350.0,
            width=370.0,
            height=100.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets(page_name,"button_2.png"))
        self.button_to_main = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_to_main.place(
            x=20.0,
            y=350.0,
            width=370.0,
            height=100.0
        )