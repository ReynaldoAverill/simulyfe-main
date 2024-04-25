
import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets
page_name = "page_main"
logger = logging.getLogger(__name__)

class Page_main(Canvas):
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

        self.place(x = 0, y = 0)

        image_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"image_1.png"))
        image_1 = self.create_image(
            400.0,
            240.0,
            image=image_image_1
        )

        # button_image_1 = PhotoImage(
        #     file=relative_to_assets(page_name,"button_1.png"))
        # button_1 = Button(self,
        #     image=button_image_1,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     # command=lambda: canvas2.place(x=0,y=0),
        #     relief="flat"
        # )
        # button_1.place(
        #     x=200.0,
        #     y=205.0,
        #     width=400.0,
        #     height=100.0
        # )

        button_image_2 = PhotoImage(
        file=relative_to_assets(page_name,"button_2.png"))

        button_2b = Button(self,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: self2.tkraise(),
            relief="flat"
        )
        button_2b.place(
            x=200.0,
            y=346.0,
            width=400.0,
            height=100.0
        )

        button_2b.config(command=lambda: print("button_3 clicked"))

        button_image_3 = PhotoImage(
            file=relative_to_assets(page_name,"button_3.png"))
        button_3 = Button(self,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: parent.destroy(),
            relief="flat"
        )
        button_3.place(
            x=35.0,
            y=346.0,
            width=100.0,
            height=100.0
        )
        logger.debug(str(page_name)+" canvas created")
        # parent.mainloop()




