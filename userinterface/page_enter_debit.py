import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets

page_name = "page_enter_debit"
logger = logging.getLogger(__name__)

class Page_enter_debit(Canvas):
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
        self.button_dict = {}

        self.create_text(
            400.0,
            25.0,
            anchor="nw",
            text="ENTER EXPECTED DEBIT (ml/min)",
            fill="#1C666F",
            font=("Inter Bold", 40 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        button_finalize_debit = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_finalize_debit.place(
            x=400.0,
            y=350.0,
            width=380.0,
            height=105.0
        )
        self.button_dict.update({"button_finalize_debit" : button_finalize_debit})

        self.button_image_2 = PhotoImage(
            file=relative_to_assets(page_name,"button_2.png"))
        button_number_7 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_number_7.place(
            x=40.0,
            y=25.0,
            width=100.0,
            height=100.0
        )
        self.button_dict.update({"button_number_7" : button_number_7})

        self.button_image_3 = PhotoImage(
            file=relative_to_assets(page_name,"button_3.png"))
        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=40.0,
            y=135.0,
            width=100.0,
            height=100.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets(page_name,"button_4.png"))
        button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=40.0,
            y=245.0,
            width=100.0,
            height=100.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets(page_name,"button_5.png"))
        button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=150.0,
            y=135.0,
            width=100.0,
            height=100.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets(page_name,"button_6.png"))
        button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=150.0,
            y=245.0,
            width=100.0,
            height=100.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets(page_name,"button_7.png"))
        button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        button_7.place(
            x=150.0,
            y=355.0,
            width=100.0,
            height=100.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets(page_name,"button_8.png"))
        button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        button_8.place(
            x=40.0,
            y=355.0,
            width=100.0,
            height=100.0
        )

        self.button_image_9 = PhotoImage(
            file=relative_to_assets(page_name,"button_9.png"))
        button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        button_9.place(
            x=260.0,
            y=135.0,
            width=100.0,
            height=100.0
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets(page_name,"button_10.png"))
        button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        button_10.place(
            x=260.0,
            y=245.0,
            width=100.0,
            height=100.0
        )

        self.button_image_11 = PhotoImage(
            file=relative_to_assets(page_name,"button_11.png"))
        button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        button_11.place(
            x=150.0,
            y=25.0,
            width=100.0,
            height=100.0
        )

        self.button_image_12 = PhotoImage(
            file=relative_to_assets(page_name,"button_12.png"))
        button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        button_12.place(
            x=260.0,
            y=25.0,
            width=100.0,
            height=100.0
        )

        self.create_rectangle(
            400.0,
            150.0,
            780.0,
            300.0,
            fill="#000000",
            outline="")

        self.create_rectangle(
            410.0,
            160.0,
            770.0,
            290.0,
            fill="#000000",
            outline="")

        self.create_text(
            440.0,
            200.0,
            anchor="nw",
            text="123456",
            fill="#1C666F",
            font=("Inter Bold", 80 * -1)
        )        
