import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage, Label
from .userinterface_tools import relative_to_assets

page_name = "page_training_summary"
logger = logging.getLogger(__name__)

class Page_training_summary(Canvas):
    def __init__(self,parent):
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

        self.create_text(
            0.0,
            0.0,
            anchor="nw",
            text="TRAINING SUMMARY",
            fill="#1C666F",
            font=("Inter Bold", 40 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        self.button_to_main = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_to_main.place(
            x=410.0,
            y=350.0,
            width=370.0,
            height=110.0
        )

        self.create_rectangle(
            410.0,
            90.0,
            780.0,
            200.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            410.0,
            119.0,
            anchor="nw",
            text="EXPECTED DEBIT",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            600.0,
            119.0,
            anchor="nw",
            text="xx \nml/min",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        self.create_rectangle(
            20.0,
            90.0,
            390.0,
            200.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            20.0,
            119.0,
            anchor="nw",
            text="MEASURED DEBIT",
            fill="#000000",
            font=("Inter", 30 * -1,"bold")
        )

        self.create_text(
            214.0,
            112.0,
            anchor="nw",
            text="xx \nml/min",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        self.create_rectangle(
            20.0,
            220.0,
            390.0,
            330.0,
            fill="#5DA295",
            outline="")

        self.create_text(
            20.0,
            249.0,
            anchor="nw",
            text="DEBIT\nACCURACY",
            fill="#FFFFFF",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            220.0,
            249.0,
            anchor="nw",
            text="xxx%",
            fill="#FFFFFF",
            font=("Inter Bold", 60 * -1)
        )

        self.create_rectangle(
            410.0,
            220.0,
            780.0,
            330.0,
            fill="#5DA295",
            outline="")

        self.create_text(
            410.0,
            249.0,
            anchor="nw",
            text="SUTURINGFORCE AVG",
            fill="#FFFFFF",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            610.0,
            249.0,
            anchor="nw",
            text="STRONG",
            fill="#FF0000",
            font=("Inter Bold", 30 * -1)
        )

        self.create_rectangle(
            22.0,
            350.0,
            392.0,
            460.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            22.0,
            350.0,
            anchor="nw",
            text="TIME ELAPSED",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            22.0,
            396.0,
            anchor="nw",
            text="HH:MM:SS",
            fill="#000000",
            font=("Inter Bold", 60 * -1)
        )