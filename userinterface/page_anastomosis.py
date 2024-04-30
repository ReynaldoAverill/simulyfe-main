import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets

page_name = "page_anastomosis"
logger = logging.getLogger(__name__)

class Page_anastomosis(Canvas):
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
        self.text_stopwatch_time = "00:00:00"
        self.text_camera_connectionstatus = "DISCONNECTED"
        self.text_camera_recordingstatus = "NOT RECORDING"

        self.create_rectangle(
            120.0,
            345.0,
            140.0,
            385.0,
            fill="#D9D9D9",
            outline="")

        self.create_rectangle(
            300.0,
            345.0,
            320.0,
            385.0,
            fill="#D9D9D9",
            outline="")

        self.create_rectangle(
            480.0,
            345.0,
            500.0,
            385.0,
            fill="#D9D9D9",
            outline="")

        self.create_rectangle(
            660.0,
            345.0,
            680.0,
            385.0,
            fill="#D9D9D9",
            outline="")

        self.create_rectangle(
            20.0,
            150.0,
            600.0,
            260.0,
            fill="#5DA295",
            outline="")

        self.create_rectangle(
            620.0,
            150.0,
            780.0,
            260.0,
            fill="#5DA295",
            outline="")

        self.create_text(
            120,205,
            anchor="c",
            text="TIME ELAPSED",
            fill="#FFFFFF",
            font=('Inter',-40,'bold'),
            width=200,
            justify="center"
        )

        self.create_text(
            410,205,
            anchor="c",
            text=self.text_stopwatch_time,
            fill="#FFFFFF",
            font=('Inter', 60 * -1,'bold'),
            width=380,
            justify="center"
        )

        self.create_text(
            620.0,
            151.0,
            anchor="nw",
            text="CAMERA",
            fill="#FFFFFF",
            font=("Inter Bold", 30 * -1)
        )

        self.create_text(
            620.0,
            191.0,
            anchor="nw",
            text="DISCONNECTED",
            fill="#FFFFFF",
            font=("Inter Bold", 15 * -1)
        )

        self.create_text(
            620.0,
            227.0,
            anchor="nw",
            text="NOT RECORDING",
            fill="#FFFFFF",
            font=("Inter Bold", 15 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        self.button_confirmation_to_main = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_confirmation_to_main.place(
            x=20.0,
            y=315.0,
            width=100.0,
            height=100.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets(page_name,"button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=680.0,
            y=315.0,
            width=100.0,
            height=100.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets(page_name,"button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=140.0,
            y=280.0,
            width=160.0,
            height=160.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets(page_name,"button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=320.0,
            y=280.0,
            width=160.0,
            height=160.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets(page_name,"button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=500.0,
            y=280.0,
            width=160.0,
            height=160.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets(page_name,"button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=20.0,
            y=20.0,
            width=240.0,
            height=110.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets(page_name,"button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=280.0,
            y=20.0,
            width=240.0,
            height=110.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets(page_name,"button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=540.0,
            y=20.0,
            width=240.0,
            height=110.0
        )
