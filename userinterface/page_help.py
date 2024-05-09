import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets

page_name = "page_help"
logger = logging.getLogger(__name__)

class Page_help(Canvas):
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
        self.button_to_app_guide = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_app_guide clicked"),
            relief="flat"
        )

        self.button_to_app_guide.place(
            x=420.0,
            y=140.0,
            width=340.0,
            height=200.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets(page_name,"button_2.png"))
        self.button_to_anastomosis_guide = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_anastomosis_guide clicked"),
            relief="flat"
        )
        self.button_to_anastomosis_guide.place(
            x=40.0,
            y=140.0,
            width=340.0,
            height=200.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets(page_name,"button_3.png"))
        self.button_to_other_menu = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_other_menu clicked"),
            relief="flat"
        )
        self.button_to_other_menu.place(
            x=50.0,
            y=40.0,
            width=100.0,
            height=60.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"image_1.png"))
        self.image_1 = self.create_image(
            400.0,
            241.0,
            image=self.image_image_1
        )
