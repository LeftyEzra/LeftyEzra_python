import tkinter as tk
import customtkinter
from tkinter import messagebox
from tkinter import Canvas
from PIL import Image, ImageTk, ImageDraw,ImageGrab
from tkinter import simpledialog
from tkinter import ttk
import openpyxl
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry("1100x580")
window.title('LEFTY click and display'.title())
window.resizable(False,False)
############################################################################################



class SlidePanel(customtkinter.CTkFrame):
    def __init__ (self,parent,start_position,end_position,):
        super().__init__(master=parent,fg_color="black",width=280)

        #general attributes
        self.start_position = start_position + 0.01
        self.end_position   = end_position   - 0.01
        #self.width          = abs(start_position - end_position)

        #animation logic
        self.pos = self.start_position
        self.in_start_position = True

        #layout
        self.place(relx=self.start_position,rely=0.09,relheight=0.85)


    def animate(self):
        if self.in_start_position:
            self.animate_forward()
        else:
            self.animate_backwards()
    def animate_forward(self):
        if self.pos > self.end_position:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.09)
            self.after(10,self.animate_forward)
        else:
            self.in_start_position = False

    def animate_backwards(self):
        if self.pos < self.start_position:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.09)
            self.after(10,self.animate_backwards)
        else:
            self.in_start_position = True

#                                  1.0,0.6
animated_panel = SlidePanel(window,0,-0.35)


button=customtkinter.CTkButton(window,text='Click me',command=animated_panel.animate,fg_color="#37FD12",text_color="black")
button.place(relx = 0.01,rely= 0.01,anchor='nw')
##############################################################################################
label_bg1 = customtkinter.CTkImage(light_image=Image.open("cup.png"),size=(750,470))
label_bg2 = customtkinter.CTkImage(light_image=Image.open("Figure_wc1.png"),size=(750,470))
label_bg3 = customtkinter.CTkImage(light_image=Image.open("fwcup.png"),size=(750,470))
global my_imagees
count = -1
my_images= [label_bg1,label_bg2,label_bg3]

home_label = customtkinter.CTkLabel(window,text="",width=750,height=470)
home_label.place(relx=0.5,rely=0)
def next_image():
    global count
    if count == 2:
        home_label1 = customtkinter.CTkLabel(home_label, text="", image=my_images[0])
        home_label1.place(relx=0.0, rely=0)
        count = 0

    else:
        home_label1 = customtkinter.CTkLabel(home_label, text="", image=my_images[count+1])
        home_label1.place(relx=0.0, rely=0)
        count +=1

    window.after(2000,next_image)

next_image()
######################################################################################
############################################################################################
def home():
    home_label.place(relx=0.29, rely=0)
    basketball_canvas.place_forget()
    football_canvas.place_forget()
    volley_canvas.place_forget()
    lawntennis_canvas.place_forget()


def display_basketball():
    basketball_canvas.place(relx=0.29,rely=0)
    football_canvas.place_forget()
    volley_canvas.place_forget()
    lawntennis_canvas.place_forget()
    home_label.place_forget()

def display_football():
    football_canvas.place(relx=0.29, rely=0)
    volley_canvas.place_forget()
    lawntennis_canvas.place_forget()
    basketball_canvas.place_forget()
    home_label.place_forget()
def display_volley() :
    volley_canvas.place(relx=0.29,rely=0)
    basketball_canvas.place_forget()
    football_canvas.place_forget()
    lawntennis_canvas.place_forget()
    home_label.place_forget()
def display_tennis():
    lawntennis_canvas.place(relx=0.29, rely=0)
    volley_canvas.place_forget()
    basketball_canvas.place_forget()
    football_canvas.place_forget()
    home_label.place_forget()

###############################################################################################
##############################################################################################
#Create basketball canvas
basketball_canvas = Canvas(window,width=1149,height=700,bg="orange",highlightthickness=0)

basketball_canvas.place(relx=0.22,rely=0)

### basketball image background
basketball_image = Image.open("bball3.PNG")
basketball_resized_photo = basketball_image.resize((1151,702))
basketball_bg_img = ImageTk.PhotoImage(basketball_resized_photo)
background_image = basketball_canvas.create_image(0,0,image=basketball_bg_img,anchor="nw")
basketball_canvas.create_text(590,26,font=("Arial",20),text="1st & 2nd     =======     3rd & 4th      ",fill="green")
# Letters to print on the background
font = ("Arial", 23,'bold')
positions = []
letters = []

#Defining a function that will print letters on the screen when you click anywhere on the canvas
def handle_click(event):
    x = event.x
    y = event.y
    print(f'Clicked @ position ({x}, {y})')

    #using the simpledialog to ask which letter to print
    letter = tk.simpledialog.askstring("Select letter", "(x or o )")
    if letter and letter in('x', 'o', ):
         positions.append((x,y))
         letters.append(letter)

         #loop through every time you press the button
         for pos, letter in zip(positions,letters):
            if letter == 'x':
                basketball_canvas.create_text(pos, text=letter, font=font, fill="#d1001f")

            elif letter == 'o':
                basketball_canvas.create_text(pos, text=letter, font=font, fill="#37FD12")

        #last_item_id = basketball_canvas.find_all()[-1]

        # delete the last text item from the canvas
        #basketball_canvas.delete(last_item_id)

    else:
        messagebox.showerror("Invalid input", "Pls, enter a valid letter (x or o)".title())
    basketball_canvas.update()
    basketball_canvas.postscript(file="fifaabc.ps",colormode='color')
#bind the buttonpress events
basketball_canvas.bind('<Button-1>',handle_click)

def convert_to_png():
    psimage= Image.open("fifaabc.ps")
    psimage.save("border.png",save_all=True)
#A button to save or convert the ps file to png file
basketball_button = customtkinter.CTkButton(window, height=30,width=150,corner_radius=10,
                                     text="Save bball",command=convert_to_png, text_color="yellow",fg_color="#51074a",)
basketball_button.place(relx=0.29,rely=0.82,)

#########################################################################################################
########################################################################################################

#####################################################################################################
################################################################################################
#Create football canvas
football_canvas = Canvas(window,width=1150,height=700,bg="green",highlightthickness=0)
football_canvas.place(relx=0.22,rely=0)

#Creating a background photo
football_canvas_image = Image.open("foot.JPG")
football_canvas_image_resized = football_canvas_image.resize((1152,702))
football_canvas_pitch = ImageTk.PhotoImage(football_canvas_image_resized)
football_image = football_canvas.create_image(0,0,image=football_canvas_pitch,anchor="nw")
football_canvas.create_text(590,35,font=("Arial",20),text="Sweden >>>          2nd half            <<< Japan",fill="yellow")

# Letters to print on the background
font1 = ("Arial", 30,'bold')
positions1 = []
letters1 = []

#Defining a function that will print letters on the screen when you click anywhere on the canvas
def get_click(event):
    x1 = event.x
    y1 = event.y
    print(f'Clicked @ position ({x1}, {y1})')

    #using the simpledialog to ask which letter to print
    letter = tk.simpledialog.askstring("Select letter", "(x or o)")
    if letter and letter in('x', 'o'):
         positions1.append((x1,y1))
         letters1.append(letter)

         #loop through every time you press the button
         for pos1, letter1 in zip(positions1,letters1):
            if letter1 == 'x':
                football_canvas.create_text(pos1, text=letter1, font=font1, fill="#d1001f")
            elif letter1 == 'o':
                football_canvas.create_text(pos1, text=letter1, font=font1, fill="yellow")

    else:
        messagebox.showerror("Invalid input", "Pls, enter a valid letter (x or o)".title())
    football_canvas.update()
    football_canvas.postscript(file="football.ps",colormode='color')
#bind the buttonpress events
football_canvas.bind('<Button-1>',get_click)

def convert_to_png1():
    psimage1= Image.open("football.ps")
    psimage1.save("footballplot.png",save_all=True)
#A button to save or convert the ps file to png file
football_button = customtkinter.CTkButton(window, height=30,width=150,corner_radius=10,
                                     text="Save fball",command=convert_to_png1,fg_color="#000080",text_color="#00FF2F")
football_button.place(relx=0.29,rely=0.88)
###########################################################################################
###########################################################################################
#Volleyball court creation
volley_canvas = Canvas(window,width=1150,height=700,bg="red")
volley_canvas.place(relx=0.22,rely=0)

#Image background for volleyball
volleyball_canvas_image = Image.open("volley2.png")
volleyball_canvas_image_resize = volleyball_canvas_image.resize((1152,702))
volleyball_canvas_court = ImageTk.PhotoImage(volleyball_canvas_image_resize)
volleyball_bg_pic = volley_canvas.create_image(0,0,image=volleyball_canvas_court,anchor="nw")

# Letters to print on the background
font2 = ("Arial", 30,'bold')
positions2 = []
letters2 = []

#Defining a function that will print letters on the screen when you click anywhere on the canvas
def get_position_click(event):
    x2 = event.x
    y2 = event.y
    print(f'Clicked @ position ({x2}, {y2})')

    #using the simpledialog to ask which letter to print
    letter = tk.simpledialog.askstring("Select letter", "(x or o)",)
    if letter and letter in('x', 'o'):
         positions2.append((x2,y2))
         letters2.append(letter)

         #loop through every time you press the button
         for pos2, letter2 in zip(positions2,letters2):
            if letter2 == 'x':
                volley_canvas.create_text(pos2, text=letter2, font=font2, fill="#d1001f")
            elif letter2 == 'o':
                volley_canvas.create_text(pos2, text=letter2, font=font2, fill="green")

    else:
        messagebox.showerror("Invalid input", "Pls, enter a valid letter (x or o)".title())
    volley_canvas.update()
    volley_canvas.postscript(file="volleyball.ps",colormode='color')
#bind the buttonpress events
volley_canvas.bind('<Button-1>',get_position_click)

###Ask to save ps file to png###
def convert_to_png2():
    psimage2= Image.open("volleyball.ps")
    psimage2.save("volleyball.png",save_all=True)
#A button to save or convert the ps file to png file
volleyball_button = customtkinter.CTkButton(window, height=30,width=150,corner_radius=10,
                                     text="Save volley",command=convert_to_png2,fg_color="#800000",text_color="#00FF2F")
volleyball_button.place(relx=0.43,rely=0.82)

###############################################################################################
###############################################################################################
#Lawntennis canvas creation
lawntennis_canvas = Canvas(window,width=1150,height=700,bg="black")
lawntennis_canvas.place(relx=0.22,rely=0)

#creating image object on the canvas
tennis_image = Image.open("tennis1.png")
tennis_canvas_image_resize = tennis_image.resize((1152,702))
tennisball_court = ImageTk.PhotoImage(tennis_canvas_image_resize)
tennis_bg_pic = lawntennis_canvas.create_image(0,0,image=tennisball_court,anchor='nw')


# Letters to print on the background
font3 = ("Arial", 30,'bold')
positions3 = []
letters3 = []

#Defining a function that will print letters on the screen when you click anywhere on the canvas
def print_position_click(event):
    x3 = event.x
    y3 = event.y
    print(f'Clicked @ position ({x3}, {y3})')

    #using the simpledialog to ask which letter to print
    letter = tk.simpledialog.askstring("Select letter", "(x or o)",)
    if letter and letter in('x', 'o'):
         positions3.append((x3,y3))
         letters3.append(letter)

         #loop through every time you press the button
         for pos3, letter3 in zip(positions3,letters3):
            if letter3 == 'x':
                lawntennis_canvas.create_text(pos3, text=letter3, font=font3, fill="#d1001f")
            elif letter3 == 'o':
                lawntennis_canvas.create_text(pos3, text=letter3, font=font3, fill="green")

    else:
        messagebox.showerror("Invalid input", "Pls, enter a valid letter (x or o)".title())
    lawntennis_canvas.update()
    lawntennis_canvas.postscript(file="lawntennis.ps",colormode='color')
#bind the buttonpress events
lawntennis_canvas.bind('<Button-1>',print_position_click)

###Ask to save ps file to png###
def convert_to_png3():
    psimage3= Image.open("lawntennis.ps")
    psimage3.save("lawntennis.png",save_all=True)
#A button to save or convert the ps file to png file
lawntennis_button = customtkinter.CTkButton(window, height=30,width=150,corner_radius=10,
                                     text="Save tennis",text_color="#00FF2F",fg_color="#480062",command=convert_to_png3)
lawntennis_button.place(relx=0.43,rely=0.88,)

##############################################################################################
##############################################################################################
### Button to call the home label as background to display###
bt_img1 =customtkinter.CTkImage(light_image=Image.open("Home_pic.png"),size=(40,40),)

home_button= customtkinter.CTkButton(animated_panel, height=40,width=250,image=bt_img1,compound='left',
                                     corner_radius=20,text_color='#FF5412',hover_color="green",
                                     text="Home",command=home,fg_color="#008D7C",font=('Arial', 16, 'bold'))
home_button.place(relx=0.01,rely=0.01,)

###Button to call basketball canvas###
bt_img2 =customtkinter.CTkImage(light_image=Image.open("ball1.PNG"),size=(40,40),)

basketball_button = customtkinter.CTkButton(animated_panel, height=40,width=250,
                                            fg_color="#8f0b47",hover_color="#952B60",
                                            corner_radius=20,text_color='orange',
                                            font=('Arial', 16, 'bold'),
                                            text="Basketball",
                                            command=display_basketball,image=bt_img2)#F62AA0
basketball_button.place(relx=0.01,rely=0.11,)

#football creation
bt_img3 =customtkinter.CTkImage(light_image=Image.open("ball7.PNG"),size=(40,40),)
football_button = customtkinter.CTkButton(animated_panel, height=40,width=250,
                                            image=bt_img3,corner_radius=20,
                                            font=('Arial', 16, 'bold'),
                                            text_color="yellow",
                                            fg_color="#51074a",hover_color="#952B60",
                                            text="Football",command=display_football)
football_button.place(relx=0.01,rely=0.21,)

### Button to call the volleyball canvas###

bt_img4 =customtkinter.CTkImage(light_image=Image.open("ball8.PNG"),size=(40,40),)
volleyball_button = customtkinter.CTkButton(animated_panel, height=40,width=250,
                                            image=bt_img4,fg_color="#F62AA0",
                                            font=('Arial', 16, 'bold'),text_color="yellow",
                                            corner_radius=20,
                                            text="Volleyball",command=display_volley)
volleyball_button.place(relx=0.01,rely=0.31,)

### Button to call the tennis canvas to display###
bt_img5 =customtkinter.CTkImage(light_image=Image.open("ball9.PNG"),size=(40,40),)
lawntennis_button= customtkinter.CTkButton(animated_panel, height=40,width=250,
                                            image=bt_img5,fg_color="green",
                                            font=('Arial', 16, 'bold'),
                                            corner_radius=20,text_color="#A8E10C",
                                            text="Tennis",command=display_tennis)
lawntennis_button.place(relx=0.01,rely=0.41,)
################################################################################################
##############################################################################################


######################################################################################################

########################################################################################################

###############################################################################################
#############################################################################################
### Create buttons to create entry and treeview and graphs ###
## Entries  and treeview call button


graph_button= customtkinter.CTkButton(animated_panel, height=60,width=250,
                                            fg_color="green",
                                            font=('Arial', 28, 'bold'),
                                            corner_radius=5,text_color="#A8E10C",
                                            text="Show Stats",)
graph_button.place(relx=0.01,rely=0.7,)

#####################################################################################################
######################################################################################################
home_label.place(relx=0.29,rely=0)
basketball_canvas.place_forget()
football_canvas.place_forget()
volley_canvas.place_forget()
lawntennis_canvas.place_forget()


#canvas_visibility = False


#window.geometry("1000x500")
#window.title('Stop Clock')
#window.config(bg="#0A0B0C")

#font1 = ("Arial", 20,'bold')
#font2 = ("Arial", 18,'bold')
#font3 = ("Arial", 33,'bold')


#Creating a animated class frame to contain all the entry widgets
class SlidePanel(customtkinter.CTkFrame):
    def __init__ (self,parent,start_position,end_position,):
        super().__init__(master=parent,fg_color="#FB7C00",width=880,height=460)

        #general attributes
        self.start_position = start_position + 0.01
        self.end_position   = end_position   - 0.01
        #self.width          = abs(start_position - end_position)

        #animation logic
        self.pos = self.start_position
        self.in_start_position = True

        #layout
        self.place(relx=0.2,rely=self.start_position)


    def animate(self):
        if self.in_start_position:
            self.animate_upward()
        else:
            self.animate_downwards()
    def animate_upward(self):
        if self.pos > self.end_position:
            self.pos -= 0.008
            self.place(rely=self.pos, relx=0.2)
            self.after(0,self.animate_upward)

        else:
            self.in_start_position = False

    def animate_downwards(self):
        if self.pos < self.start_position:
            self.pos += 0.008
            self.place(rely=self.pos, relx=0.2)
            self.after(0,self.animate_downwards)
        else:
            self.in_start_position = True

#                                  1.0,0.6
animated_panel1 = SlidePanel(window,1.0,0.02)

#font1 = ("Arial", 30,'bold')
#button to call the treeview from its resting state

entry_treeview_button= customtkinter.CTkButton(animated_panel, height=60,width=250,
                                            fg_color="green",command=animated_panel1.animate,
                                            font=('Arial', 28, 'bold'),
                                            corner_radius=5,text_color="#A8E10C",
                                            text="Enter Stats",)
entry_treeview_button.place(relx=0.01,rely=0.55,)


#Teams Entry and label widgets
team1_label_stat = customtkinter.CTkLabel(animated_panel1,height=30,
                                          text="                          Team 1 Stats",font=font1)
team1_label_stat.place(relx=0.01,rely=0.01)

team_name_label = customtkinter.CTkLabel(animated_panel1,text="Team name").place(relx=0.01,rely=0.07)

team_name_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_name_entry.delete(0, "end")
team_name_entry.insert(0, "Team name")

team_name_entry.bind("<FocusIn>", lambda d: team_name_entry.delete('0', "end"))
team_name_entry.place(relx=0.01,rely=0.12)


team_3ptAttempts_label = customtkinter.CTkLabel(animated_panel1,text="3points Attempts").place(relx=0.01,rely=0.2)

team_3ptsAttempts_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_3ptsAttempts_entry.delete(0, "end")
team_3ptsAttempts_entry.insert(0, "0")

team_3ptsAttempts_entry.bind("<FocusIn>", lambda e: team_3ptsAttempts_entry.delete('0', "end"))
team_3ptsAttempts_entry.place(relx=0.01,rely=0.25)

team_3ptMade_label = customtkinter.CTkLabel(animated_panel1,text="3points Made").place(relx=0.01,rely=0.33)

team_3ptsMade_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_3ptsMade_entry.delete(0, "end")
team_3ptsMade_entry.insert(0, "0")

team_3ptsMade_entry.bind("<FocusIn>", lambda f: team_3ptsAttempts_entry.delete('0', "end"))
team_3ptsMade_entry.place(relx=0.01,rely=0.38)

team_2ptsAttempts_label = customtkinter.CTkLabel(animated_panel1,text="2points Attempts").place(relx=0.2,rely=0.07)

team_2ptsAttempts_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)

team_2ptsAttempts_entry.delete(0, "end")
team_2ptsAttempts_entry.insert(0, "0")

team_2ptsAttempts_entry.bind("<FocusIn>", lambda g: team_2ptsAttempts_entry.delete('0', "end"))
team_2ptsAttempts_entry.place(relx=0.2,rely=0.12)

team_2ptMade_label = customtkinter.CTkLabel(animated_panel1,text="2points Made").place(relx=0.2,rely=0.2)

team_2ptsMade_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_2ptsMade_entry.delete(0, "end")
team_2ptsMade_entry.insert(0, "0")

team_2ptsMade_entry.bind("<FocusIn>", lambda h: team_2ptsMade_entry.delete('0', "end"))
team_2ptsMade_entry.place(relx=0.2,rely=0.25)


team_ftAttempts_label = customtkinter.CTkLabel(animated_panel1,text="Freethrows Attempts").place(relx=0.51,rely=0.07)

team_ftAttempts_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_ftAttempts_entry.delete(0, "end")
team_ftAttempts_entry.insert(0, "0")

team_ftAttempts_entry.bind("<FocusIn>", lambda i: team_ftAttempts_entry.delete('0', "end"))
team_ftAttempts_entry.place(relx=0.51,rely=0.12)

team_ftMade_label = customtkinter.CTkLabel(animated_panel1,text="Freethrow Made").place(relx=0.51,rely=0.2)

team_ftMade_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)

team_ftMade_entry.delete(0, "end")
team_ftMade_entry.insert(0, "0")

team_ftMade_entry.bind("<FocusIn>", lambda j: team_ftMade_entry.delete('0', "end"))
team_ftMade_entry.place(relx=0.51,rely=0.25)

team_offensive_rebound_label = customtkinter.CTkLabel(animated_panel1,text="Offensive Rebounds").place(relx=0.7,rely=0.07)

team_off_rebounds_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_off_rebounds_entry.delete(0, "end")
team_off_rebounds_entry.insert(0, "0")

team_off_rebounds_entry.bind("<FocusIn>", lambda k: team_off_rebounds_entry.delete('0', "end"))
team_off_rebounds_entry.place(relx=0.7,rely=0.12)

team_defensive_rebounds_label = customtkinter.CTkLabel(animated_panel1,text="Defensive Rebounds").place(relx=0.7,rely=0.2)

team_def_rebounds_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_def_rebounds_entry.delete(0, "end")
team_def_rebounds_entry.insert(0, "0")

team_def_rebounds_entry.bind("<FocusIn>", lambda l: team_def_rebounds_entry.delete('0', "end"))
team_def_rebounds_entry.place(relx=0.7,rely=0.25)

team_block_label = customtkinter.CTkLabel(animated_panel1,text="Blocks").place(relx=0.51,rely=0.33)

team_block_entry = customtkinter.CTkEntry(animated_panel1,width=140,height=30,corner_radius=5)
team_block_entry.delete(0, "end")
team_block_entry.insert(0, "0")

team_block_entry.bind("<FocusIn>", lambda f: team_block_entry.delete('0', "end"))
team_block_entry.place(relx=0.51,rely=0.38)



#Line to divide the animated panel into 2
baseline_div = customtkinter.CTkBaseClass(animated_panel1,height=300,bg_color="black",width=5)
baseline_div.place(relx=0.5)


######################################################################################################
### Team1 entry and lab
###Select items to update
def display_record():
    #Delete all the entry records
    team_name_entry.delete(0, "end")
    team_3ptsAttempts_entry.delete(0, "end")
    team_3ptsMade_entry.delete(0, "end")
    team_2ptsAttempts_entry.delete(0, "end")
    team_2ptsMade_entry.delete(0, "end")
    team_ftAttempts_entry.delete(0, "end")
    team_ftMade_entry.delete(0, "end")
    team_off_rebounds_entry.delete(0, "end")
    team_def_rebounds_entry.delete(0, "end")
    team_block_entry.delete(0, "end")



    #variable to select the row in the treeview
    selected_item = tree.focus()

    new_update = tree.item(selected_item,'values')
    team_name_entry.insert(0, new_update[0])
    team_3ptsAttempts_entry.insert(0, new_update[1])
    team_3ptsMade_entry.insert(0, new_update[2])
    team_2ptsAttempts_entry.insert(0, new_update[3])
    team_2ptsMade_entry.insert(0, new_update[4])
    team_ftAttempts_entry.insert(0, new_update[5])
    team_ftMade_entry.insert(0, new_update[6])
    team_off_rebounds_entry.insert(0, new_update[7])
    team_def_rebounds_entry.insert(0, new_update[8])
    team_block_entry.insert(0, new_update[9])
#
#Update the selected items in the treeview
def update_record():

    #The focus point
    selected_item = tree.focus()
    #row_index = int(tree.index(selected_item))
    tree.item(selected_item, text="",values=(team_name_entry.get(),team_3ptsAttempts_entry.get(),team_3ptsMade_entry.get(),
                                             team_2ptsAttempts_entry.get(),team_2ptsMade_entry.get(),team_ftAttempts_entry.get(),
                                             team_ftMade_entry.get(),team_off_rebounds_entry.get(),team_def_rebounds_entry.get(),
                                             team_block_entry.get()))

    #after updating clear the entry boxes
    team_name_entry.delete(0, "end")
    team_3ptsAttempts_entry.delete(0, "end")
    team_3ptsMade_entry.delete(0, "end")
    team_2ptsAttempts_entry.delete(0, "end")
    team_2ptsMade_entry.delete(0, "end")
    team_ftAttempts_entry.delete(0, "end")
    team_ftMade_entry.delete(0, "end")
    team_off_rebounds_entry.delete(0, "end")
    team_def_rebounds_entry.delete(0, "end")
    team_block_entry.delete(0, "end")

    messagebox.showinfo("Success", "Datas updated successfully.")


#Clear selected items from treeview
def clear():
    x = tree.selection()
    for record in x:
        tree.delete(record)



#Add items to treeview
def add_items():

    ###Variable to store the entry datas
    team_name = str(team_name_entry.get())
    pt3_attempts = int(team_3ptsAttempts_entry.get())
    pt3_made = int(team_3ptsMade_entry.get())
    pt2_attempts = int(team_2ptsAttempts_entry.get())
    pt2_made = int(team_2ptsMade_entry.get())
    ft_attempts = int(team_ftAttempts_entry.get())
    ft_made = int(team_ftMade_entry.get())
    off_rebound = int(team_off_rebounds_entry.get())
    def_rebound = int(team_def_rebounds_entry.get())
    blocks = int(team_block_entry.get())

    ### This is to insert all the input datas into the treview rows
    row_values = [team_name,pt3_attempts, pt3_made, pt2_attempts,pt2_made,ft_attempts,ft_made,off_rebound,def_rebound,blocks]
    tree.insert('', "end", values=row_values)

    #for loop function is to get all the widgets that are type entry and delete them
    for widget in animated_panel1.winfo_children():
        if isinstance(widget, customtkinter.CTkEntry):
            widget.delete(0,"end")

    ### Save data to Excel
    games_filepath = "team_datas.xlsx"
    if not os.path.exists(games_filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["Team names","3pts_Attempts", "3pts_Made", "2pts_Attempts","2pts_Made",
                    "FT_Attempts","FT_Made","Off_rebounds","Def_rebounds","Blocks","Team2",]

        sheet.append(heading)
        workbook.save(games_filepath)

    workbook = openpyxl.load_workbook(games_filepath)
    sheet = workbook.active
    sheet.append([team_name,pt3_attempts, pt3_made, pt2_attempts,pt2_made,ft_attempts,ft_made,off_rebound,def_rebound,blocks])
    workbook.save(games_filepath)
    messagebox.showinfo("Success","Datas saved successfully.")


###buton widgets to call the trreview created functions
add_button_item = customtkinter.CTkButton(window,text="Add Stats",fg_color="#37FD12",text_color="black",command=add_items).place(relx=0.6,rely=0.82)
del_button = customtkinter.CTkButton(window,text="Clear Stats",fg_color="#37FD12",text_color="black",command=clear).place(relx=0.6,rely=0.88)
update_button = customtkinter.CTkButton(window,text="Update Stats",fg_color="#37FD12",text_color="black",command=update_record).place(relx=0.73,rely=0.82)
select_button = customtkinter.CTkButton(window,text="Select Stats",fg_color="#37FD12",text_color="black",command=display_record).place(relx=0.73,rely=0.88)


###styling the treeview
style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview.Heading",font=("Arial",12,"bold"),foreground="blue",background="orange")
style.configure('Treeview',font=("Arial",15),foreground="#00FF2F",background="#000080",fieldbackground='#480062')
style.map('Treeview',background=[('selected', '#AA04A7')])


###Column title for the treeview
cols=("Team names","3pts Attempts", "3pts Made", "2pts Attempts","2pts Made","FT Attempts","FT Made","Off_rebounds","Def_rebounds","Blocks")

tree = ttk.Treeview(animated_panel1,height=15,columns=cols)
#tree["columns"] = ("3points Attempts","Made","Missed")

tree.column("#0",width=0,stretch=tk.NO)
tree.column("Team names",width=150,anchor=tk.W,stretch=tk.YES,)
tree.column("3pts Attempts",width=120,anchor=tk.W,stretch=True,)
tree.column("3pts Made",width=150,anchor=tk.W,stretch=tk.YES,)
tree.column("2pts Attempts",width=130,anchor=tk.W,stretch=True,)
tree.column("2pts Made",width=120,anchor=tk.W,stretch=tk.YES,)
tree.column("FT Attempts",width=120,anchor=tk.W,stretch=True,)
tree.column("FT Made",width=100,anchor=tk.W,stretch=tk.YES,)
tree.column("Off_rebounds",width=150,anchor=tk.W,stretch=True,)
tree.column("Def_rebounds",width=150,anchor=tk.W,stretch=tk.YES,)
tree.column("Blocks",width=100,anchor=tk.W,stretch=False,)


tree.heading("#0",text="")
tree.heading("Team names", text="Team names")
tree.heading("3pts Attempts", text="3pts Attempts",anchor=tk.W)
tree.heading("3pts Made", text="3pts Made")
tree.heading("2pts Attempts", text="2pts Attempts")
tree.heading("2pts Made", text="2pts Made")
tree.heading("FT Attempts", text="FT Attempts",anchor=tk.W)
tree.heading("FT Made", text="FT Made")
tree.heading("Off_rebounds", text="Off_rebounds")
tree.heading("Def_rebounds", text="Def_rebounds")
tree.heading("Blocks",text="Blocks")





tree.place(relx=0.001,rely=0.5)
#tree.bind('<ButtonRelease>', display_record)
tree_scrollbar = customtkinter.CTkScrollbar(animated_panel1,orientation="vertical",command=tree.yview,width=20,
                                            height=220,fg_color="transparent",bg_color="blue")
#tree.configure(xscrollcommand=treeview_scrollbar.set)
tree.configure(yscrollcommand=tree_scrollbar.set)
tree_scrollbar.place(relx=1,rely=0.5,anchor="ne")
window.mainloop()