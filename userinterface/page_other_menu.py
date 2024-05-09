import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets

page_name = "page_other_menu"
logger = logging.getLogger(__name__)

class Page_other_menu(Canvas):
    def __init__(self,parent):
        super().__init__(parent)
        logger.info("Create "+str(page_name)+" canvas")
        self.config(
            bg = "#F2F2F2",
            height = 480,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        self.button_to_setting = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_setting clicked"),
            relief="flat"
        )
        self.button_to_setting.place(
            x=550.0,
            y=140.0,
            width=200.0,
            height=200.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets(page_name,"button_2.png"))
        self.button_to_history = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_history clicked"),
            relief="flat"
        )
        self.button_to_history.place(
            x=50.0,
            y=140.0,
            width=200.0,
            height=200.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets(page_name,"button_3.png"))
        self.button_to_help = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_help clicked"),
            relief="flat"
        )
        self.button_to_help.place(
            x=300.0,
            y=140.0,
            width=200.0,
            height=200.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets(page_name,"button_4.png"))
        self.button_to_main = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_main clicked"),
            relief="flat"
        )
        self.button_to_main.place(
            x=50.0,
            y=40.0,
            width=100.0,
            height=60.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"image_1.png"))
        self.image_1 = self.create_image(
            400.0,
            240.0,
            image=self.image_image_1
        )
