from ttkbootstrap.validation import add_regex_validation, add_numeric_validation
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.tooltip import ToolTip
import ttkbootstrap.dialogs
from tkinter import messagebox
from ttkbootstrap.constants import *
from PIL import  Image, ImageTk
from datetime import datetime
import tkinter as tk
import customtkinter
import ttkbootstrap
import openpyxl
import sqlite3
import os



#customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("green")

window = ttkbootstrap.Window(themename="cyborg")
window.geometry("500x500")
window.title('Tinazze_Foot')
window.resizable(True,True)
icon = tk.PhotoImage(file="Tinnazze.png")
window.iconphoto(False, icon)

#scan_ig =customtkinter.CTkImage(light_image=Image.open("tinazze_ig.png"),size=(200,200))


photo1 =customtkinter.CTkImage(light_image=Image.open("basketcourt.png"),size=(1500,1000))
bg_pic= customtkinter.CTkLabel(window,image=photo1,)
bg_pic.pack()
photo2 =customtkinter.CTkImage(light_image=Image.open("Instagram.PNG"),size=(20,20),)
photo3 =customtkinter.CTkImage(light_image=Image.open("FACEBOOK1.PNG"),size=(20,20))

#A toplevel window after login button is pressed
windows_open = False
def login_button():
    global windows_open
    if not windows_open:
        login= ttkbootstrap.Toplevel(str(window))
        login.geometry("500x900")
        login.title('Home Page')
        login.iconphoto(False, icon)

        open_instagram1 = False
        class Tinazze_FOOT(ttkbootstrap.Labelframe):
            def __init__(self, parent, start_position, end_position, ):
                super().__init__(master=parent, width=400, style="warning", padding=10, labelanchor="nw",
                                 text="Frame widgets", )

                # general attributes
                self.start_position = start_position + 0.01
                self.end_position = end_position - 0.01
                # self.width          = abs(start_position - end_position)

                # animation logic
                self.pos = self.start_position
                self.in_start_position = True

                # layout
                self.place(relx=self.start_position, rely=0.10, relheight=0.85)

                self.create_buttons()
                self.labels_creator()
                self.update_time()

            def labels_creator(self):

                self.main_menu_label = customtkinter.CTkLabel(self, height=28,
                                                              font=("Oswald", 30, "bold", "italic"),
                                                              compound="center", text_color="white")
                self.main_menu_label.place(relx=0.01, rely=0.1)

                self.time_label = customtkinter.CTkLabel(self, width=250, height=50, fg_color="transparent",
                                                         font=("Gothic", 40, "bold"), text_color="yellow")

                self.time_label.place(relx=0.01, rely=0.01)
                # self.update_time()

            def update_time(self):
                self.time_label.configure(text=datetime.now().strftime("%H:%M:%S"))
                self.after(1000, self.update_time)
                # self.main_menu_label.configure(text=datetime.now().month)
                # self.after(1000,self.update_time)

            def create_buttons(self):
                self.home_button = customtkinter.CTkButton(self, width=250, text="Home", height=40,command=self.instagram_page1,
                                                           font=("Gothic", 30, "bold"),
                                                           text_color='white', fg_color='green',
                                                           hover_color="red",
                                                           compound="left"
                                                           )
                self.home_button.place(relx=0.01, rely=0.2)

                self.shop_button = customtkinter.CTkButton(self, width=250, command=self.instagram_page1,
                                                           text="Shop", font=("Gothic", 30, "bold"),
                                                           height=40,
                                                           text_color='white', fg_color='red', compound="left",
                                                           hover_color="#dc5349")
                self.shop_button.place(relx=0.01, rely=0.3)

                self.manage_button = customtkinter.CTkButton(self, width=250, text="Manager",
                                                             font=("Gothic", 30, "bold"),
                                                             command=self.open_toplevel,
                                                             text_color='#080808', fg_color="orange",
                                                             hover_color="#dc5349", height=40,
                                                             )
                self.manage_button.place(relx=0.01, rely=0.4)

                # Toplevel window for main business called from sliding manager button in the label frame

            #value = ["Male", "Female", "Other"]
            def open_toplevel(self):
                top_level_window = ttkbootstrap.Toplevel()
                top_level_window.title("Business")
                top_level_window.geometry("2000x2000")
                top_level_window.iconphoto(False,icon )
                value = ["Male", "Female", "Other"]
                class Mainframe(ttkbootstrap.Labelframe):
                    def __init__(self, parent):
                        super().__init__(master=parent, style="warning", width=400, padding=10, text="Entry widgets",
                                         labelanchor='nw')

                        self.place(relx=0, rely=0.08, height=880, width=1900)

                        # Calling the defined functions
                        self.entries_creation()
                        self.entry_labels()
                        self.current_row = 0
                        self.data = []
                        self.table = self.create_table()

                    def entry_labels(self):
                        self.name_entry_label = ttkbootstrap.Label(self, compound='center', text="Customer's name",
                                                                   foreground="orange",
                                                                   font=("Gothic", 15, "bold",))
                        self.name_entry_label.place(relx=0, rely=0)

                        self.purchase_order_type = ttkbootstrap.Label(self, compound="center",
                                                                      text="Purchase description ",
                                                                      foreground='orange', font=("Gothic", 15, "bold",))
                        self.purchase_order_type.place(relx=0, rely=0.15)

                        self.buyer_gender_label = ttkbootstrap.Label(self, compound="center", text="Gender ",
                                                                     foreground='orange', font=("Gothic", 15, "bold",))
                        self.buyer_gender_label.place(relx=0, rely=0.30)

                        self.purchase_quatity = ttkbootstrap.Label(self, compound="center", foreground='orange',
                                                                   font=("Gothic", 15, "bold",),
                                                                   text="Purchase quantity")
                        self.purchase_quatity.place(relx=0.35, rely=0)

                        self.size_entry_label = ttkbootstrap.Label(self, compound="center", text="Size(s)",
                                                                   foreground='orange', font=("Gothic", 15, "bold",))
                        self.size_entry_label.place(relx=0.35, rely=0.15)

                        self.price_entry_label = ttkbootstrap.Label(self, compound="center", text="Sales price",
                                                                    foreground='orange', font=("Gothic", 15, "bold",))
                        self.price_entry_label.place(relx=0.7, rely=0)

                        self.total_entry_label = ttkbootstrap.Label(self, compound="center", text="Total",
                                                                    foreground='orange', font=("Gothic", 15, "bold",))
                        self.total_entry_label.place(relx=0.7, rely=0.185)

                    def entries_creation(self):
                        # name entry
                        self.name_entry = ttkbootstrap.Entry(self, font=("Gothic", 20), foreground='white')
                        self.name_entry.insert(0, "")
                        self.name_entry.bind("<FocusIn>", lambda n: self.name_entry.delete('0', "end"))

                        self.name_entry.place(relx=0, rely=0.05, height=50, width=420)

                        self.description_entry = ttkbootstrap.Entry(self, font=("Gothic", 20), foreground="white", )
                        self.description_entry.delete(0, "end")
                        self.description_entry.insert(0, "")
                        self.description_entry.bind("<FocusIn>", lambda d: self.description_entry.delete('0', "end"))
                        self.description_entry.place(relx=0, rely=0.2, height=50, width=420)


                        self.buyer_gender = ttkbootstrap.Combobox(self, background="#000000",
                                                                  font=("Gothic", 20, "bold"),
                                                                  foreground="green",
                                                                  values=['Male', 'Female', 'Other'], state="readonly")
                        self.buyer_gender.delete(0, "end")
                        self.buyer_gender.set(value[0])
                        self.buyer_gender.bind("<FocusIn>", lambda buy_g: self.buyer_gender.delete('0', "end"))
                        self.buyer_gender.place(relx=0, rely=0.35, height=60, width=420)

                        self.quantity_combobox = ttkbootstrap.Combobox(self, font=("Gothic", 20),
                                                                       values=['1', '2', '3', '4', '5', '6', '7', '8',
                                                                               '9', '10'],
                                                                       state="readonly")
                        self.quantity_combobox.delete(0, "end")
                        self.quantity_combobox.set(0)
                        self.quantity_combobox.bind("<FocusIn>", lambda q: self.quantity_combobox.delete('0', "end"))
                        self.quantity_combobox.place(relx=0.35, rely=0.05, height=50, width=420)

                        self.size_entry = ttkbootstrap.Entry(self, font=("Gothic", 20))
                        self.size_entry.delete(0, "end")
                        self.size_entry.insert(0, "0")
                        self.size_entry.bind("<FocusIn>", lambda a: self.size_entry.delete('0', "end"))
                        self.size_entry.place(relx=0.35, rely=0.2, height=50, width=420)

                        self.price_entry = ttkbootstrap.Entry(self, font=("Gothic", 40, 'bold'), )
                        self.price_entry.delete(0, "end")
                        self.price_entry.insert(0, "0")
                        self.price_entry.bind("<FocusIn>", lambda p: self.price_entry.delete('0', "end"))
                        self.price_entry.place(relx=0.7, rely=0.05, height=100, width=420)

                        self.total_label = ttkbootstrap.Label(self, font=("Gothic", 40, 'bold'),text="Total",
                                                              foreground="red")
                        self.total_label.place(relx=0.7, rely=0.24, height=100, width=420)

                        self.insert_button = ttkbootstrap.Button(self,style="success", text='Save datas', width=20, command=self.add_rows)
                        self.insert_button.place(relx=0.75, rely=0.38, width=420, height=50)
                        #add_numeric_validation(self.price_entry,)
                        #add_regex_validation()
                        # ToolTip a semi-transparent popup notification window when hovering the widgets for clue
                        ToolTip(self.name_entry, text="Enter buyer's name", bootstyle="primary",wraplength=500)
                        ToolTip(self.description_entry, text="Type of items bought", bootstyle="primary",wraplength=500)
                        ToolTip(self.buyer_gender, text="Male or Female buyer", bootstyle="primary",wraplength=500)
                        ToolTip(self.quantity_combobox, text="Number of items bought", bootstyle="primary",wraplength=500)
                        ToolTip(self.size_entry, text="Leg sizes", bootstyle="primary",wraplength=500)
                        ToolTip(self.price_entry, text="Amount per sales", bootstyle="primary",wraplength=500)
                        ToolTip(self.insert_button, text="Click to save data", bootstyle="success",wraplength=700)
                    def add_rows(self):
                        name        = self.name_entry.get()
                        description = self.description_entry.get()
                        gender      = self.buyer_gender.get()
                        quantity    = int(self.quantity_combobox.get())
                        size        = int(self.size_entry.get())
                        price       = float(self.price_entry.get())
                        total       = quantity * price
                        self.total_label.configure(text=f"{total}")
                        id          = self.current_row
                        #setting the current date to my table view
                        now = datetime.now()
                        date_string = now.strftime(f"%Y-%m-%d %H:%M:%S")

                        #date = ttkbootstrap.dialogs.DatePickerDialog(parent=window, title="Days", firstweekday=6)

                        # self.table.insert_rows(self,'',self)
                        self.data.append([[id], [name], [self.buyer_gender.get()],
                                          [description], [quantity],
                                          [size], [int(price)],
                                          [float(total)], [date_string]])
                        #destoy table and then create again
                        self.table.destroy()
                        self.table = self.create_table()
                        #Display output after recreating the table
                        self.price_entry.delete(0, "end")
                        self.price_entry.insert(0, "0")
                        self.name_entry.delete(0, "end")
                        self.name_entry.insert(0, "")
                        self.description_entry.delete(0, "end")
                        self.description_entry.insert(0, "")
                        self.size_entry.delete(0, "end")
                        self.size_entry.insert(0, '0')
                        self.quantity_combobox.delete(0, "end")
                        self.quantity_combobox.set(0)
                        self.buyer_gender.delete(0, "end")
                        self.buyer_gender.set(value[0])
                        self.total_entry_label.configure(text="")
                        self.current_row += 1

                        tinazze_filepath = "Tinazze_foot.xlsx"


                        #Save data to Excel
                        if not os.path.exists(tinazze_filepath):
                            workbook = openpyxl.Workbook()
                            sheet = workbook.active
                            heading = ["Name", "Gender", "Description", "Quantity", "Size", "Price", "Total",
                                       "Date"]
                            sheet.append(heading)
                            workbook.save(tinazze_filepath)

                        workbook = openpyxl.load_workbook(tinazze_filepath)
                        sheet = workbook.active
                        sheet.append([name, gender,
                                      description, quantity,
                                      size, int(price),
                                      float(total), date_string])
                        workbook.save(tinazze_filepath)


                        # Export to Sqlite database
                        # Create table
                        connection = sqlite3.connect('Tinazze_foot.db')
                        table_create_query = '''CREATE TABLE IF NOT EXISTS Tinazze_data
                                 (Name TEXT, Gender TEXT, Description TEXT, Quantity INT,
                                      Size INT, Price INT, Total Float, Date INT)
                        '''
                        connection.execute(table_create_query)

                        #Insert datas
                        data_create_query = '''INSERT INTO Tinazze_data
                                                        (Name, Gender, Description, Quantity,
                                                             Size ,Price ,Total , Date ) 
                                                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
                        data_insert_tuple = (name, gender, description , quantity,
                                                             size , price , total , date_string )
                        cursor = connection.cursor()
                        cursor.execute(data_create_query,data_insert_tuple)
                        connection.commit()
                        connection.close()
                    

                        

                        #Add a toast notification that the entered datas has been submitted
                        toast = ToastNotification(title="Succcessful",
                                                  message="Data exported to excel, database and googlesheets\nfor analysis",
                                                  bootstyle="success",
                                                  alert=True, position='nw', duration=4000)
                        toast.show_toast()



                    def create_table(self):
                        col_data = [{"text": "id", "stretch": False}, {"text": "Customer's name", "stretch": True},
                                    {"text": "Gender", "stretch": False}, {'text': "Description", "stretch": True},
                                    {"text": "Qantity", "stretch": False}, {"text": "Size", "stretch": False},
                                    {"text": "Price", "stretch": False}, {"text": "Total", "stretch": True},
                                    {"text": "Date", "stretch": True}]

                        table = Tableview(master=self, coldata=col_data, rowdata=self.data,
                                          paginated=True, searchable=True, bootstyle="info",
                                          pagesize=2000, height=10, stripecolor="green")

                        table.place(relx=0, rely=0.45, height=450, width=1870)






                        return table

                product_label = ttkbootstrap.Label(top_level_window,
                                                   text="                 Sales Master",
                                                   font=("Gothic", 40, "bold"), compound='center',
                                                   background="green")
                product_label.place(relx=0, rely=0, height=80, width=2000)


                mainframe = Mainframe(top_level_window)
                top_level_window.mainloop()
            # Another toplevel window to open instagram for gallery

            def instagram_page1(self):
                global open_instagram
                if not open_instagram:
                    ig = tk.Toplevel(window)
                    ig.geometry("500x500")
                    ig.title('Instagram_page')
                    ig.resizable(False, False)
                    p = tk.PhotoImage(file="ig_resized.png", )
                    open_instagram = True

                    scanimage = tk.Label(ig, image=p,
                                         text="Tinazze_Foot", background="black",
                                         font=("Century Gothic", 20),
                                         compound='top')
                    scanimage.pack(fill="both", expand=True)

                    ig.mainloop()

            # Animation Algorithms
            def animate(self):
                if self.in_start_position:
                    self.animate_forward()
                else:
                    self.animate_backwards()

            # Move the labeframe forward
            def animate_forward(self):
                if self.pos > self.end_position:
                    self.pos -= 0.008
                    self.place(relx=self.pos, rely=0.10)
                    self.after(5, self.animate_forward)
                else:
                    self.in_start_position = False

            # Move the label frame backwards
            def animate_backwards(self):
                if self.pos < self.start_position:
                    self.pos += 0.008
                    self.place(relx=self.pos, rely=0.10)
                    self.after(3, self.animate_backwards)
                else:
                    self.in_start_position = True

            #                                  1.0,0.6

        animated_panel = Tinazze_FOOT(login, 0.05, -0.35)

        # button to call the animated labelframe
        button_x = 0.01  # setting an initial positon to x
        frame2_button = customtkinter.CTkButton(login, text='Just do it',
                                                command=animated_panel.animate,
                                                fg_color="green",
                                                compound='right',
                                                hover_color="#02075d",
                                                font=("Gothic", 20, "bold", "italic"))
        frame2_button.place(relx=button_x, rely=0.01, anchor='nw')
        windows_open = True
open_instagram = False
class Login_frame(customtkinter.CTkFrame):
    def __init__(self, parent ):
        super().__init__(master=parent, width=400,height=400, fg_color='transparent')

        self.place(relx=0.5, rely=0.55, anchor='center')
        #Calling the wigets
        self.create_frame_widgets()


    #Wigets for class frames
    def create_frame_widgets(self):

        self.label = customtkinter.CTkLabel(self, text="Lefty Login System", font=("Roboto", 24), compound='top')
        self.label.place(x=95, y=40)

        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="Username", width=210)
        self.entry1.place(x=95, y=100)

        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Password", show="*", width=210,
                                        placeholder_text_color='green', )
        self.entry2.place(x=95, y=160)

        self.forget_label = customtkinter.CTkLabel(self, text="forgot password?", bg_color='transparent')
        self.forget_label.place(relx=0.5, rely=0.47)

        self.login_button = customtkinter.CTkButton(self, text="Login", command=login_button, width=210)
        self.login_button.place(x=95, y=220)

        self.checkbox = customtkinter.CTkCheckBox(self, text="Remember Me", )
        self.checkbox.place(relx=0.25, rely=0.63)

        self.button_Ig = customtkinter.CTkButton(self, command=self.instagram_page,
                                                 text='Instagram', image=photo2,
                                                 compound='left',
                                                 text_color="black", width=100,
                                                 fg_color='white')
        self.button_Ig.place(relx=0.25, rely=0.75)
        self.facebook_button = customtkinter.CTkButton(self,
                                                       text='Facebook', image=photo3, hover_color="cyan",
                                                       compound='left',
                                                       text_color="black", width=100,
                                                       fg_color="white")
        self.facebook_button.place(relx=0.52, rely=0.75)

    open_instagram = False
    def instagram_page(self):
        global open_instagram
        if not open_instagram:
            ig = tk.Toplevel(window)
            # customtkinter.set_appearance_mode("dark")
            ig.geometry("500x500")
            ig.title('Instagram_page')
            ig.resizable(False, False)
            p = tk.PhotoImage(file="ig_resized.png", )
            open_instagram = True

            scanimage = tk.Label(ig, image=p,
                                 text="Tinazze_Foot", background="black",
                                 font=("Century Gothic", 20),
                                 compound='top')
            scanimage.pack(fill="both", expand=True)

            ig.mainloop()

        #creating instangram and facebook
        self.button_Ig = customtkinter.CTkButton(self, command=self.instagram_page,
                                            text='Instagram', image=photo2,
                                            compound='left',
                                            text_color="black", width=100,
                                            fg_color='white')
        self.button_Ig.place(relx=0.25, rely=0.75)
        """self.facebook_button = customtkinter.CTkButton(self,
                                            text='Facebook', image=photo3, hover_color="cyan",
                                            compound='left',
                                            text_color="black", width=100,
                                            fg_color="white")
        self.facebook_button.place(relx=0.52, rely=0.75)
        self.signup_button = customtkinter.CTkButton(self,
                                                text='Sign-up',
                                                
                                                text_color="white", width=200,
                                                fg_color="green")
        self.signup_button.place(relx=0.25, rely=0.85)"""
my_frame = Login_frame(window)







window.mainloop()











"""#text = open("bal.txt", 'r').read()
#bal_image = PIL.Image.open("BAL.png")
#color_map = ImageColorGenerator(bal_image)
bal_image =Image.open("resize.png")
max_size = (400,400)
bal_image.thumbnail(max_size)
bal_image.save("pythonthumb.png")
bal_image.show()





#balimage = np.array(PIL.Image.open("pythonthumb.png"))


#print(STOPWORDS)
wc = WordCloud(stopwords=STOPWORDS,
              mask=bal_image,contour_color="black",
               contour_width=1,background_color="white",
              min_font_size=3,
              max_words=100).generate(text)
wc.recolor(color_func=color_map,)
plt.imshow(wc)
plt.axis("off")
plt.show()"""