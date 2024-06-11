import logging
from tkinter import Canvas, Entry, Text, Button, PhotoImage, Label
from .userinterface_tools import relative_to_assets

page_name = "page_anastomosis_suturing_force"
logger = logging.getLogger(__name__)

class Page_anastomosis_suturing_force(Canvas):
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
        self.text_stopwatch_time = "00:00:00:00"
        self.text_camera_connectionstatus = "DISCONNECTED"
        self.text_camera_recordingstatus = "NOT RECORDING"
        self.text_suturing_force_measured_left = "STRONG"
        self.text_suturing_force_measured_right = "MEDIUM"

        # Force measurement result (Left)
        self.create_rectangle(
            20,
            20,
            20+370,
            20+110,
            fill="#BFDDD2",
            outline="")
        
        self.create_text(
            20+200/2,20+110/2,
            anchor="c",
            text="FORCE\n(LEFT)",
            fill="#000000",
            font=("Inter",30*-1,"bold"),
            width=200,
            justify="center"
        )        

        self.box_suturing_force_left = self.create_rectangle(
            230,
            30,
            230+150,
            30+90,
            fill="#FF0000",
            outline="")
        
        self.text_suturing_force_left = self.create_text(
            220+170/2,20+110/2,
            anchor="c",
            text=self.text_suturing_force_measured_left,
            fill="#000000",
            font=("Inter",30*-1,"bold"),
            width=150,
            justify="center"
        )
        # self.itemconfigure(self.box_suturing_force_left,fill="#FFF500")

        # self.box_suturing_force_left.itemconfigure(fill="#FFF500")

        # Force measurement result (Right)
        self.create_rectangle(
            410,
            20,
            410+370,
            20+110,
            fill="#BFDDD2",
            outline="")
        
        self.create_text(
            580+200/2,20+110/2,
            anchor="c",
            text="FORCE\n(RIGHT)",
            fill="#000000",
            font=("Inter",30*-1,"bold"),
            width=200,
            justify="center"
        )        

        self.box_suturing_force_right = self.create_rectangle(
            420,
            30,
            420+150,
            30+90,
            fill="#FFF500",
            outline="")
        
        self.text_suturing_force_right = self.create_text(
            410+170/2,20+110/2,
            anchor="c",
            text=self.text_suturing_force_measured_right,
            fill="#000000",
            font=("Inter",30*-1,"bold"),
            width=150,
            justify="center"
        )

        # Measurement bar
        # self.create_rectangle(
        #     40.0,
        #     40.0,
        #     220.0,
        #     110.0,
        #     fill="#00FF00",
        #     outline="")

        # self.create_rectangle(
        #     220.0,
        #     40.0,
        #     400.0,
        #     110.0,
        #     fill="#FFF400",
        #     outline="")

        # self.create_rectangle(
        #     400.0,
        #     40.0,
        #     580.0,
        #     110.0,
        #     fill="#FF0000",
        #     outline="")
        
        # self.create_rectangle(
        #     20.0,
        #     20.0,
        #     60.0,
        #     130.0,
        #     fill="#1C666F",
        #     outline="")
        
        # self.text_suturing_force = self.create_text(
        #     620.0,
        #     55.0,
        #     anchor="nw",
        #     text=self.text_suturing_force_measured,
        #     fill="#00FF00",
        #     font=("Inter Bold", 30 * -1)
        # )

        # Decorator rectangle
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
        
        # Box for stopwatch

        self.create_rectangle(
            200,
            150.0,
            600.0,
            260.0,
            fill="#5DA295",
            outline="")

        # self.create_rectangle(
        #     620.0,
        #     150.0,
        #     780.0,
        #     260.0,
        #     fill="#5DA295",
        #     outline="")

        # self.create_text(
        #     120,205,
        #     anchor="c",
        #     text="TIME ELAPSED",
        #     fill="#FFFFFF",
        #     font=('Inter',-40,'bold'),
        #     width=200,
        #     justify="center"
        # )

        self.text_stopwatch = self.create_text(
            200+400/2,150+110/2,
            anchor="c",
            text=self.text_stopwatch_time,
            fill="#FFFFFF",
            font=('Inter', 55 * -1,'bold'),
            width=380,
            justify="left"
        )

        # self.text_stopwatch_time = "11:22:33:44"
        # self.itemconfigure(self.text_stopwatch,text=self.text_stopwatch_time)

        # self.config(self.text_stopwatch,text=self.text_stopwatch_time)

        # self.create_text(
        #     700,
        #     170,
        #     anchor="c",
        #     text="CAMERA",
        #     fill="#FFFFFF",
        #     font=("Inter", 30 * -1,"bold"),
        #     width=160,
        #     justify="center"
        # )

        # self.create_text(
        #     700,
        #     210,
        #     anchor="c",
        #     text=self.text_camera_connectionstatus,
        #     fill="#FF0000",
        #     font=("Inter", 15 * -1,"bold"),
        #     width=160,
        #     justify="center"
        # )

        # self.create_text(
        #     700,
        #     245,
        #     anchor="c",
        #     text=self.text_camera_recordingstatus,
        #     fill="#FF0000",
        #     font=("Inter", 15 * -1,"bold"),
        #     width=160,
        #     justify="center"
        # )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets(page_name,"button_1.png"))
        self.button_confirmation_to_main = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_confirmation_to_main clicked"),
            relief="flat"
        )
        self.button_confirmation_to_main.place(
            x=20.0,
            y=315.0,
            width=100.0,
            height=100.0
        )
        self.itemconfig=()
        self.button_image_2 = PhotoImage(
            file=relative_to_assets(page_name,"button_2.png"))
        self.button_confirmation_to_pump = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_confirmation_to_pump clicked"),
            relief="flat"
        )
        self.button_confirmation_to_pump.place(
            x=680.0,
            y=315.0,
            width=100.0,
            height=100.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets(page_name,"button_3.png"))
        self.button_to_anastomosis_stopwatch = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_anastomosis_stopwatch clicked"),
            relief="flat"
        )
        self.button_to_anastomosis_stopwatch.place(
            x=140.0,
            y=280.0,
            width=160.0,
            height=160.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets(page_name,"button_4.png"))
        self.button_to_anastomosis_suturing_force = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_anastomosis_suturing_force clicked"),
            relief="flat"
        )
        self.button_to_anastomosis_suturing_force.place(
            x=320.0,
            y=280.0,
            width=160.0,
            height=160.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets(page_name,"button_5.png"))
        self.button_to_anastomosis_camera = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_to_anastomosis_camera clicked"),
            relief="flat"
        )
        self.button_to_anastomosis_camera.place(
            x=500.0,
            y=280.0,
            width=160.0,
            height=160.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets(page_name,"button_6.png"))
        self.button_zero_left = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_zero_left clicked"),
            relief="flat"
        )
        self.button_zero_left.place(
            x=20,
            y=150,
            width=160.0,
            height=110.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets(page_name,"button_7.png"))
        self.button_zero_right = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_zero_right clicked"),
            relief="flat"
        )
        self.button_zero_right.place(
            x=620,
            y=150,
            width=160.0,
            height=110.0
        )