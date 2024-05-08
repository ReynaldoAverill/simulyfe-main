import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets

page_name = "page_pump"
logger = logging.getLogger(__name__)

class Page_pump(Canvas):
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

        self.create_rectangle(
            390.0,
            345.0,
            410.0,
            385.0,
            fill="#D9D9D9",
            outline=""
        )

        self.create_rectangle(
            210.0,
            345.0,
            230.0,
            385.0,
            fill="#D9D9D9",
            outline="")

        self.create_rectangle(
            570.0,
            345.0,
            590.0,
            385.0,
            fill="#D9D9D9",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        self.button_back_to_anastomosis = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_back_to_anastomosis.place(
            x=20.0,
            y=315.0,
            width=190.0,
            height=100.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets(page_name,"button_2.png"))
        self.button_finalize = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_finalize.place(
            x=590.0,
            y=315.0,
            width=190.0,
            height=100.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets(page_name,"button_3.png"))
        self.button_change_pump_state = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_change_pump_state.place(
            x=230.0,
            y=285.0,
            width=160.0,
            height=160.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets(page_name,"button_4.png"))
        self.button_change_debit = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_change_debit.place(
            x=410.0,
            y=285.0,
            width=160.0,
            height=160.0
        )

        self.create_rectangle(
            20.0,
            150.0,
            600.0,
            260.0,
            fill="#5DA295",
            outline="")

        self.create_text(
            22.0,
            180.0,
            anchor="nw",
            text="DEBIT\nACCURACY",
            fill="#FFFFFF",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            220.0,
            180.0,
            anchor="nw",
            text="xxx %",
            fill="#FFFFFF",
            font=("Inter Bold", 60 * -1)
        )

        self.create_rectangle(
            620.0,
            150.0,
            780.0,
            260.0,
            fill="#5DA295",
            outline="")

        self.create_text(
            620.0,
            225.0,
            anchor="nw",
            text="OFF",
            fill="#FFFFFF",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            620.0,
            151.0,
            anchor="nw",
            text="PUMP STATUS",
            fill="#FFFFFF",
            font=("Inter Bold", 30 * -1)
        )

        self.create_rectangle(
            20.0,
            20.0,
            390.0,
            130.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            22.0,
            50.0,
            anchor="nw",
            text="MEASURED DEBIT",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            212.0,
            50.0,
            anchor="nw",
            text="xx \nml/min",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        self.create_rectangle(
            410.0,
            20.0,
            780.0,
            130.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            410.0,
            50.0,
            anchor="nw",
            text="EXPECTED DEBIT",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            600.0,
            50.0,
            anchor="nw",
            text="xx \nml/min",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )