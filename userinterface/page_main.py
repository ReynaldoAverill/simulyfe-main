import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage
from .userinterface_tools import relative_to_assets
from model.model import Model

page_name = "page_main"
logger = logging.getLogger(__name__)

class Page_main(Canvas):
    def __init__(self,parent,model: Model):
        self.model = model
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
        
        # image_1
        self.image_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"image_1.png"))
        self.create_image(
            400.0,
            240.0,
            image=self.image_image_1
        )

        # button_start
        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        self.x = 7
        self.button_start = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_start clicked"),
            # command=lambda: self._moveto_page_anastomosis,
            relief="flat"
        )

        self.button_start.place(
            x=200.0,
            y=205.0,
            width=400.0,
            height=100.0
        )

        #  button_othermenu
        self.button_image_2 = PhotoImage(
        file=relative_to_assets(page_name,"button_2.png"))
        self.button_othermenu = Button(self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_othermenu clicked"),
            # command=lambda: self2.tkraise(),
            relief="flat"
        )

        self.button_othermenu.place(
            x=200.0,
            y=346.0,
            width=400.0,
            height=100.0
        )

        # self.button_start.config(command=lambda: print("button_start 2 clicked"))

        self.button_image_3 = PhotoImage(
            file=relative_to_assets(page_name,"button_3.png"))
        self.button_exit = Button(self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_exit clicked"),
            # command=lambda: parent.destroy(),
            relief="flat"
        )
        self.button_exit.place(
            x=35.0,
            y=346.0,
            width=100.0,
            height=100.0
        )
        logger.debug(str(page_name)+" canvas created")
        self.place(x = 0, y = 0)
        # parent.mainloop()

    def get_start_button(self):
        return self.x
    

    def _moveto_page_anastomosis(self):
        logger.debug("button start_pressed")
        self.model.user_state.page_anastomosis()

