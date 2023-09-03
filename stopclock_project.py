import customtkinter
import threading
import pygame
from datetime import datetime, timedelta
import time


pygame.mixer.init()
buzzer_sound = pygame.mixer.Sound("buzzersound.wav")
doh_sound = pygame.mixer.Sound("do.mp3")
mi_sound = pygame.mixer.Sound("mi.mp3")
soh_sound = pygame.mixer.Sound("soh.mp3")
minutes = 0
seconds = 0
seconds_24 = 0
milli_seconds = 0
lhs_points = 0
rhs_points = 0
quarter1_left = 0
quarter1_right = 0
quarter2_left = 0
quarter2_right = 0
current_bar = 0
current_bar1 = 0


running = True

class Shot_Clock_Timer:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        self.window = customtkinter.CTk()
        self.window.geometry("1200x600")
        self.window.title('Stop Clock')
        self.window.resizable(False, False)

        #frame  to put all thr widgets
        self.frame_containers = customtkinter.CTkFrame(self.window,width=800,height=590,)
        self.frame_containers.pack()

        #Label widgets
        ###################################################################################################
        ##################################################################################################
        self.milli_seconds_label = customtkinter.CTkLabel(self.frame_containers, font=("Ubuntu", 30, 'bold'),
                                                    text="",
                                                    text_color="red", )

        self.milli_seconds_label.place(relx=0.514, rely=0.24, )
        #24 shot clock
        self.shot_24_label = customtkinter.CTkLabel(self.frame_containers, font=("Ubuntu", 50, 'bold'), text="24",
                                                  text_color="red",fg_color="transparent")

        self.shot_24_label.place(relx=0.443, rely=0.2, )

        self.clock_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",
                                                  font=("Ubuntu", 100, 'bold'),
                                                  text="00:00", text_color="red")

        self.clock_label.place(relx=0.36, rely=0.02, )

        self.home_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",height=40,
                                                  font=("Ubuntu", 60, 'bold'),
                                                  text="Home", text_color="white")

        self.home_label.place(relx=0.15, rely=0.3, )

        self.home_label_scores = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent", height=50,width=70,
                                                 font=("Ubuntu", 100, 'bold'),
                                                 text="00", text_color="blue")

        self.home_label_scores.place(relx=0.17, rely=0.42, )

        self.foul_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",text_color="red",
                                                  font=("Ubuntu", 20, 'bold'),
                                                  text="FOULS")

        self.foul_label.place(relx=0.46, rely=0.60, )

        self.lefty_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",
                                                 font=("Ubuntu", 30, 'bold',"italic"),
                                                 text="lefty.com", text_color="white")

        self.lefty_label.place(relx=0.42, rely=0.34, )


        self.away_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",
                                                  font=("Ubuntu", 60, 'bold'),
                                                  text="Away", text_color="white")

        self.away_label.place(relx=0.67, rely=0.3, )

        self.away_label_scores = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent", height=50, width=70,
                                                        font=("Ubuntu", 100, 'bold'),
                                                        text="00", text_color="blue")

        self.away_label_scores.place(relx=0.69, rely=0.42, )

        self.clock_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",
                                                  font=("Ubuntu", 100, 'bold'),
                                                  text="00:00", text_color="red")

        self.clock_label.place(relx=0.36, rely=0.02, )

        """self.clock_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",
                                                  font=("Ubuntu", 100, 'bold'),
                                                  text="00:00", text_color="red")

        self.clock_label.place(relx=0.36, rely=0.02, )

        self.clock_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",
                                                  font=("Ubuntu", 100, 'bold'),
                                                  text="00:00", text_color="red")

        self.clock_label.place(relx=0.36, rely=0.02, )

        self.clock_label = customtkinter.CTkLabel(self.frame_containers, fg_color="transparent",
                                                  font=("Ubuntu", 100, 'bold'),
                                                  text="00:00", text_color="red")

        self.clock_label.place(relx=0.36, rely=0.02, )"""
        ###################################################################################################
        ###################################################################################################

        #Labels for 1st quarter scores
        self.qrt1_label = customtkinter.CTkLabel(self.frame_containers,
                                                  font=("Ubuntu", 50, 'bold'),
                                                  text="1st", text_color="teal")

        self.qrt1_label.place(relx=0.08, rely=0.73, )

        self.lqrt1_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                 font=("Ubuntu", 60, 'bold'),
                                                 text="00", text_color="orange")

        self.lqrt1_label_scores.place(relx=0.035, rely=0.85)

        self.div_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 50, 'bold'),
                                                        text=":", text_color="orange")

        self.div_label_scores.place(relx=0.12, rely=0.85)

        self.rqrt1_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 60, 'bold'),
                                                        text="00", text_color="orange")

        self.rqrt1_label_scores.place(relx=0.14, rely=0.85)

        #labels for 2nd quarters
        self.qrt2_label = customtkinter.CTkLabel(self.frame_containers,
                                                  font=("Ubuntu", 50, 'bold'),
                                                  text="2nd", text_color="teal")

        self.qrt2_label.place(relx=0.33, rely=0.73, )

        self.lqrt2_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 60, 'bold'),
                                                        text="00", text_color="orange")

        self.lqrt2_label_scores.place(relx=0.3, rely=0.85)


        self.div2_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 50, 'bold'),
                                                        text=":", text_color="orange")

        self.div2_label_scores.place(relx=0.3815, rely=0.85)

        self.rqrt2_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 60, 'bold'),
                                                        text="00", text_color="orange")

        self.rqrt2_label_scores.place(relx=0.401, rely=0.85)


        #Labels for 3rd quarter
        self.qrt3_label = customtkinter.CTkLabel(self.frame_containers,
                                                  font=("Ubuntu", 50, 'bold'),
                                                  text="3rd", text_color="teal")

        self.qrt3_label.place(relx=0.6, rely=0.73, )

        self.lqrt3_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 60, 'bold'),
                                                        text="00", text_color="orange")

        self.lqrt3_label_scores.place(relx=0.56, rely=0.85)


        self.div3_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 50, 'bold'),
                                                        text=":", text_color="orange")

        self.div3_label_scores.place(relx=0.64, rely=0.85)

        self.rqrt3_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 60, 'bold'),
                                                        text="00", text_color="orange")

        self.rqrt3_label_scores.place(relx=0.659, rely=0.85)


        #Labels for 4th quarter
        self.qrt4_label = customtkinter.CTkLabel(self.frame_containers,
                                                  font=("Ubuntu", 50, 'bold'),
                                                  text="4rt", text_color="teal")

        self.qrt4_label.place(relx=0.83, rely=0.73, )

        self.lqrt4_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 60, 'bold'),
                                                        text="00", text_color="orange")

        self.lqrt4_label_scores.place(relx=0.79, rely=0.85)

        self.div4_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                        font=("Ubuntu", 50, 'bold'),
                                                        text=":", text_color="orange")

        self.div4_label_scores.place(relx=0.87, rely=0.85)

        self.rqrt4_label_scores = customtkinter.CTkLabel(self.frame_containers,
                                                         font=("Ubuntu", 60, 'bold'),
                                                         text="00", text_color="orange")

        self.rqrt4_label_scores.place(relx=0.889, rely=0.85)


        #24 seconds shot clock
        self.lside_shot_24_label = customtkinter.CTkLabel(self.window, font=("Ubuntu", 120, 'bold'), text="24",
                                                    text_color="red", fg_color="transparent",width=180,height=180)

        self.lside_shot_24_label.place(relx=0.001, rely=0.6, )

        #self.lside_shot_24ml_label = customtkinter.CTkLabel(self.window, font=("Ubuntu", 30, 'bold'), text=".0",
        #                                                  text_color="red", fg_color="black",)

        #self.lside_shot_24ml_label.place(relx=0.13, rely=0.77, )



        self.rside_shot_24_label = customtkinter.CTkLabel(self.window, font=("Ubuntu", 120, 'bold'), text="24",
                                                    text_color="red", fg_color="transparent",width=180,height=180)

        self.rside_shot_24_label.place(relx=0.84, rely=0.02, )

        #####################################################################################################
        #####################################################################################################
        # Buuton to trigger the start and pause
        self.add_minute_button = customtkinter.CTkButton(self.frame_containers, command=self.add_minute, width=50,
                                                    text="+min", fg_color="#37FD12",text_color="black", font=("helvetica", 24))
        self.add_minute_button.place(relx=0.02, rely=0.02)

        self.minus_minute_button = customtkinter.CTkButton(self.frame_containers, command=self.minus_minute, width=50,
                                                         text="-min", fg_color="#37FD12",text_color="black", font=("helvetica", 24))
        self.minus_minute_button.place(relx=0.02, rely=0.09)

        self.add_sec_button = customtkinter.CTkButton(self.frame_containers, command=self.add_seconds,
                                                 text="+sec", width=50,fg_color="#37FD12",text_color="black", )
        self.add_sec_button.place(relx=0.8, rely=0.02, )

        self.minus_sec_button = customtkinter.CTkButton(self.frame_containers, command=self.minus_seconds,
                                                      text="-sec",  width=50,fg_color="#37FD12",text_color="black", )
        self.minus_sec_button.place(relx=0.8, rely=0.09, )

        self.reset_button = customtkinter.CTkButton(self.window, command=self.reset_timer,
                                               text="Reset", state="raised", width=100)
        self.reset_button.place(relx=0.87, rely=0.7)

        self.start_button = customtkinter.CTkButton(self.window, command=self.start_pause, width=150,height=40,
                                               text="Start", font=("helvetica", 24,"bold"))
        self.start_button.place(relx=0.85, rely=0.9)

        self.teamname_button = customtkinter.CTkButton(self.window,height=50,  width=100,text_color="orange",command=self.team_tab,
                                               text="Teams", font=("helvetica", 24,"bold"),fg_color="teal")
        self.teamname_button.place(relx=0.01, rely=0.13)

        self.buzzer_button = customtkinter.CTkButton(self.window, corner_radius=10,
                                                  width=50,command=self.playsound,
                                                 text="Buzzer",  font=("helvetica", 24))
        self.buzzer_button.place(relx=0.87, rely=0.6)

        self.scores_button = customtkinter.CTkButton(self.window, corner_radius=5,command=self.opentab,
                                                     width=100,height=50,hover_color="#c23728",fg_color="teal",
                                                     text="Scores", font=("helvetica", 24))
        self.scores_button.place(relx=0.01, rely=0.02)

        self.done_button = customtkinter.CTkButton(self.window, corner_radius=5, command=self.place_scores,fg_color="green",
                                                     width=50,height=50,text_color="orange",hover_color="#e60049",
                                                     text="Done", font=("Gothic", 24))
        self.done_button.place(relx=0.1, rely=0.02)

        self.add_team_button = customtkinter.CTkButton(self.window, corner_radius=5, command=self.place_teamnames,
                                                   width=50,height=50,fg_color="green",text_color="#e6d800",
                                                   text="Display", font=("Arial", 18))
        self.add_team_button.place(relx=0.1, rely=0.13)

        ######################################################################################################
        ####################################################################################################
        self.plus3_LHS_button = customtkinter.CTkButton(self.frame_containers,width=50,text="+3",text_color="#00FF2F",
                                                        command=self.plus3_LHS,fg_color="#800000",
                                                        corner_radius=10,font=("helvetica",24))
        self.plus3_LHS_button.place(relx=0.02,rely=0.42)

        self.plus2_LHS_button = customtkinter.CTkButton(self.frame_containers, width=50, text="+2",text_color="#00FF2F",
                                                        command=self.plus2_LHS,fg_color="#480062",
                                                     corner_radius=10, font=("helvetica", 24))
        self.plus2_LHS_button.place(relx=0.02, rely=0.49)

        self.plus1_LHS_button = customtkinter.CTkButton(self.frame_containers, width=50, text="+1",
                                                        command=self.plus1_LHS,fg_color="#000080",text_color="#00FF2F",
                                                        corner_radius=10, font=("helvetica", 24))
        self.plus1_LHS_button.place(relx=0.02, rely=0.56)



        self.plus3_RHS_button = customtkinter.CTkButton(self.frame_containers, width=50, text="+3",
                                                        command=self.plus3_RHS,fg_color="#800000",text_color="#00FF2F",
                                                        corner_radius=10, font=("helvetica", 24))
        self.plus3_RHS_button.place(relx=0.92, rely=0.42)

        self.plus2_RHS_button = customtkinter.CTkButton(self.frame_containers, width=50, text="+2",
                                                       command=self.plus2_RHS,text_color="#00FF2F",fg_color="#480062",
                                                     corner_radius=10, font=("helvetica", 24))
        self.plus2_RHS_button.place(relx=0.92, rely=0.49)

        self.plus1_RHS_button = customtkinter.CTkButton(self.frame_containers, width=50, text="+1",
                                                        command=self.plus1_RHS,text_color="#00FF2F",fg_color="#000080",
                                                     corner_radius=10, font=("helvetica", 24))
        self.plus1_RHS_button.place(relx=0.92, rely=0.56)

        #colors = ["green", "#37FD12", "#7FFF00", "#FFFF00", "#FF0000"]

        self.button_14 = customtkinter.CTkButton(self.frame_containers, command=self.button_14, width=50,
                                                 corner_radius=10,fg_color="#37FD12",text_color="black",
                                                 text="14", font=("helvetica", 24))
        self.button_14.place(relx=0.02, rely=0.15)

        self.button_24 = customtkinter.CTkButton(self.frame_containers,corner_radius=10,
                                                 command=self.button_24, width=50,fg_color="#37FD12",text_color="black",
                                                 text="24", font=("helvetica", 24))
        self.button_24.place(relx=0.02, rely=0.22)

        self.plus_24_secs = customtkinter.CTkButton(self.frame_containers, corner_radius=5,command=self.plus_secs_24,
                                                  width=50, font=("helvetica", 22),fg_color="#37FD12",text_color="black",
                                                 text="+secs", state="raised", )
        self.plus_24_secs.place(relx=0.89, rely=0.02)

        self.minus_24_secs = customtkinter.CTkButton(self.frame_containers, corner_radius=5,command=self.minus_secs_24,
                                                  width=50, font=("helvetica", 24),fg_color="#37FD12",text_color="black",
                                                 text="-secs")
        self.minus_24_secs.place(relx=0.89, rely=0.09)
        ###########################################################################################################
        #####################################################################################################


        colors = ["green", "#37FD12", "#7FFF00","#FFFF00","#FF0000"]

        #Left hand side progress bars
        self.percent1 = customtkinter.IntVar()
        self.bar = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                progress_color=colors[0],
                                                width=50,
                                                mode="determinate", variable=self.percent1)
        self.bar.place(relx=0.36, rely=0.61)
        self.percent1.set(0)
        self.bar['variable'] = self.percent1

        self.percent2 = customtkinter.IntVar()
        self.bar2 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                 progress_color=colors[1],
                                                 determinate_speed=5,
                                                 width=60,
                                                 mode="determinate", variable=self.percent2)
        self.bar2.place(relx=0.36, rely=0.57)
        self.percent2.set(0)
        self.bar2['variable'] = self.percent2

        self.percent3 = customtkinter.IntVar()
        self.bar3 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                 progress_color=colors[2],
                                                 determinate_speed=15,
                                                 width=70,
                                                 mode="determinate", variable=self.percent3)
        self.bar3.place(relx=0.36, rely=0.53)
        self.percent3.set(0)
        self.bar3['variable'] = self.percent3


        self.percent4 = customtkinter.IntVar()
        self.bar4 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                 progress_color=colors[3],
                                                 determinate_speed=15,
                                                 width=80,
                                                 mode="determinate", variable=self.percent4)
        self.bar4.place(relx=0.36, rely=0.49)
        self.percent4.set(0)
        self.bar4['variable'] = self.percent4


        self.percent5 = customtkinter.IntVar()
        self.bar5 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                 progress_color=colors[4],
                                                 determinate_speed=15,
                                                 width=90,
                                                 mode="determinate", variable=self.percent5)
        self.bar5.place(relx=0.36, rely=0.45)
        self.percent5.set(0)
        self.bar5['variable'] = self.percent5
        #########################################################################################################

        #Right hand side progress bars

        self.percent6 = customtkinter.IntVar()
        self.bar6 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                progress_color=colors[0],
                                                width=50,
                                                mode="determinate", variable=self.percent6)
        self.bar6.place(relx=0.574, rely=0.61)
        self.percent6.set(0)
        self.bar6['variable'] = self.percent6

        self.percent7 = customtkinter.IntVar()
        self.bar7 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                 progress_color=colors[1],
                                                 determinate_speed=5,
                                                 width=60,
                                                 mode="determinate", variable=self.percent7)
        self.bar7.place(relx=0.562, rely=0.57)
        self.percent7.set(0)
        self.bar7['variable'] = self.percent7

        self.percent8 = customtkinter.IntVar()
        self.bar8 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                 progress_color=colors[2],
                                                 determinate_speed=15,
                                                 width=70,
                                                 mode="determinate", variable=self.percent8)
        self.bar8.place(relx=0.55, rely=0.53)
        self.percent8.set(0)
        self.bar8['variable'] = self.percent8

        self.percent9 = customtkinter.IntVar()
        self.bar9 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                 progress_color=colors[3],
                                                 determinate_speed=15,
                                                 width=80,
                                                 mode="determinate", variable=self.percent9)
        self.bar9.place(relx=0.537, rely=0.49)
        self.percent9.set(0)
        self.bar9['variable'] = self.percent9

        self.percent10 = customtkinter.IntVar()
        self.bar10 = customtkinter.CTkProgressBar(self.frame_containers, height=15, orientation="horizontal",
                                                 progress_color=colors[4],
                                                 determinate_speed=15,
                                                 width=90,
                                                 mode="determinate", variable=self.percent10)
        self.bar10.place(relx=0.525, rely=0.45)
        self.percent10.set(0)
        self.bar10['variable'] = self.percent10

        #Button to call the progress left bars
        self.bar_button1 = customtkinter.CTkButton(self.window, command=self.increase_bar1,width=100,text="Team1 fouls",
                                                   fg_color='green')
        self.bar_button1.place(relx=0.01,rely=0.23)

        #Button to call the progress right bars

        self.bar_button2 = customtkinter.CTkButton(self.window, command=self.increase_bar2, width=100,
                                                   text="Team2 fouls",fg_color="green")
        self.bar_button2.place(relx=0.01, rely=0.30)

        self.bar_reset_button =customtkinter.CTkButton(self.window, command=self.reset_bars,
                                                       height=50, width=100,fg_color="#37FD12",text_color="black",
                                                   text="Reset fouls",font=("helvetica",24))
        self.bar_reset_button.place(relx=0.03, rely=0.37)

        #self.progress_label = customtkinter.CTkLabel(self.frame_containers,text="")
        #self.progress_label.place(relx=0.4, rely=0.5)

        self.window.mainloop()
        ######################################################################################################
        ####################################################################################################

    #colors = ["green", "#37FD12", "#7FFF00", "#FFFF00", "#FF0000"]

    def increase_bar1(self):
        global current_bar
        current_bar += 1
        if current_bar == 1:
            self.percent1.set(self.percent1.get()+20)
            self.bar_button1.configure(fg_color="green",font=("helvetica",14,))
            #self.bar.start()

        elif current_bar == 2:
            self.percent2.set(self.percent1.get()+20)
            self.bar_button1.configure(fg_color="#37FD12",text_color="black",font=("helvetica",18,))
            #self.bar2.start()

        elif current_bar == 3:
            self.percent3.set(self.percent3.get()+20)
            self.bar_button1.configure(fg_color="#7FFF00", text_color="black", font=("helvetica", 22,))
            #self.bar3.start()


        elif current_bar == 4:
            self.percent4.set(self.percent4.get()+20)
            self.bar_button1.configure(fg_color="#FFFF00", text_color="black", font=("helvetica", 26,))

        elif current_bar == 5:
            self.percent5.set(self.percent5.get()+20)
            self.bar_button1.configure(fg_color="#FF0000", text_color="black", font=("helvetica", 30,))

        else:
            self.percent1.set(0)
            self.percent2.set(0)
            self.percent3.set(0)
            self.percent4.set(0)
            self.percent5.set(0)
            self.bar_button1.configure(text_color="white",font=("helvetica", 14),fg_color="green",)
            current_bar = 0
        ###############################################################################################


    def increase_bar2(self):
        global current_bar1
        current_bar1 += 1
        if current_bar1 == 1:
            self.percent6.set(self.percent6.get() + 20)
            self.bar_button2.configure(fg_color="green", font=("helvetica", 14,))


        elif current_bar1 == 2:
            self.percent7.set(self.percent7.get() + 20)
            self.bar_button2.configure(fg_color="#37FD12", text_color="black", font=("helvetica", 18,))
            # self.bar2.start()

        elif current_bar1 == 3:
            self.percent8.set(self.percent8.get() + 20)
            self.bar_button2.configure(fg_color="#7FFF00", text_color="black", font=("helvetica", 22,))
            # self.bar3.start()
        elif current_bar1 == 4:
            self.percent9.set(self.percent9.get() + 20)
            self.bar_button2.configure(fg_color="#FFFF00", text_color="black", font=("helvetica", 26,))

        elif current_bar1 == 5:
            self.percent10.set(self.percent10.get() + 20)
            self.bar_button2.configure(fg_color="#FF0000", text_color="black", font=("helvetica", 30,))
        else:
            self.bar_button2.configure(fg_color="green", text_color="white", font=("helvetica", 14,))
            self.percent6.set(0)
            self.percent7.set(0)
            self.percent8.set(0)
            self.percent9.set(0)
            self.percent10.set(0)
            current_bar1 = 0

    ######################################################################################################
    def reset_bars(self):
        for widget in self.frame_containers.winfo_children():
            if isinstance(widget, customtkinter.CTkProgressBar):
                widget.set(value=0)
                self.bar_button2.configure(fg_color="green", text_color="white", font=("helvetica", 14,))
                self.bar_button1.configure(fg_color="green", text_color="white", font=("helvetica", 14,))
     ###################################################################################################
    #####################################################################################################
    ###Update names of team label
    def team_tab(self):
            self.tabview_team = customtkinter.CTkTabview(self.frame_containers, width=300, height=100)
            self.tabview_team.place(relx=0.3, rely=0.4)
            self.tabview_team.add("Teams")
            self.tabview_team.add("Team2")

            self.team_entry_left1 = customtkinter.CTkEntry(self.tabview_team.tab("Teams"), corner_radius=5,
                                                      width=100, height=30, font=("Helvetica", 30), text_color="cyan")
            self.team_entry_left1.place(relx=0.03, rely=0.1)

            self.versus_label1 = customtkinter.CTkLabel(self.tabview_team.tab("Teams"), text="vs", height=50, width=5,
                                                         font=(None, 30))
            self.versus_label1.place(relx=0.45, rely=0.1)

            self.team_entry_right1 = customtkinter.CTkEntry(self.tabview_team.tab("Teams"), corner_radius=5,
                                                       width=100, height=30, font=("Helvetica", 30), text_color="cyan")
            self.team_entry_right1.place(relx=0.6, rely=0.1)

    ######################################################################################################
    ####################################################################################################

    def opentab(self):
            self.tabview = customtkinter.CTkTabview(self.frame_containers, width=100, height=120)
            self.tabview.place(relx=0.4, rely=0.4)
            self.tabview.add("1st")
            self.tabview.add("2nd")
            self.tabview.add("3rd")
            self.tabview.add("4th")

            self.score_entry_left1 = customtkinter.CTkEntry(self.tabview.tab("1st"), corner_radius=5,
                                                      width=50, height=50, font=("Helvetica", 30), text_color="cyan")
            self.score_entry_left1.place(relx=0.03, rely=0.1)

            self.divide_scores_label1 = customtkinter.CTkLabel(self.tabview.tab("1st"), text=":", height=50, width=5,
                                                         font=(None, 30))
            self.divide_scores_label1.place(relx=0.47, rely=0.1)

            self.score_entry_right1 = customtkinter.CTkEntry(self.tabview.tab("1st"), corner_radius=5,
                                                       width=50, height=50, font=("Helvetica", 30), text_color="cyan")
            self.score_entry_right1.place(relx=0.6, rely=0.1)

            #Second quater scores
            self.score_entry_left2 = customtkinter.CTkEntry(self.tabview.tab("2nd"), corner_radius=5,
                                                           width=50, height=50, font=("Helvetica", 30),
                                                           text_color="cyan")
            self.score_entry_left2.place(relx=0.03, rely=0.1)

            self.divide_scores_label2 = customtkinter.CTkLabel(self.tabview.tab("2nd"), text=":", height=50, width=5,
                                                              font=(None, 30))
            self.divide_scores_label2.place(relx=0.47, rely=0.1)

            self.score_entry_right2 = customtkinter.CTkEntry(self.tabview.tab("2nd"), corner_radius=5,
                                                            width=50, height=50, font=("Helvetica", 30),
                                                            text_color="cyan")
            self.score_entry_right2.place(relx=0.6, rely=0.1)

            # Third quater scores
            self.score_entry_left3 = customtkinter.CTkEntry(self.tabview.tab("3rd"), corner_radius=5,
                                                            width=50, height=50, font=("Helvetica", 30),
                                                            text_color="cyan")
            self.score_entry_left3.place(relx=0.03, rely=0.1)

            self.divide_scores_label3 = customtkinter.CTkLabel(self.tabview.tab("3rd"), text=":", height=50, width=5,
                                                               font=(None, 30))
            self.divide_scores_label3.place(relx=0.47, rely=0.1)

            self.score_entry_right3 = customtkinter.CTkEntry(self.tabview.tab("3rd"), corner_radius=5,
                                                             width=50, height=50, font=("Helvetica", 30),
                                                             text_color="cyan")
            self.score_entry_right3.place(relx=0.6, rely=0.1)

            # Second quater scores
            self.score_entry_left4 = customtkinter.CTkEntry(self.tabview.tab("4th"), corner_radius=5,
                                                            width=50, height=50, font=("Helvetica", 30),
                                                            text_color="cyan")
            self.score_entry_left4.place(relx=0.03, rely=0.1)

            self.divide_scores_label4 = customtkinter.CTkLabel(self.tabview.tab("4th"), text=":", height=50, width=5,
                                                               font=(None, 30))
            self.divide_scores_label4.place(relx=0.47, rely=0.1)

            self.score_entry_right4 = customtkinter.CTkEntry(self.tabview.tab("4th"), corner_radius=5,
                                                             width=50, height=50, font=("Helvetica", 30),
                                                             text_color="cyan")
            self.score_entry_right4.place(relx=0.6, rely=0.1)
###########################################################################################################
############################################################################################################
    def start_timer_thread(self):
        t =  threading.Thread(target=self.start_pause())
        t.start()

    def playsound(self):
        buzzer_sound.play()

    def update_shot_clock(self):
        global minutes, seconds, milli_seconds, lhs_points, rhs_points,quarter1_left,quarter1_right
        #self.milli_seconds_label.configure(text=f".{milli_seconds:1d}")
        self.shot_24_label.configure(text=f"{seconds_24:02d}")
        self.clock_label.configure(text=f"{minutes:02d}:{seconds:02d}")
        self.home_label_scores.configure(text=f"{lhs_points:02d}")
        self.away_label_scores.configure(text=f"{rhs_points:02d}")
        self.lside_shot_24_label.configure(text=f"{seconds_24:02d}")
        #self.lside_shot_24ml_label.configure(text=f".{milli_seconds:1d}")
        self.rside_shot_24_label.configure(text=f"{seconds_24:02d}")
        #self.qrt1_label_scores.configure(text=f"{ int(self.score_entry_left.get())}:{ int(self.score_entry_right.get())}")



        #if seconds > 59:
        #    seconds = 0

        if minutes >= 2:
            self.clock_label.configure(text_color="#37FD12")

        elif minutes >=1:
            self.clock_label.configure(text_color="orange")

        elif  minutes < 1:
            self.clock_label.configure(text_color="red")

        if seconds_24 >= 24:
            self.shot_24_label.configure(text_color="#37FD12", text="24")
            self.lside_shot_24_label.configure(text_color="#37FD12")
            self.rside_shot_24_label.configure(text_color="#37FD12")


        elif seconds_24 >= 10:
            self.shot_24_label.configure(text_color="#37FD12")
            self.lside_shot_24_label.configure(text_color="#37FD12")
            self.rside_shot_24_label.configure(text_color="#37FD12")


        elif seconds_24 >= 5:
            self.shot_24_label.configure(text_color="orange")
            self.lside_shot_24_label.configure(text_color="orange")
            self.rside_shot_24_label.configure(text_color="orange")

        elif seconds_24  < 5:
            self.shot_24_label.configure(text_color="red")
            self.lside_shot_24_label.configure(text_color="red")
            self.rside_shot_24_label.configure(text_color="red")




        if lhs_points > rhs_points:
            self.home_label_scores.configure(text_color="#37FD12")
            self.away_label_scores.configure(text_color="red")
            self.home_label.configure(text_color="#37FD12")
            self.away_label.configure(text_color="red")
        elif rhs_points > lhs_points:
            self.away_label_scores.configure(text_color="#37FD12")
            self.home_label_scores.configure(text_color="red")
            self.away_label.configure(text_color="#37FD12")
            self.home_label.configure(text_color="red")

        elif lhs_points == rhs_points:
            self.home_label_scores.configure(text_color="orange")
            self.away_label_scores.configure(text_color="orange")
            self.home_label.configure(text_color="orange")
            self.away_label.configure(text_color="orange")



    """# Create a label for the seconds
    seconds_label = tk.Label(frame, font=("Ubuntu", 50, 'bold'), text="24", fg="red")
    seconds_label.grid(row=0, column=0)

    # Create a label for the milliseconds
    milliseconds_label = tk.Label(frame, font=("Ubuntu", 30, 'bold'), text=".00", fg="red")
    milliseconds_label.grid(row=0, column=1)

    # Create a variable for the seconds
    seconds = 24

    # Create a variable for the milliseconds
    milliseconds = 0

    # Define a function to update the timer
    def update_timer():
        # Declare the global variables
        global seconds, milliseconds

        # Decrement the milliseconds by 10
        milliseconds -= 10

        # Check if the milliseconds reach zero
        if milliseconds < 0:
            # Reset the milliseconds to 99
            milliseconds = 99

            # Decrement the seconds by one
            seconds -= 1

        # Check if the seconds reach zero
        if seconds < 0:
            # Stop the timer and display a message
            seconds_label.config(text="Time's up!")
            return

        # Update the labels with the new values
        seconds_label.config(text=str(seconds))
        milliseconds_label.config(text="." + str(milliseconds).zfill(2))

        
        root.after(10, update_timer)

    # Start the timer
    update_timer()"""



    def decrement_time(self):
        global minutes, seconds,seconds_24, running,milli_seconds
        if seconds > 0  and not running:
            seconds -= 1
        elif minutes > 0 and not running:
            minutes -= 1
            seconds = 59

            # Decrement the milliseconds by 10

        if seconds_24 > 0 and not running:

            seconds_24 -= 1
            if seconds_24 <=0:
                buzzer_sound.play()
                self.start_pause()

            self.update_shot_clock()
            self.window.after(1000, self.decrement_time)
            #self.window.after(1, self.milisec_decrement)





    def start_pause(self):
        global running
        running = not running # toggle pause state
        if running:
            self.start_button.configure(text="continue") # change button text
        else:
            self.start_button.configure(text="pause")
            self.decrement_time()


    def add_minute(self):
        global minutes
        minutes += 1
        self.update_shot_clock()

    def minus_minute(self):
        global minutes
        minutes -= 1
        self.update_shot_clock()

    def add_seconds(self):
        global seconds, seconds_24,milli_seconds,minutes
        seconds += 1
        if seconds >= 59:
            seconds = 0
            minutes += 1
        self.update_shot_clock()


    def minus_seconds(self):
        global seconds, seconds_24
        seconds -= 1
        if seconds <= 0:
            seconds = 59
        self.update_shot_clock()

    def plus_secs_24(self):
        global seconds_24
        seconds_24 += 1
        if seconds_24 >= 24:
            seconds_24 = 24
        self.update_shot_clock()

    def minus_secs_24(self):
        global seconds_24
        seconds_24 -= 1
        if seconds_24 <= 0:
            seconds_24 = 24
        self.update_shot_clock()

    def plus3_LHS(self):
        global lhs_points
        lhs_points += 3
        soh_sound.play()

        self.update_shot_clock()

    def plus2_LHS(self):
        global lhs_points
        lhs_points += 2
        mi_sound.play()
        self.update_shot_clock()

    def plus1_LHS(self):
        global lhs_points
        lhs_points += 1
        doh_sound.play()
        self.update_shot_clock()

    def plus3_RHS(self):
        global rhs_points
        rhs_points += 3
        soh_sound.play()
        self.update_shot_clock()


    def plus2_RHS(self):
        global rhs_points
        rhs_points += 2
        mi_sound.play()
        self.update_shot_clock()

    def plus1_RHS(self):
        global rhs_points
        rhs_points += 1
        doh_sound.play()
        self.update_shot_clock()


    def reset_timer(self):
        global minutes, seconds,seconds_24
        minutes = 0
        seconds = 0
        seconds_24 = 24
        self.update_shot_clock()

    def button_14(self):
        global seconds_24
        seconds_24 = 14
        self.update_shot_clock()

    def button_24(self):
        global seconds_24
        seconds_24 = 24
        self.update_shot_clock()

    def place_scores(self):
        # get the name of the current tab
        current_tab = self.tabview.get()
        if current_tab == "1st":
            quarter1_left = int(self.score_entry_left1.get())
            quarter1_right = int(self.score_entry_right1.get())
            if quarter1_left > quarter1_right:
                self.lqrt1_label_scores.configure(text=f"{quarter1_left}",text_color="#37FD12")
                self.div_label_scores.configure(text=":")
                self.rqrt1_label_scores.configure(text=f"{quarter1_right}",text_color='red')
                self.tabview.place_forget()
            elif quarter1_left < quarter1_right:
                self.lqrt1_label_scores.configure(text=f"{quarter1_left}", text_color='red')
                self.div_label_scores.configure(text=":")
                self.rqrt1_label_scores.configure(text=f"{quarter1_right}", text_color="#37FD12")
                self.tabview.place_forget()
            else:
                self.lqrt1_label_scores.configure(text=f"{quarter1_left}", text_color='orange')
                self.div_label_scores.configure(text=":")
                self.rqrt1_label_scores.configure(text=f"{quarter1_right}", text_color='orange')
                self.tabview.place_forget()
        #2nd quarter label
        if current_tab == "2nd":
            quarter2_left = int(self.score_entry_left2.get())
            quarter2_right = int(self.score_entry_right2.get())
            if quarter2_left > quarter2_right:
                self.lqrt2_label_scores.configure(text=f"{quarter2_left}", text_color="#37FD12")
                self.div2_label_scores.configure(text=":")
                self.rqrt2_label_scores.configure(text=f"{quarter2_right}", text_color='red')
                self.tabview.place_forget()
            elif quarter2_left < quarter2_right:
                self.lqrt2_label_scores.configure(text=f"{quarter2_left}", text_color='red')
                self.div2_label_scores.configure(text=":")
                self.rqrt2_label_scores.configure(text=f"{quarter2_right}", text_color="#37FD12")
                self.tabview.place_forget()
            else:
                self.lqrt2_label_scores.configure(text=f"{quarter2_left}", text_color='orange')
                self.div2_label_scores.configure(text=":")
                self.rqrt2_label_scores.configure(text=f"{quarter2_right}", text_color='orange')
                self.tabview.place_forget()


        #3rd quarter label
        if current_tab == "3rd":
            quarter3_left = int(self.score_entry_left3.get())
            quarter3_right = int(self.score_entry_right3.get())
            if quarter3_left > quarter3_right:
                self.lqrt3_label_scores.configure(text=f"{quarter3_left}", text_color="#37FD12")
                self.div3_label_scores.configure(text=":")
                self.rqrt3_label_scores.configure(text=f"{quarter3_right}", text_color='red')
                self.tabview.place_forget()
            elif quarter3_left < quarter3_right:
                self.lqrt3_label_scores.configure(text=f"{quarter3_left}", text_color='red')
                self.div3_label_scores.configure(text=":")
                self.rqrt3_label_scores.configure(text=f"{quarter3_right}", text_color="#37FD12")
                self.tabview.place_forget()
            else:
                self.lqrt3_label_scores.configure(text=f"{quarter3_left}", text_color='orange')
                self.div3_label_scores.configure(text=":")
                self.rqrt3_label_scores.configure(text=f"{quarter3_right}", text_color='orange')
                self.tabview.place_forget()
        #4th quarter label
        if current_tab == "4th":
            quarter4_left = int(self.score_entry_left4.get())
            quarter4_right = int(self.score_entry_right4.get())
            if quarter4_left > quarter4_right:
                self.lqrt4_label_scores.configure(text=f"{quarter4_left}", text_color="#37FD12")
                self.div4_label_scores.configure(text=":")
                self.rqrt4_label_scores.configure(text=f"{quarter4_right}", text_color='red')
                self.tabview.place_forget()
            elif quarter4_left < quarter4_right:
                self.lqrt4_label_scores.configure(text=f"{quarter4_left}", text_color='red')
                self.div4_label_scores.configure(text=":")
                self.rqrt4_label_scores.configure(text=f"{quarter4_right}", text_color="#37FD12")
                self.tabview.place_forget()
            else:
                self.lqrt4_label_scores.configure(text=f"{quarter4_left}", text_color='orange')
                self.div4_label_scores.configure(text=":")
                self.rqrt4_label_scores.configure(text=f"{quarter4_right}", text_color='orange')
                self.tabview.place_forget()




    def place_teamnames(self):
        # get the name of the current tab
        #current_name_tab = self.tabview_team.get()
        left_teamname = str(self.team_entry_left1.get())
        right_teamname = str(self.team_entry_right1.get())

        self.home_label.configure(text=f"{left_teamname}")
        self.div_label_scores.configure(text="vs")
        self.away_label.configure(text=f"{right_teamname}")
        self.bar_button1.configure(text=f"{left_teamname}")
        self.bar_button2.configure(text=f"{right_teamname}")
        self.tabview_team.place_forget()
        if len(left_teamname) or len(right_teamname) >= 6:
            self.home_label.place(relx=0.08)
            self.away_label.place(relx=0.63)

        """elif quarter1_left < quarter1_right:
            self.lqrt1_label_scores.configure(text=f"{quarter1_left}", text_color='red')
            self.div_label_scores.configure(text=":")
            self.rqrt1_label_scores.configure(text=f"{quarter1_right}", text_color='green')
            self.tabview.place_forget()
        else:
            self.lqrt1_label_scores.configure(text=f"{quarter1_left}", text_color='orange')
            self.div_label_scores.configure(text=":")
            self.rqrt1_label_scores.configure(text=f"{quarter1_right}", text_color='orange')
            self.tabview.place_forget()"""


Shot_Clock_Timer()
