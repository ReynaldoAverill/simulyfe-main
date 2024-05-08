import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets

page_name = "page_action_history"
logger = logging.getLogger(__name__)

class Page_action_history(Canvas):
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
        self.button_to_other_menu = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_to_other_menu.place(
            x=50.0,
            y=40.0,
            width=100.0,
            height=60.0
        )

        self.create_text(
            175.0,
            40.0,
            anchor="nw",
            text="ACTION HISTORY",
            fill="#1C666F",
            font=("Inter Bold", 40 * -1)
        )

        self.create_rectangle(
            100.0,
            370.0,
            700.0,
            445.0,
            fill="#000000",
            outline="")

        self.create_rectangle(
            100.0,
            370.0,
            160.0,
            445.0,
            fill="#1C666F",
            outline="")

        self.create_rectangle(
            160.0,
            370.0,
            700.0,
            408.0,
            fill="#717171",
            outline="")

        self.create_rectangle(
            430.0,
            408.0,
            700.0,
            445.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            100.0,
            370.0,
            anchor="nw",
            text="1",
            fill="#FFFFFF",
            font=("Inter Bold", 40 * -1)
        )

        self.create_text(
            280.0,
            370.0,
            anchor="nw",
            text="Time Elapsed: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            430.0,
            370.0,
            anchor="nw",
            text="HH:MM:SS",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            175.0,
            408.0,
            anchor="nw",
            text="Debit Accuracy: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            345.0,
            408.0,
            anchor="nw",
            text="xxx%",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            430.0,
            408.0,
            anchor="nw",
            text="Suturing Force Avg: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            630.0,
            408.0,
            anchor="nw",
            text="Weak",
            fill="#00FF00",
            font=("Inter Bold", 20 * -1)
        )

        self.create_rectangle(
            100.0,
            255.0,
            700.0,
            330.0,
            fill="#000000",
            outline="")

        self.create_rectangle(
            100.0,
            255.0,
            160.0,
            330.0,
            fill="#1C666F",
            outline="")

        self.create_rectangle(
            160.0,
            255.0,
            700.0,
            293.0,
            fill="#717171",
            outline="")

        self.create_rectangle(
            430.0,
            293.0,
            700.0,
            330.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            100.0,
            255.0,
            anchor="nw",
            text="2",
            fill="#FFFFFF",
            font=("Inter Bold", 40 * -1)
        )

        self.create_text(
            280.0,
            255.0,
            anchor="nw",
            text="Time Elapsed: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            430.0,
            255.0,
            anchor="nw",
            text="HH:MM:SS",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            175.0,
            293.0,
            anchor="nw",
            text="Debit Accuracy: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            345.0,
            293.0,
            anchor="nw",
            text="xxx%",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            430.0,
            293.0,
            anchor="nw",
            text="Suturing Force Avg: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            630.0,
            293.0,
            anchor="nw",
            text="Med",
            fill="#FFF400",
            font=("Inter Bold", 20 * -1)
        )

        self.create_rectangle(
            100.0,
            140.0,
            700.0,
            215.0,
            fill="#000000",
            outline="")

        self.create_rectangle(
            100.0,
            140.0,
            160.0,
            215.0,
            fill="#1C666F",
            outline="")

        self.create_rectangle(
            160.0,
            140.0,
            700.0,
            178.0,
            fill="#717171",
            outline="")

        self.create_rectangle(
            430.0,
            178.0,
            700.0,
            215.0,
            fill="#BFDDD2",
            outline="")

        self.create_text(
            100.0,
            140.0,
            anchor="nw",
            text="3",
            fill="#FFFFFF",
            font=("Inter Bold", 40 * -1)
        )

        self.create_text(
            280.0,
            140.0,
            anchor="nw",
            text="Time Elapsed: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            430.0,
            140.0,
            anchor="nw",
            text="HH:MM:SS",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            175.0,
            178.0,
            anchor="nw",
            text="Debit Accuracy: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            345.0,
            178.0,
            anchor="nw",
            text="xxx%",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            430.0,
            178.0,
            anchor="nw",
            text="Suturing Force Avg: ",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.create_text(
            630.0,
            178.0,
            anchor="nw",
            text="Strong",
            fill="#FF0000",
            font=("Inter Bold", 20 * -1)
        )