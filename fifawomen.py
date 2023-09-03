import time
import tkinter as tk
import customtkinter
from tkinter import Canvas
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry("1200x590")
window.title('LEFTY fifa women world cup analysis'.title())
window.resizable(False,False)




WIDTH = 1000
HEIGHT = 780
label_photo =  customtkinter.CTkImage(light_image=Image.open("women_fifa.png"),size=(390,522))
label_bg = customtkinter.CTkLabel(window,text_color="#ff0",font=("Gothic", 20, "bold"),text="Follow for more update:\n @babalefty on tiktok\n"
                                     " @babalefty on instagram\n@LeftyEzra1 on twitter\n Solomon Ezra Lefty on facebook\n\n\n"
                                     "for adverts, ^^^^^^^   ",fg_color='green',image=label_photo,height=522,width=390)
label_bg.place(relx=0.672,rely=0.001)
"""cpchoice = [ PhotoImage(file="fifawomenlogo2.png"),PhotoImage(file="anotherlogo.png"),PhotoImage(file="fifawomenlodo1.PNG")]
label_logo = choice(cpchoice)
picture1_photo =  customtkinter.CTkImage(light_image=Image.open("fifawomenlodo1.PNG"),size=(300,450))
label_photo =  customtkinter.CTkImage(light_image=Image.open("women_fifa.png"),size=(390,536))
label_bg = customtkinter.CTkLabel(window,text="lefty",fg_color='green',image=label_photo,height=536,width=390)
label_bg.place(relx=0.672,rely=0.001)

def move_button():
    global button_x
    button_x -= 0.01
    picture1.place(relx=0.1, rely=button_x)
    if button_x >= 0.1:
        window.after(10,move_button)
        picture1.place(relx=0.1, rely=button_x)
    #window.after(3000, slide_thru)


    window.after(3000, slide_thru)
def move_buton():
    global button_y
    button_y -= 0.01
    picture1.place(relx=button_y, rely=0.1)
    if button_y >= -1.0:
        window.after(10,move_buton)
        picture1.place(relx=button_y, rely=0.1)
    #window.after(3000,move_button)


def slide_thru():
    global button_x
    button_x += 0.001
    picture1.place(relx=1.0, rely=0.1)
    window.after(2000, slide_thru)



button_x = 1.0
picture1 = customtkinter.CTkLabel(label_bg,image=picture1_photo)
picture1.place(relx=0.1, rely=button_x, )

button_y = 1.0
label3 = ttkbootstrap.Label(label_bg,image=label_logo)
label3.place(relx=button_y, rely=0.1, width=500, height=650)

photo2 =customtkinter.CTkImage(light_image=Image.open("button.png"),size=(20,20),)
button = customtkinter.CTkButton(window,command=move_buton,compound='left',
                                 fg_color='purple',hover_color="green",
                                 width=50,height=30,text="FifaWC",image=photo2)
button.place(relx=0.15,rely=0.93,)"""





image1 = Image.open("fifa_playoff.png")
photo1 = ImageTk.PhotoImage(image1)
label1 = tk.Label(label_bg,image=photo1)
label1.place(relx=1.0, rely=0.1)


abel_photo =  customtkinter.CTkImage(dark_image=Image.open("r16.JPG"),size=(400,400))
label2 = customtkinter.CTkLabel(label_bg,image=abel_photo,text="")
label2.place(relx=1.0,rely=0.1)

label_photo =  customtkinter.CTkImage(light_image=Image.open("women_fifa.png"),size=(390,536))
label3 = customtkinter.CTkLabel(label_bg,image=label_photo,text="QUALIFIED",
                                font=('Gothic',20,'bold'),text_color="green")
label3.place(relx=1.0,rely=0.1)

#image3 = Image.open("goldenbootrace_1.png")
#photo3 = ImageTk.PhotoImage(image3)
#label3 = tk.Label(label_bg,image=photo3)
#label3.place(relx=1.0, rely=0.1, )

"""image4 = Image.open("")
photo4 = ImageTk.PhotoImage(image4)
label4 = tk.Label(label_bg,image=photo4)
label4.place(relx=1.0, rely=0.1, )

image5 = Image.open("goalsconceded.png")
photo5 = ImageTk.PhotoImage(image5)
label5 = tk.Label(label_bg,image=photo5)
label5.place(relx=1.0, rely=0.1)

photo6 = customtkinter.CTkImage(light_image=Image.open("Figure_wc1.png"), size=(350, 400))
label6 = customtkinter.CTkLabel(label_bg,text="",image=photo6,text_color="pink",font=('Gothic',18,"italic"))
label6.place(relx=1.0,rely=0.1)"""
label_bg1  = customtkinter.CTkImage(light_image=Image.open("semis.jpg"),size=(390,536))
label_bg2  = customtkinter.CTkImage(light_image=Image.open("SORRYOO.jpg"),size=(390,536))
label_bg3  = customtkinter.CTkImage(light_image=Image.open("ausqualified.jpg"),size=(390,536))
label_bg4  = customtkinter.CTkImage(light_image=Image.open("sorryj2.jpg"),size=(390,536))
label_bg5  = customtkinter.CTkImage(light_image=Image.open("sorryjap.jpg"),size=(390,536))
label_bg6  = customtkinter.CTkImage(light_image=Image.open("footballplot.png"),size=(390,536))
label_bg7  = customtkinter.CTkImage(light_image=Image.open("scoressemis.jpg"),size=(390,536))
label_bg8  = customtkinter.CTkImage(light_image=Image.open("Figure_1_goalden.png"),size=(390,536))
label_bg9  = customtkinter.CTkImage(light_image=Image.open("cup_bg2.png"),size=(390,536))
label_bg10  = customtkinter.CTkImage(light_image=Image.open("aus1.jpg"),size=(390,536))
label_bg11 = customtkinter.CTkImage(light_image=Image.open("spain4.jpg"),size=(390,536))
label_bg12 = customtkinter.CTkImage(light_image=Image.open("spain2.jpg"),size=(390,536))
label_bg13 = customtkinter.CTkImage(light_image=Image.open("a8.png"),size=(390,536))
label_bg14 = customtkinter.CTkImage(light_image=Image.open("newfifawordcloud.png"),size=(390,536))
label_bg15 = customtkinter.CTkImage(light_image=Image.open("women_fifa.png"),size=(390,536))

#global my_imagees
count = -1
my_images= [label_bg1,label_bg2,label_bg3,label_bg4,label_bg5,label_bg6,label_bg7,label_bg8,label_bg9,
           label_bg10,label_bg11,label_bg12,label_bg13,label_bg14,label_bg15]


def next_image():
    global count
    if count == 14:
        home_label1 = customtkinter.CTkLabel(label_bg, text="", image=my_images[0])
        home_label1.place(relx=0.0, rely=0)
        count = 0

    else:
        home_label1 = customtkinter.CTkLabel(label_bg, text="", image=my_images[count+1])
        home_label1.place(relx=0.0, rely=0)
        count +=1

    window.after(2000,next_image)

next_image()

"""def slide_images():
    global i
    i += 1
    if i == 1:
        label1.place(relx=0.1, rely=0.1)
    elif i == 2:
        label1.place(relx=1.5, rely=0.2)
        label2.place(relx=0, rely=0.2)
    elif i == 3:
        label2.place(relx=1.5, rely=0.2)
        label3.place(relx=0, rely=0)
    elif i == 4:
        label3.place(relx=1.5, rely=0.2)
        label4.place(relx=0, rely=0.2)
    elif i == 5:
        label4.place(relx=1.5, rely=0.2)
        label5.place(relx=0, rely=0.2)
    elif i == 6:
        label5.place(relx=1.5, rely=0.2)
        label6.place(relx=0.03, rely=0.1)
    window.after(3000, slide_images)
    if i == 7:
       label6.place(relx=1.5, rely=0.2)
i = 0"""
photo2 =customtkinter.CTkImage(light_image=Image.open("button.png"),size=(20,20),)
#button = customtkinter.CTkButton(window,command=slide_images,compound='left',
#                                 fg_color='purple',hover_color="green",
#                                 width=50,height=30,text="FifaWC",image=photo2)
#button.place(relx=0.15,rely=0.93,)
#root.after(2000, slide_images)
#button = tk.Button(window, text="Slide Images", command=slide_images)
#button.pack()"""


#background image
cup_image = Image.open("cup.png")
resized_photo = cup_image.resize((1000,800))
bg_cup = ImageTk.PhotoImage(resized_photo)

"""cup_image1 = Image.open("women_fifa.png")
resized_photo1 = cup_image1.resize((1200,800))
bg_cup1 = ImageTk.PhotoImage(resized_photo1)


cup_image2 = Image.open("cup_bg2.png")
resized_photo2 = cup_image2.resize((1200,800))
bg_cup2 = ImageTk.PhotoImage(resized_photo2)

cup_image3 = Image.open("cup_bg1.png")
resized_photo3 = cup_image3.resize((1200,800))
bg_cup3 = ImageTk.PhotoImage(resized_photo3)




my_images = [bg_cup, bg_cup1, bg_cup2, bg_cup3]"""



#createcanvas instance
fifa_canvas = Canvas(window,width=WIDTH,height=HEIGHT)
fifa_canvas.place(relx=0.001,rely=0.001)
background_image = fifa_canvas.create_image(0,0,image=bg_cup,anchor="nw")
#count = -1

"""def next_image():
    global count
    if count == 2:
        fifa_canvas.create_image(0, 0, image=my_images[0], anchor="nw")
        count = 0
    else:
        fifa_canvas.create_image(0, 0, image=my_images[count + 1], anchor="nw")
        count += 1

    window.after(3000,next_image)

next_image()"""




#CREATING HE FLAG LOGOS
#argentina
"""arg = Image.open("Argentina.PNG")
resized_arg = arg.resize((100,80))
arg_flag = ImageTk.PhotoImage(resized_arg)
argentina_flag = fifa_canvas.create_image(0,0,image=arg_flag,anchor='nw')
argentina_flag_width = arg_flag.width()
argentina_flag_height= arg_flag.height()"""
arg_out = customtkinter.CTkImage(light_image=Image.open("Argentina.PNG"), size=(65, 50))
arg_out_label = customtkinter.CTkLabel(window,text="",image=arg_out)
arg_out_label.place(relx=0.56,rely=0.4)

#Austraila
aus = Image.open("Austrailia.PNG")
resized_aus = aus.resize((140,120))
aus_flag = ImageTk.PhotoImage(resized_aus)
australia_flag = fifa_canvas.create_image(0,100,image=aus_flag,anchor='nw')
australia_flag_width = aus_flag.width()
australia_flag_height= aus_flag.height()

#Brazil
"""bra = Image.open("Brazil.PNG")
resized_bra = bra.resize((100,80))
bra_flag = ImageTk.PhotoImage(resized_bra)
brazil_flag = fifa_canvas.create_image(0,300,image=bra_flag,anchor='nw')
brazil_flag_width = bra_flag.width()
brazil_flag_height= bra_flag.height()"""
bra_out = customtkinter.CTkImage(light_image=Image.open("Brazil.PNG"), size=(65, 50))
bra_out_label = customtkinter.CTkLabel(window,text="",image=bra_out)
bra_out_label.place(relx=0.617,rely=0.6)

#canada flag
"""can = Image.open("Canada.PNG")
resized_can = can.resize((100,80))
can_flag = ImageTk.PhotoImage(resized_can)
canada_flag = fifa_canvas.create_image(200,0,image=can_flag,anchor='nw')
canada_flag_width = can_flag.width()
canada_flag_height= can_flag.height()"""
canada_out = customtkinter.CTkImage(light_image=Image.open("Canada.PNG"), size=(65, 50))
canada_out_label = customtkinter.CTkLabel(window,text="",image=canada_out)
canada_out_label.place(relx=0.56,rely=0)
#china flag
"""chinko = Image.open("china.PNG")
resized_chinko = chinko.resize((100,80))
chinko_flag = ImageTk.PhotoImage(resized_chinko)
china_flag = fifa_canvas.create_image(350,0,image=chinko_flag,anchor='nw')
china_flag_width = chinko_flag.width()
china_flag_height= chinko_flag.height()"""
china_out = customtkinter.CTkImage(light_image=Image.open("china.PNG"), size=(65, 50))
china_out_label = customtkinter.CTkLabel(window,text="",image=china_out)
china_out_label.place(relx=0.617,rely=0)

#coastarica flag
"""coast = Image.open("coastarica.PNG")
resized_coast = coast.resize((100,80))
coast_flag = ImageTk.PhotoImage(resized_coast)
coastarica_flag = fifa_canvas.create_image(0,700,image=coast_flag,anchor='nw')
coastarica_flag_width = coast_flag.width()
coastarica_flag_height= coast_flag.height()"""
coast_out = customtkinter.CTkImage(light_image=Image.open("coastarica.PNG"), size=(65, 50))
coastarica_out_label = customtkinter.CTkLabel(window,text="",image=coast_out)
coastarica_out_label.place(relx=0.56,rely=0.1)
#columbia flag
"""col = Image.open("columbia.PNG")
resized_col = col.resize((140,120))
col_flag = ImageTk.PhotoImage(resized_col)
columbia_flag = fifa_canvas.create_image(500,0,image=col_flag,anchor='nw')
columbia_flag_width = col_flag.width()
columbia_flag_height= col_flag.height()"""
col_out = customtkinter.CTkImage(light_image=Image.open("columbia.PNG"), size=(65, 50))
col_out_label = customtkinter.CTkLabel(window,text="",image=col_out)
col_out_label.place(relx=0.158,rely=0.89)


#denmark flag
"""den = Image.open("denmark.PNG")
resized_den = den.resize((120,100))
den_flag = ImageTk.PhotoImage(resized_den)
denmark_flag = fifa_canvas.create_image(350,500,image=den_flag,anchor='w')
denmark_flag_width = den_flag.width()
denmark_flag_height= den_flag.height()"""
den_out = customtkinter.CTkImage(light_image=Image.open("denmark.PNG"), size=(65, 50))
den_out_label = customtkinter.CTkLabel(window,text="",image=den_out)
den_out_label.place(relx=0.503,rely=0.89)

#england flag
eng = Image.open("england.PNG")
resized_eng = eng.resize((140,120))
eng_flag = ImageTk.PhotoImage(resized_eng)
england_flag = fifa_canvas.create_image(0,300,image=eng_flag,anchor='nw')
england_flag_width = eng_flag.width()
england_flag_height= eng_flag.height()


#france flag
"""franc = Image.open("france.PNG")
resized_franc = franc.resize((140,120))
franc_flag = ImageTk.PhotoImage(resized_franc)
france_flag = fifa_canvas.create_image(200,600,image=franc_flag,anchor='nw')
france_flag_width = franc_flag.width()
france_flag_height= franc_flag.height()"""
franc_out = customtkinter.CTkImage(light_image=Image.open("france.PNG"), size=(65, 50))
franc_out_label = customtkinter.CTkLabel(window,text="",image=franc_out)
franc_out_label.place(relx=0.675,rely=0.89)

#germany flag
"""ger = Image.open("germany.PNG")
resized_ger = ger.resize((120,100))
ger_flag = ImageTk.PhotoImage(resized_ger)
germany_flag = fifa_canvas.create_image(700,300,image=ger_flag,anchor='nw')
germany_flag_width = ger_flag.width()
germany_flag_height= ger_flag.height()"""
ger_out = customtkinter.CTkImage(light_image=Image.open("germany.PNG"), size=(65, 50))
germany_out_label = customtkinter.CTkLabel(window,text="",image=ger_out)
germany_out_label.place(relx=0.617,rely=0.7)

#haiti flag
"""hai = Image.open("Haiti.PNG")
resized_hai = hai.resize((100,80))
hai_flag = ImageTk.PhotoImage(resized_hai)
haiti_flag = fifa_canvas.create_image(250,550,image=hai_flag,anchor='nw')
haiti_flag_width = hai_flag.width()
haiti_flag_height= hai_flag.height()"""
haiti_out = customtkinter.CTkImage(light_image=Image.open("Haiti.PNG"), size=(65, 50))
haiti_out_label = customtkinter.CTkLabel(window,text="",image=haiti_out)
haiti_out_label.place(relx=0.617,rely=0.1)

#england flag
"""itly = Image.open("italy.PNG")
resized_itly = itly.resize((100,80))
itly_flag = ImageTk.PhotoImage(resized_itly)
italy_flag = fifa_canvas.create_image(500,700,image=itly_flag,anchor='sw')
italy_flag_width = itly_flag.width()
italy_flag_height= itly_flag.height()"""
ity_out = customtkinter.CTkImage(light_image=Image.open("italy.PNG"), size=(65, 50))
ity_out_label = customtkinter.CTkLabel(window,text="",image=ity_out)
ity_out_label.place(relx=0.56,rely=0.6)

#jamaica flag
"""jam = Image.open("jamaica.PNG")
resized_jam = jam.resize((120,100))
jam_flag = ImageTk.PhotoImage(resized_jam)
jamaica_flag = fifa_canvas.create_image(500,600,image=jam_flag,anchor='sw')
jamaica_flag_width = jam_flag.width()
jamaica_flag_height= jam_flag.height()"""
jam_out = customtkinter.CTkImage(light_image=Image.open("jamaica.PNG"), size=(65, 50))
jam_out_label = customtkinter.CTkLabel(window,text="",image=jam_out)
jam_out_label.place(relx=0.56,rely=0.89)

#japan flag
"""jap = Image.open("japan.PNG")
resized_jap = jap.resize((140,120))
jap_flag = ImageTk.PhotoImage(resized_jap)
japan_flag = fifa_canvas.create_image(450,460,image=jap_flag,anchor='sw')
japan_flag_width = jap_flag.width()
japan_flag_height= jap_flag.height()"""
jap_out = customtkinter.CTkImage(light_image=Image.open("japan.PNG"), size=(65, 50))
jap_out_label = customtkinter.CTkLabel(window,text="",image=jap_out)
jap_out_label.place(relx=0.215,rely=0.89)

#korea flag
"""kor = Image.open("korea.PNG")
resized_kor = kor.resize((100,80))
kor_flag = ImageTk.PhotoImage(resized_kor)
korea_flag = fifa_canvas.create_image(700,700,image=kor_flag,anchor='sw')
korea_flag_width = kor_flag.width()
korea_flag_height= kor_flag.height()"""
korea_out = customtkinter.CTkImage(light_image=Image.open("korea.PNG"), size=(65, 50))
korea_out_label = customtkinter.CTkLabel(window,text="",image=korea_out)
korea_out_label.place(relx=0.56,rely=0.7)

#morroco flag
"""maroc = Image.open("morroco.PNG")
resized_mar = maroc.resize((120,100))
maroc_flag = ImageTk.PhotoImage(resized_mar)
morroco_flag = fifa_canvas.create_image(650,500,image=maroc_flag,anchor='sw')
morroco_flag_width = maroc_flag.width()
morroco_flag_height= maroc_flag.height()"""
mar_out = customtkinter.CTkImage(light_image=Image.open("morroco.PNG"), size=(65, 50))
mar_out_label = customtkinter.CTkLabel(window,text="",image=mar_out)
mar_out_label.place(relx=0.56,rely=0.8)
#naija flag
"""naija = Image.open("naija.PNG")
resized_naija = naija.resize((120,100))
naija_flag = ImageTk.PhotoImage(resized_naija)
nigeria_flag = fifa_canvas.create_image(850,500,image=naija_flag,anchor='nw')
nigeria_flag_width = naija_flag.width()
nigeria_flag_height= naija_flag.height()"""
naija_out = customtkinter.CTkImage(light_image=Image.open("naija.PNG"), size=(65, 50))
naija_out_label = customtkinter.CTkLabel(window,text="",image=naija_out)
naija_out_label.place(relx=0.617,rely=0.8)

#netherlands flag
"""ned = Image.open("netherlands.PNG")
resized_ned = ned.resize((120,100))
ned_flag = ImageTk.PhotoImage(resized_ned)
netherlands_flag = fifa_canvas.create_image(510,320,image=ned_flag,anchor='sw')
netherlands_flag_width = ned_flag.width()
netherlands_flag_height= ned_flag.height()"""
ned_out = customtkinter.CTkImage(light_image=Image.open("netherlands.PNG"), size=(65, 50))
ned_out_label = customtkinter.CTkLabel(window,text="",image=ned_out)
ned_out_label.place(relx=0.617,rely=0.89)

#newzealand flag
"""new = Image.open("newzealand.PNG")
resized_new = new.resize((100,80))
new_flag = ImageTk.PhotoImage(resized_new)
newzealand_flag = fifa_canvas.create_image(1000,500,image=new_flag,anchor='sw')
newzealand_flag_width = new_flag.width()
newzealand_flag_height= new_flag.height()"""
new_out = customtkinter.CTkImage(light_image=Image.open("newzealand.PNG"), size=(65, 50))
new_out_label = customtkinter.CTkLabel(window,text="",image=new_out)
new_out_label.place(relx=0.617,rely=0.2)

#norway flag
"""nor = Image.open("norway.PNG")
resized_nor = nor.resize((120,100))
nor_flag = ImageTk.PhotoImage(resized_nor)
norway_flag = fifa_canvas.create_image(80,600,image=nor_flag,anchor='sw')
norway_flag_width = nor_flag.width()
norway_flag_height= nor_flag.height()"""
nor_out = customtkinter.CTkImage(light_image=Image.open("norway.PNG"), size=(65, 50))
nor_out_label = customtkinter.CTkLabel(window,text="",image=nor_out)
nor_out_label.place(relx=0.445,rely=0.89)

#panama flag
"""pan = Image.open("panama.PNG")
resized_pan = pan.resize((100,80))
pan_flag = ImageTk.PhotoImage(resized_pan)
panama_flag = fifa_canvas.create_image(900,350,image=pan_flag,anchor='sw')
panama_flag_width = pan_flag.width()
panama_flag_height= pan_flag.height()"""
pan_out = customtkinter.CTkImage(light_image=Image.open("panama.PNG"), size=(65, 50))
pan_out_label = customtkinter.CTkLabel(window,text="",image=pan_out)
pan_out_label.place(relx=0.56,rely=0.2)

#philiphines flag
"""phi = Image.open("phillipines.PNG")
resized_phi = phi.resize((100,80))
phi_flag = ImageTk.PhotoImage(resized_phi)
philiphines_flag = fifa_canvas.create_image(500,500,image=phi_flag,anchor='sw')
philiphines_flag_width = phi_flag.width()
philiphines_flag_height= phi_flag.height()"""
phi_out = customtkinter.CTkImage(light_image=Image.open("phillipines.PNG"), size=(65, 50))
phi_out_label = customtkinter.CTkLabel(window,text="",image=phi_out)
phi_out_label.place(relx=0.56,rely=0.3)

#portugual flag
"""port = Image.open("portugual.PNG")
resized_port = port.resize((100,80))
port_flag = ImageTk.PhotoImage(resized_port)
portugual_flag = fifa_canvas.create_image(300,200,image=port_flag,anchor='sw')
portugual_flag_width = port_flag.width()
portugual_flag_height= port_flag.height()"""
port_out = customtkinter.CTkImage(light_image=Image.open("portugual.PNG"), size=(65, 50))
port_out_label = customtkinter.CTkLabel(window,text="",image=port_out)
port_out_label.place(relx=0.617,rely=0.4)

#ireland flag
"""ire = Image.open("republic_du_ireland.PNG")
resized_ire = ire.resize((100,80))
ire_flag = ImageTk.PhotoImage(resized_ire)
rep_ireland_flag = fifa_canvas.create_image(1100,600,image=ire_flag,anchor='sw')
rep_ireland_flag_width = ire_flag.width()
rep_ireland_flag_height= ire_flag.height()"""
ire_out = customtkinter.CTkImage(light_image=Image.open("republic_du_ireland.PNG"), size=(65, 50))
ire_out_label = customtkinter.CTkLabel(window,text="",image=ire_out)
ire_out_label.place(relx=0.617,rely=0.3)

#southafrica flag
"""south = Image.open("South_africa.PNG")
resized_south = south.resize((120,100))
south_flag = ImageTk.PhotoImage(resized_south)
southafrica_flag = fifa_canvas.create_image(280,300,image=south_flag,anchor='sw')
southafrica_flag_width = south_flag.width()
southafrica_flag_height= south_flag.height()"""
south_out = customtkinter.CTkImage(light_image=Image.open("South_africa.PNG"), size=(65, 50))
south_out_label = customtkinter.CTkLabel(window,text="",image=south_out)
south_out_label.place(relx=0.387,rely=0.89)

#spain flag
esp = Image.open("spain.PNG")
resized_esp = esp.resize((140,120))
esp_flag = ImageTk.PhotoImage(resized_esp)
spain_flag = fifa_canvas.create_image(350,750,image=esp_flag,anchor='sw')
spain_flag_width = esp_flag.width()
spain_flag_height= esp_flag.height()

#sweden flag
swd = Image.open("sweden.PNG")
resized_swd = swd.resize((140,120))
swd_flag = ImageTk.PhotoImage(resized_swd)
sweden_flag = fifa_canvas.create_image(750,250,image=swd_flag,anchor='sw')
sweden_flag_width = swd_flag.width()
sweden_flag_height= swd_flag.height()

#switzerland flag
"""switz = Image.open("switzerland.PNG")
resized_switz = switz.resize((120,100))
switz_flag = ImageTk.PhotoImage(resized_switz)
switzerland_flag = fifa_canvas.create_image(100,500,image=switz_flag,anchor='sw')
switzerland_flag_width = switz_flag.width()
switzerland_flag_height= switz_flag.height()"""
switz_out = customtkinter.CTkImage(light_image=Image.open("switzerland.PNG"), size=(65, 50))
switz_out_label = customtkinter.CTkLabel(window,text="",image=switz_out)
switz_out_label.place(relx=0.330,rely=0.89)

#usa flag
"""us = Image.open("usa.PNG")
resized_us = us.resize((120,100))
us_flag = ImageTk.PhotoImage(resized_us)
usa_flag = fifa_canvas.create_image(300,400,image=us_flag,anchor='sw')
usa_flag_width = us_flag.width()
usa_flag_height= us_flag.height()"""
usa_out = customtkinter.CTkImage(light_image=Image.open("usa.PNG"), size=(65, 50))
usa_out_label = customtkinter.CTkLabel(window,text="",image=usa_out)
usa_out_label.place(relx=0.273,rely=0.89)

#veitnam flag
"""vet = Image.open("vietnam.PNG")
resized_vet = vet.resize((100,80))
vet_flag = ImageTk.PhotoImage(resized_vet)
veitnam_flag = fifa_canvas.create_image(1000,250,image=vet_flag,anchor='sw')
veitnam_flag_width = vet_flag.width()
veitnam_flag_height= vet_flag.height()"""
vet_out = customtkinter.CTkImage(light_image=Image.open("vietnam.PNG"), size=(65, 50))
vet_out_label = customtkinter.CTkLabel(window,text="",image=vet_out)
vet_out_label.place(relx=0.56,rely=0.5)


#zambia flag
"""zam = Image.open("zambia.PNG")
resized_zam = zam.resize((100,80))
zam_flag = ImageTk.PhotoImage(resized_zam)
zambia_flag = fifa_canvas.create_image(900,650,image=zam_flag,anchor='sw')
zambia_flag_width = zam_flag.width()
zambia_flag_height= zam_flag.height()"""
zam_out = customtkinter.CTkImage(light_image=Image.open("zambia.PNG"), size=(65, 50))
zam_out_label = customtkinter.CTkLabel(window,text="",image=zam_out)
zam_out_label.place(relx=0.617,rely=0.5)


#Creating button for the canvas to move and waits the flags
images_running = False
def start_pause():
    global images_running
    if images_running:
        images_running= False
        mov_button.configure(text="Pause")
        start()
    else:
        images_running = True
        mov_button.configure(text="Start")
        fifa_canvas.wait_window()

#Buuton to trigger the start and pause
mov_button = customtkinter.CTkButton(window,fg_color="transparent", height=30,width=150,image=photo2,
                                     text="Start",command=start_pause,state="flat")
mov_button.place(relx=0,rely=0.93,)

#This function is to call the images to move after running the program
def start():
    WIDTH = 1000
    HEIGHT = 800
    #argentina_xvelocity  = 2
    #argentina_yvelocity  = -1
    australia_xvelocity  = 1
    australia_yvelocity  = -2
    #brazil_xvelocity     = -2
    #brazil_yvelocity     = -2
    #canada_xvelocity     = 1.2
    #canada_yvelocity     = 1.3
    #china_xvelocity      = 1.4
    #china_yvelocity      = -1.3
    #coastarica_xvelocity = -2.1
    #coastarica_yvelocity = 1.5
    #columbia_xvelocity   = 1.7
    #columbia_yvelocity   = -1.4
    #denmark_xvelocity    = -1.7
    #denmark_yvelocity    = 1.4
    england_xvelocity    = 1.5
    england_yvelocity    = -2.4
    ###france_xvelocity     = 2.7
    ###france_yvelocity     = -1.4
    #germany_xvelocity    = 1.9
    #germany_yvelocity    = -2.4
    #haiti_xvelocity      = 2.7
    #haiti_yvelocity      = -2.4
    #italy_xvelocity      = 2.7
    #italy_yvelocity      = -2.4
    #jamaica_xvelocity = 2
    #jamaica_yvelocity = 1.4
    #japan_xvelocity =-1.4
    #japan_yvelocity = 1.7
    #korea_xvelocity = 2.7
    #korea_yvelocity = -1.4
    #morroco_xvelocity = 1
    #morroco_yvelocity = -2.4
    #naija_xvelocity = 1
    #naija_yvelocity = -3.4
    #netherlands_xvelocity = 2.7
    #netherlands_yvelocity = -4.4

    #newzealand_xvelocity = -2.3
    #newzealand_yvelocity = 3.4
    #norway_xvelocity = -2.1
    #norway_yvelocity = 2.4
    #panama_xvelocity = 2.7
    #panama_yvelocity = -1.4
    #philiphines_xvelocity = 3
    #philiphines_yvelocity = -2.4
    #portugual_xvelocity = 1.7
    #portugual_yvelocity = -3.4
    #ireland_xvelocity = 2.7
    #ireland_yvelocity = -4.4

    #southafrica_xvelocity = -2.3
    #southafrica_yvelocity = 1.4
    spain_xvelocity = 1.5
    spain_yvelocity = -1.4
    sweden_xvelocity = -1.7
    sweden_yvelocity = 1.5
    #switzerland_xvelocity = 1
    #switzerland_yvelocity = -2.4
    #usa_xvelocity = -1.7
    #usa_yvelocity = 3.4
    #veitnam_xvelocity = -2.7
    #veitnam_yvelocity = 2.4
    #zambia_xvelocity = -3.7
    #zambia_yvelocity = -1.4


    while True:
        # Settings the coordinates of the flag for argentina
        """argentina_flag_coordinates = fifa_canvas.coords(argentina_flag)
        if ((argentina_flag_coordinates[0] >= WIDTH - argentina_flag_width) or argentina_flag_coordinates[0] < 0):
            argentina_xvelocity = -argentina_xvelocity
        elif (argentina_flag_coordinates[1] >= (HEIGHT - argentina_flag_height) or argentina_flag_coordinates[1] < 0):
            argentina_yvelocity = -argentina_yvelocity

        fifa_canvas.move(argentina_flag, argentina_xvelocity, argentina_yvelocity)"""

        # Settings the coordinates of the flag for australia
        australia_flag_coordinates = fifa_canvas.coords(australia_flag)
        if ((australia_flag_coordinates[0] >= WIDTH - australia_flag_width) or australia_flag_coordinates[0] < 0):
            australia_xvelocity = -australia_xvelocity
        elif (australia_flag_coordinates[1] >= (HEIGHT - australia_flag_height) or australia_flag_coordinates[1] < 0):
            australia_yvelocity = -australia_yvelocity

        fifa_canvas.move(australia_flag,australia_xvelocity,australia_yvelocity)


        # Settings the coordinates of the flag for brazil
        """brazil_flag_coordinates = fifa_canvas.coords(brazil_flag)
        if ((brazil_flag_coordinates[0] >= WIDTH-brazil_flag_width) or brazil_flag_coordinates[0] < 0):
            brazil_xvelocity = -brazil_xvelocity
        elif (brazil_flag_coordinates[1] >= (HEIGHT-brazil_flag_height) or brazil_flag_coordinates[1] < 0):
            brazil_yvelocity = -brazil_yvelocity

        fifa_canvas.move(brazil_flag,brazil_xvelocity,brazil_yvelocity)"""

        # Settings the coordinates of the flag for canada
        """canada_flag_coordinates = fifa_canvas.coords(canada_flag)
        if ((canada_flag_coordinates[0] >= WIDTH-canada_flag_width) or canada_flag_coordinates[0] < 0):
            canada_xvelocity = -canada_xvelocity
        elif (canada_flag_coordinates[1] >= (HEIGHT-canada_flag_height) or canada_flag_coordinates[1] < 0):
            canada_yvelocity = -canada_yvelocity

        fifa_canvas.move(canada_flag,canada_xvelocity,canada_yvelocity)"""


        # Settings the coordinates of the flag for china
        """china_flag_coordinates = fifa_canvas.coords(china_flag)
        if ((china_flag_coordinates[0] >= WIDTH-china_flag_width) or china_flag_coordinates[0] < 0):
            china_xvelocity = -china_xvelocity
        elif (china_flag_coordinates[1] >= (HEIGHT-china_flag_height) or china_flag_coordinates[1] < 0):
            china_yvelocity = -china_yvelocity

        fifa_canvas.move(china_flag,china_xvelocity,china_yvelocity)"""


        # Settings the coordinates of the flag for coastarica
        """coastarica_flag_coordinates = fifa_canvas.coords(coastarica_flag)
        if ((coastarica_flag_coordinates[0] >= WIDTH - coastarica_flag_width) or coastarica_flag_coordinates[0] < 0):
            coastarica_xvelocity = -coastarica_xvelocity
        elif (coastarica_flag_coordinates[1] >= (HEIGHT - coastarica_flag_height) or coastarica_flag_coordinates[1] < 0):
            coastarica_yvelocity = -coastarica_yvelocity

        fifa_canvas.move(coastarica_flag,coastarica_xvelocity,coastarica_yvelocity)"""


        # Settings the coordinates of the flag for columbia
        """columbia_flag_coordinates = fifa_canvas.coords(columbia_flag)
        if ((columbia_flag_coordinates[0] >= WIDTH-columbia_flag_width) or columbia_flag_coordinates[0] < 0):
            columbia_xvelocity = -columbia_xvelocity
        elif (columbia_flag_coordinates[1] >= (HEIGHT-columbia_flag_height) or columbia_flag_coordinates[1] < 0):
            columbia_yvelocity = -columbia_yvelocity

        fifa_canvas.move(columbia_flag,columbia_xvelocity,columbia_yvelocity)"""

        window.update()
        time.sleep(0.001)
        # Settings the coordinates of the flag for denmark
        """denmark_flag_coordinates = fifa_canvas.coords(denmark_flag)
        if ((denmark_flag_coordinates[0] >= WIDTH - denmark_flag_width) or denmark_flag_coordinates[0] < 0):
            denmark_xvelocity = -denmark_xvelocity
        elif (denmark_flag_coordinates[1] >= (HEIGHT - denmark_flag_height) or denmark_flag_coordinates[1] < 0):
            denmark_yvelocity = -denmark_yvelocity

        fifa_canvas.move(denmark_flag, denmark_xvelocity,denmark_yvelocity)"""

        # Settings the coordinates of the flag for england
        england_flag_coordinates = fifa_canvas.coords(england_flag)
        if ((england_flag_coordinates[0] >= WIDTH - england_flag_width) or england_flag_coordinates[0] < 0):
            england_xvelocity = -england_xvelocity
        elif (england_flag_coordinates[1] >= (HEIGHT - england_flag_height) or england_flag_coordinates[1] < 0):
            england_yvelocity = -england_yvelocity

        fifa_canvas.move(england_flag, england_xvelocity, england_yvelocity)

        # Settings the coordinates of the flag for france
        """france_flag_coordinates = fifa_canvas.coords(france_flag)
        if ((france_flag_coordinates[0] >= WIDTH - france_flag_width) or france_flag_coordinates[0] < 0):
            france_xvelocity = -france_xvelocity
        elif (france_flag_coordinates[1] >= (HEIGHT - france_flag_height) or france_flag_coordinates[1] < 0):
            france_yvelocity = -france_yvelocity

        fifa_canvas.move(france_flag, france_xvelocity, france_yvelocity)

        # Settings the coordinates of the flag for germany
        germany_flag_coordinates = fifa_canvas.coords(germany_flag)
        if ((germany_flag_coordinates[0] >= WIDTH - germany_flag_width) or germany_flag_coordinates[0] < 0):
            germany_xvelocity = -germany_xvelocity
        elif (germany_flag_coordinates[1] >= (HEIGHT - germany_flag_height) or germany_flag_coordinates[1] < 0):
            germany_yvelocity = -germany_yvelocity

        fifa_canvas.move(germany_flag, germany_xvelocity, germany_yvelocity)

        # Settings the coordinates of the flag for haiti
        haiti_flag_coordinates = fifa_canvas.coords(haiti_flag)
        if ((haiti_flag_coordinates[0] >= WIDTH - haiti_flag_width) or haiti_flag_coordinates[0] < 0):
            haiti_xvelocity = -haiti_xvelocity
        elif (haiti_flag_coordinates[1] >= (HEIGHT - haiti_flag_height) or haiti_flag_coordinates[1] < 0):
            haiti_yvelocity = -haiti_yvelocity

        fifa_canvas.move(haiti_flag, haiti_xvelocity, haiti_yvelocity)

        # Settings the coordinates of the flag for italy
        italy_flag_coordinates = fifa_canvas.coords(italy_flag)
        if ((italy_flag_coordinates[0] >= WIDTH - italy_flag_width) or italy_flag_coordinates[0] < 0):
            italy_xvelocity = -italy_xvelocity
        elif (italy_flag_coordinates[1] >= (HEIGHT - italy_flag_height) or italy_flag_coordinates[1] < 0):
            italy_yvelocity = -italy_yvelocity

        fifa_canvas.move(italy_flag, italy_xvelocity, italy_yvelocity)

        # Settings the coordinates of the flag for jamaica
        jamaica_flag_coordinates = fifa_canvas.coords(jamaica_flag)
        if ((jamaica_flag_coordinates[0] >= WIDTH - jamaica_flag_width) or jamaica_flag_coordinates[0] < 0):
            jamaica_xvelocity = -jamaica_xvelocity
        elif (jamaica_flag_coordinates[1] >= (HEIGHT - jamaica_flag_height) or jamaica_flag_coordinates[1] < 0):
            jamaica_yvelocity = -jamaica_yvelocity

        fifa_canvas.move(jamaica_flag,jamaica_xvelocity,jamaica_yvelocity)

        # Settings the coordinates of the flag for japan
        japan_flag_coordinates = fifa_canvas.coords(japan_flag)
        if ((japan_flag_coordinates[0] >= WIDTH - japan_flag_width) or japan_flag_coordinates[0] < 0):
            japan_xvelocity = -japan_xvelocity
        elif (japan_flag_coordinates[1] >= (HEIGHT - japan_flag_height) or japan_flag_coordinates[1] < 0):
            japan_yvelocity = -japan_yvelocity

        fifa_canvas.move(japan_flag, japan_xvelocity, japan_yvelocity)

        # Settings the coordinates of the flag for korea
        korea_flag_coordinates = fifa_canvas.coords(korea_flag)
        if ((korea_flag_coordinates[0] >= WIDTH - korea_flag_width) or korea_flag_coordinates[0] < 0):
            korea_xvelocity = -korea_xvelocity
        elif (korea_flag_coordinates[1] >= (HEIGHT - korea_flag_height) or korea_flag_coordinates[1] < 0):
            korea_yvelocity = -korea_yvelocity

        fifa_canvas.move(korea_flag, korea_xvelocity, korea_yvelocity)

        # Settings the coordinates of the flag for morroco
        morroco_flag_coordinates = fifa_canvas.coords(morroco_flag)
        if ((morroco_flag_coordinates[0] >= WIDTH - morroco_flag_width) or morroco_flag_coordinates[0] < 0):
            morroco_xvelocity = -morroco_xvelocity
        elif (morroco_flag_coordinates[1] >= (HEIGHT - morroco_flag_height) or morroco_flag_coordinates[1] < 0):
            morroco_yvelocity = -morroco_yvelocity

        fifa_canvas.move(morroco_flag, morroco_xvelocity, morroco_yvelocity)

        # Settings the coordinates of the flag for naija
        naija_flag_coordinates = fifa_canvas.coords(nigeria_flag)
        if ((naija_flag_coordinates[0] >= WIDTH - nigeria_flag_width) or naija_flag_coordinates[0] < 0):
            naija_xvelocity = -naija_xvelocity
        elif (naija_flag_coordinates[1] >= (HEIGHT - nigeria_flag_height) or naija_flag_coordinates[1] < 0):
            naija_yvelocity = -naija_yvelocity

        fifa_canvas.move(nigeria_flag,naija_xvelocity,naija_yvelocity)

        # Settings the coordinates of the flag for netherlands
        netherlands_flag_coordinates = fifa_canvas.coords(netherlands_flag)
        if ((netherlands_flag_coordinates[0] >= WIDTH - netherlands_flag_width) or netherlands_flag_coordinates[0] < 0):
            netherlands_xvelocity = -netherlands_xvelocity
        elif (netherlands_flag_coordinates[1] >= (HEIGHT - netherlands_flag_height) or netherlands_flag_coordinates[1] < 0):
            netherlands_yvelocity = -netherlands_yvelocity

        fifa_canvas.move(netherlands_flag,netherlands_xvelocity,netherlands_yvelocity)

        # Settings the coordinates of the flag for newzealand
        newzealand_flag_coordinates = fifa_canvas.coords(newzealand_flag)
        if ((newzealand_flag_coordinates[0] >= WIDTH - newzealand_flag_width) or newzealand_flag_coordinates[0] < 0):
            newzealand_xvelocity = -newzealand_xvelocity
        elif (newzealand_flag_coordinates[1] >= (HEIGHT - newzealand_flag_height) or newzealand_flag_coordinates[1] < 0):
            newzealand_yvelocity = -newzealand_yvelocity

        fifa_canvas.move(newzealand_flag,newzealand_xvelocity,newzealand_yvelocity)

        # Settings the coordinates of the flag for norway
        norway_flag_coordinates = fifa_canvas.coords(norway_flag)
        if ((norway_flag_coordinates[0] >= WIDTH - norway_flag_width) or norway_flag_coordinates[0] < 0):
            norway_xvelocity = -norway_xvelocity
        elif (norway_flag_coordinates[1] >= (HEIGHT - norway_flag_height) or norway_flag_coordinates[1] < 0):
            norway_yvelocity = -norway_yvelocity

        fifa_canvas.move(norway_flag,norway_xvelocity,norway_yvelocity)

        # Settings the coordinates of the flag for panama
        panama_flag_coordinates = fifa_canvas.coords(panama_flag)
        if ((panama_flag_coordinates[0] >= WIDTH - panama_flag_width) or panama_flag_coordinates[0] < 0):
            panama_xvelocity = -panama_xvelocity
        elif (panama_flag_coordinates[1] >= (HEIGHT - panama_flag_height) or panama_flag_coordinates[1] < 0):
            panama_yvelocity = -panama_yvelocity

        fifa_canvas.move(panama_flag,panama_xvelocity,panama_yvelocity)

        # Settings the coordinates of the flag for philiphines
        philiphines_flag_coordinates = fifa_canvas.coords(philiphines_flag)
        if ((philiphines_flag_coordinates[0] >= WIDTH - philiphines_flag_width) or philiphines_flag_coordinates[0] < 0):
            philiphines_xvelocity = -philiphines_xvelocity
        elif (philiphines_flag_coordinates[1] >= (HEIGHT - philiphines_flag_height) or philiphines_flag_coordinates[1] < 0):
            philiphines_yvelocity = -philiphines_yvelocity

        fifa_canvas.move(philiphines_flag,philiphines_xvelocity,philiphines_yvelocity)

        # Settings the coordinates of the flag for portugual
        portugual_flag_coordinates = fifa_canvas.coords(portugual_flag)
        if ((portugual_flag_coordinates[0] >= WIDTH - portugual_flag_width) or portugual_flag_coordinates[0] < 0):
            portugual_xvelocity = -portugual_xvelocity
        elif (portugual_flag_coordinates[1] >= (HEIGHT - portugual_flag_height) or portugual_flag_coordinates[1] < 0):
            portugual_yvelocity = -portugual_yvelocity

        fifa_canvas.move(portugual_flag,portugual_xvelocity,portugual_yvelocity)

        # Settings the coordinates of the flag for ireland
        ireland_flag_coordinates = fifa_canvas.coords(rep_ireland_flag)
        if ((ireland_flag_coordinates[0] >= WIDTH - rep_ireland_flag_width) or ireland_flag_coordinates[0] < 0):
            ireland_xvelocity = -ireland_xvelocity
        elif (ireland_flag_coordinates[1] >= (HEIGHT - rep_ireland_flag_height) or ireland_flag_coordinates[1] < 0):
            ireland_yvelocity = -ireland_yvelocity

        fifa_canvas.move(rep_ireland_flag,ireland_xvelocity,ireland_yvelocity)

        # Settings the coordinates of the flag for southafrica
        southafrica_flag_coordinates = fifa_canvas.coords(southafrica_flag)
        if ((southafrica_flag_coordinates[0] >= WIDTH - southafrica_flag_width) or southafrica_flag_coordinates[0] < 0):
            southafrica_xvelocity = -southafrica_xvelocity
        elif (southafrica_flag_coordinates[1] >= (HEIGHT - southafrica_flag_height) or southafrica_flag_coordinates[1] < 0):
            southafrica_yvelocity = -southafrica_yvelocity

        fifa_canvas.move(southafrica_flag,southafrica_xvelocity,southafrica_yvelocity)"""

        # Settings the coordinates of the flag for spain
        spain_flag_coordinates = fifa_canvas.coords(spain_flag)
        if ((spain_flag_coordinates[0] >= WIDTH - spain_flag_width) or spain_flag_coordinates[0] < 0):
            spain_xvelocity = -spain_xvelocity
        elif (spain_flag_coordinates[1] >= (900 - spain_flag_height) or spain_flag_coordinates[1] < 0):
            spain_yvelocity = -spain_yvelocity

        fifa_canvas.move(spain_flag,spain_xvelocity,spain_yvelocity)

        # Settings the coordinates of the flag for sweden
        sweden_flag_coordinates = fifa_canvas.coords(sweden_flag)
        if ((sweden_flag_coordinates[0] >= WIDTH - sweden_flag_width) or sweden_flag_coordinates[0] < 0):
            sweden_xvelocity = -sweden_xvelocity
        elif (sweden_flag_coordinates[1] >= (900 - sweden_flag_height) or sweden_flag_coordinates[1] < 0):
            sweden_yvelocity = -sweden_yvelocity

        fifa_canvas.move(sweden_flag,sweden_xvelocity,sweden_yvelocity)

        # Settings the coordinates of the flag for switzerland
        """switzerland_flag_coordinates = fifa_canvas.coords(switzerland_flag)
        if ((switzerland_flag_coordinates[0] >= WIDTH - switzerland_flag_width) or switzerland_flag_coordinates[0] < 0):
            switzerland_xvelocity = -switzerland_xvelocity
        elif (switzerland_flag_coordinates[1] >= (HEIGHT - switzerland_flag_height) or switzerland_flag_coordinates[1] < 0):
            switzerland_yvelocity = -switzerland_yvelocity

        fifa_canvas.move(switzerland_flag,switzerland_xvelocity,switzerland_yvelocity)"""

        # Settings the coordinates of the flag for usa
        """usa_flag_coordinates = fifa_canvas.coords(usa_flag)
        if ((usa_flag_coordinates[0] >= WIDTH - usa_flag_width) or usa_flag_coordinates[0] < 0):
            usa_xvelocity = -usa_xvelocity
        elif (usa_flag_coordinates[1] >= (HEIGHT - usa_flag_height) or usa_flag_coordinates[1] < 0):
            usa_yvelocity = -usa_yvelocity

        fifa_canvas.move(usa_flag,usa_xvelocity,usa_yvelocity)"""

        # Settings the coordinates of the flag for veitnam
        """veitnam_flag_coordinates = fifa_canvas.coords(veitnam_flag)
        if ((veitnam_flag_coordinates[0] >= WIDTH - veitnam_flag_width) or veitnam_flag_coordinates[0] < 0):
            veitnam_xvelocity = -veitnam_xvelocity
        elif (veitnam_flag_coordinates[1] >= (HEIGHT - veitnam_flag_height) or veitnam_flag_coordinates[1] < 0):
            veitnam_yvelocity = -veitnam_yvelocity

        fifa_canvas.move(veitnam_flag,veitnam_xvelocity,veitnam_yvelocity)"""

        # Settings the coordinates of the flag for zambia
        """zambia_flag_coordinates = fifa_canvas.coords(zambia_flag)
        if ((zambia_flag_coordinates[0] >= WIDTH - zambia_flag_width) or zambia_flag_coordinates[0] < 0):
            zambia_xvelocity = -zambia_xvelocity
        elif (zambia_flag_coordinates[1] >= (HEIGHT - zambia_flag_height) or zambia_flag_coordinates[1] < 0):
            zambia_yvelocity = -zambia_yvelocity

        fifa_canvas.move(zambia_flag,zambia_xvelocity,zambia_yvelocity)"""
window.mainloop()