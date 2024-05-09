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

        self.text_default_debit_accuracy = "000 %"
        self.text_default_pump_state = "OFF"
        self.text_default_measured_debit_value = "xxx\nml/min"
        self.text_default_setpoint_debit_value = "xxx\nml/min"

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

        # Image for button when pump is turned_on
        self.button_image_5 = PhotoImage(
            file=relative_to_assets(page_name,"button_5.png"))

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
            120,
            205,
            anchor="c",
            text="DEBIT\nACCURACY",
            fill="#FFFFFF",
            font=("Inter", 30 * -1,"bold"),
            width=200,
            justify="center"
        )

        self.text_debit_accuracy = self.create_text(
            410,
            205,
            anchor="c",
            text=self.text_default_debit_accuracy,
            fill="#FFFFFF",
            font=("Inter", 60 * -1,"bold"),
            width=380,
            justify="center"
        )

        self.create_rectangle(
            620.0,
            150.0,
            780.0,
            260.0,
            fill="#5DA295",
            outline="")

        self.text_pump = self.create_text(
            700,
            240,
            anchor="c",
            text=self.text_default_pump_state,
            fill="#FF0000",
            font=("Inter", 30 * -1,"bold"),
            width=380,
            justify="center"
        )

        self.create_text(
            700,
            185,
            anchor="c",
            text="PUMP STATUS",
            fill="#FFFFFF",
            font=("Inter", 30 * -1,"bold"),
            width=160,
            justify="center"
        )

        self.create_rectangle(
            20.0,
            20.0,
            390.0,
            130.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            115,
            75,
            anchor="c",
            text="MEASURED DEBIT",
            fill="#000000",
            font=("Inter", 30 * -1,"bold"),
            width=180,
            justify="center"
        )

        self.text_measured_debit = self.create_text(
            300,
            75,
            anchor="c",
            text=self.text_default_measured_debit_value,
            fill="#000000",
            font=("Inter", 40 * -1,"bold"),
            width=370,
            justify="center"
        )

        self.create_rectangle(
            410.0,
            20.0,
            780.0,
            130.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            505,
            75,
            anchor="c",
            text="SETPOINT DEBIT",
            fill="#000000",
            font=("Inter", 30 * -1,"bold"),
            width=190,
            justify="center"
        )

        self.text_setpoint_debit = self.create_text(
            690,
            75,
            anchor="c",
            text=self.text_default_setpoint_debit_value,
            fill="#000000",
            font=("Inter", 40 * -1,"bold"),
            width=180,
            justify="center"
        )
    
    def pump_turned_on_view(self):
        self.button_change_pump_state.config(image=self.button_image_5)
        self.button_change_debit.place_forget()
    
    def pump_turned_off_view(self):
        self.button_change_pump_state.config(image=self.button_image_3)
        self.button_change_debit.place(
            x=410.0,
            y=285.0,
            width=160.0,
            height=160.0
        )