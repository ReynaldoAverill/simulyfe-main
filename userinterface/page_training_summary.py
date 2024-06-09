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

        self.text_default_setpoint_debit = "xx\nml/min"
        self.text_default_measured_debit = "xx\nml/min"
        self.text_default_debit_accuracy = "xxx %"
        self.text_suturing_force = "STRONG"
        self.text_stopwatch_default = "HH:MM:SS"

        self.create_text(
            400,
            45,
            anchor="c",
            text="TRAINING SUMMARY",
            fill="#1C666F",
            font=("Inter", 40 * -1,"bold"),
            justify="center",
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
            410+200/2,
            90+110/2,
            anchor="c",
            text="SETPOINT DEBIT",
            fill="#000000",
            font=("Inter", 30 * -1,"bold"),
            justify="center",
            width=200
        )

        self.text_setpoint_debit = self.create_text(
            610+170/2,
            90+110/2,
            anchor="c",
            text=self.text_default_setpoint_debit,
            fill="#000000",
            font=("Inter", 40 * -1,"bold"),
            justify="center",
            width=170
        )

        self.create_rectangle(
            20.0,
            90.0,
            390.0,
            200.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            120.0,
            145.0,
            anchor="c",
            text="MEASURED DEBIT",
            fill="#000000",
            font=("Inter", 30 * -1,"bold"),
            justify="center",
            width=200
        )
        
        self.text_measured_debit = self.create_text(
            220+170/2,
            90+110/2,
            anchor="c",
            text=self.text_default_measured_debit,
            fill="#000000",
            font=("Inter", 40 * -1,"bold"),
            justify="center",
            width=170
        )

        self.create_rectangle(
            20.0,
            220.0,
            390.0,
            330.0,
            fill="#5DA295",
            outline="")

        self.create_text(
            20.0+200/2,
            220.0+110/2,
            anchor="c",
            text="DEBIT\nACCURACY",
            fill="#FFFFFF",
            font=("Inter", 30 * -1,"bold"),
            justify="center",
            width=200
        )

        self.text_debit_accuracy = self.create_text(
            220.0+170/2,
            220.0+110/2,
            anchor="c",
            text=self.text_default_debit_accuracy,
            fill="#FFFFFF",
            font=("Inter", 50 * -1,"bold"),
            justify="center",
            width=170
        )

        self.create_rectangle(
            410.0,
            220.0,
            780.0,
            330.0,
            fill="#5DA295",
            outline="")

        self.create_text(
            410.0+200/2,
            220.0+110/2,
            anchor="c",
            text="SUTURING FORCE AVG",
            fill="#FFFFFF",
            font=("Inter", 30 * -1,"bold"),
            justify="center",
            width=200
        )

        self.create_text(
            610.0+170/2,
            220.0+110/2,
            anchor="c",
            text=self.text_suturing_force,
            fill="#FF0000",
            font=("Inter", 30 * -1,"bold"),
            justify="center",
            width=170
        )

        self.create_rectangle(
            22.0,
            350.0,
            392.0,
            460.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            20.0+370/2,
            355+50/2,
            anchor="c",
            text="TIME ELAPSED",
            fill="#000000",
            font=("Inter", 30 * -1,"bold"),\
            justify="center",
            width=370   
        )

        self.text_stopwatch = self.create_text(
            20.0+370/2,
            405+50/2,
            anchor="c",
            text=self.text_stopwatch_default,
            fill="#000000",
            font=("Inter", 50 * -1,"bold"),
            justify="center",
            width=370
        )