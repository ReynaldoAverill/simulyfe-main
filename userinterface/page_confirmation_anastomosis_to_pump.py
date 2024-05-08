import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets

page_name = "page_confirmation_anastomosis_to_pump"
logger = logging.getLogger(__name__)

class Page_confirmation_anastomosis_to_pump(Canvas):
    def __init__(self,parent):
        super().__init__(parent)
        logger.debug("Create "+str(page_name)+" canvas")

        self.text_confirmation_string = "Please make sure that you already finished the anastomosis and take off the clamp before you activate the pump. \nTimestamp and camera recording will be automatically stopped and saved into history. \nDo you wish to continue?"

        self.config(
            bg = "#F2F2F2",
            height = 480,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

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
            text=self.text_confirmation_string,
            fill="#000000",
            font=("Inter",-30,"bold"),
            justify='center',
            width=760
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        self.button_to_pump = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_to_pump.place(
            x=410.0,
            y=350.0,
            width=370.0,
            height=100.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets(page_name,"button_2.png"))
        self.button_to_anastomosis = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_to_anastomosis.place(
            x=20.0,
            y=350.0,
            width=370.0,
            height=100.0
        )


