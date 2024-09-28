import IR_detect_inrange_cmplt as ir_cap
import threading
import customtkinter
from tkinter import *
import pyautogui
from tkinter.colorchooser import askcolor
import os
from PIL import Image, ImageTk, ImageGrab
from Tkinter_Calculator import calculator as sci_cal
from tkinter.messagebox import askyesnocancel
import time
from tkinter.filedialog import asksaveasfilename, askopenfilename
from plot import draw_plot


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

########################### IR camera thread created#################
        ir=ir_cap.ir_detect
        t=threading.Thread(target=ir, daemon=True)
        t.start()
#####################################################################3
        
        self.title("IntractoVision")
        self.geometry("700x450")
        # set grid layout 1x2
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

# Global variables
        self.mode = 0
        self.trace = 0 
        self.current_x = 0
        self.current_y = 0
        self.pen_size=5
        self.old_coords =(-10,-10)
        self.color = 'black'
        self.draw ='free_line'
        self.ss_width, self.ss_height=pyautogui.size()
        self.s_width, self.s_height = self.ss_width-80, self.ss_height-90

############################ load images for the app
        image_path = os.path.realpath("D:/FYP/PY_WB/IntractoVision/board_images")
        #  logo image
        self.iconpath = ImageTk.PhotoImage(file=os.path.join(image_path,"logo.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)

        self.white_board_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "white_board.png")),size=(30, 30))
        self.cal_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "calculator_2.png")), size=(30, 30))
        self.graph_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "charts.png")), size=(30, 30))
        self.eraser_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "eraser.png")), size=(33, 33))
        self.delete_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "delete.png")), size=(33, 33))
        self.palette_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "palette.png")), size=(50, 50))
        self.line_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "line.png")), size=(30, 30))
        self.free_line_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "free_line.png")), size=(30, 30))
        self.circle_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "circle.png")), size=(30, 30))
        self.triangle_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "triangle.png")), size=(30, 30))
        self.rectangle_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "rectangle.png")), size=(30, 30))
        self.dark_mode_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dark.png")), size=(50, 30))
        self.light_mode_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "light.png")), size=(50, 30))
        

######################### create menu bar
        self.menu_bar_frame = customtkinter.CTkFrame(self, border_color='blue')
        self.menu_bar_frame.grid(row=0, column=0, columnspan=2, ipadx=5, ipady=2,padx=5, pady=5 , sticky='we')
        self.menu_bar_frame.grid_columnconfigure(4,weight=2)

    #  buttons in menu bar frame
        self.white_board_button = customtkinter.CTkButton(self.menu_bar_frame, corner_radius=5,width=3, height=3, border_spacing=3, text="",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.white_board_img, command=self.white_board_button_event)
        self.white_board_button.grid(row=0, column=0, padx=(20,5), pady=5,sticky='we')
        self.calculator_button = customtkinter.CTkButton(self.menu_bar_frame, corner_radius=5,width=3, height=3, border_spacing=3, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.cal_img, command=self.calculator_button_event)
        self.calculator_button.grid(row=0, column=2, padx=5, pady=5,sticky='we')
       
        self.graph_button = customtkinter.CTkButton(self.menu_bar_frame, corner_radius=5,width=3, height=3, border_spacing=3, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.graph_img, command=self.graph_button_event)
        self.graph_button.grid(row=0, column=3, padx=5, pady=5,sticky='we')
    
    # theme change button 
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.menu_bar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event, width=20)
        self.appearance_mode_optionemenu.grid(row=0, column=6, padx=5, pady=5, )
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.menu_bar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event, width=20)
        self.scaling_optionemenu.grid(row=0, column=8, padx=5, pady=5,)

################################## create navigation frame
        
        self.tools_navigation_frame = customtkinter.CTkScrollableFrame(self, corner_radius=10,width=100,)
        self.tools_navigation_frame.grid_rowconfigure(8, weight=1)

        # save, open , screen shot buttons
        self.save_screen_button = customtkinter.CTkButton(self.tools_navigation_frame, width=40 ,text='Save-image',
                                                          command=self.save_file)
        self.save_screen_button.grid(row=0,column=0,columnspan=2,pady=4)
        self.open_image = customtkinter.CTkButton(self.tools_navigation_frame, width=40 ,text='Open-image',
                                                  command=self.open_file)
        self.open_image.grid(row=1,column=0,columnspan=2,pady=4)
        self.take_screen_shot = customtkinter.CTkButton(self.tools_navigation_frame, width=40 ,text='Take-Snap',
                                                        command=self.take_snap)
        self.take_screen_shot.grid(row=2,column=0,columnspan=2,pady=4)
        # rows for the widgets
        rows=[3,4,5,6,7,8,9,10,11]
        # colors buttons
        self.color_red = customtkinter.CTkButton(self.tools_navigation_frame,width=30,height=30, corner_radius=2,border_spacing=2,
                                                 fg_color="#FF0000", text='', hover_color='#8B0000', command=lambda: self.color_picker("red"))
        self.color_red.grid(row=rows[0], column=0, padx=1,pady=(30,5))
        self.color_green = customtkinter.CTkButton(self.tools_navigation_frame,width=30,height=30, corner_radius=2,border_spacing=2,
                                                 fg_color="#008F00", text='', hover_color='#006400', command=lambda: self.color_picker("green"))
        self.color_green.grid(row=rows[0], column=1, padx=1, pady=(30,5))
        self.color_blue = customtkinter.CTkButton(self.tools_navigation_frame,width=30,height=30, corner_radius=2,border_spacing=2,
                                                 fg_color="#0000FF", text='', hover_color='#00008B', command=lambda: self.color_picker("blue"))
        self.color_blue.grid(row=rows[1], column=0, padx=1, pady=4,)
        self.color_black = customtkinter.CTkButton(self.tools_navigation_frame,width=30,height=30, corner_radius=2,border_spacing=2,
                                                 fg_color="#102200", text='', hover_color='#000000', command=lambda: self.color_picker("black"))
        self.color_black.grid(row=rows[1], column=1, padx=1, pady=4,)

        # palette button
        self.palette_button = customtkinter.CTkButton(self.tools_navigation_frame, corner_radius=5,width=3, height=3, border_spacing=8, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.palette_img, command=self.palette_color)
        self.palette_button.grid(row=rows[2], column=0,columnspan=2,padx=5, pady=10)
        # eraser and clear all buttons
        self.eraser_button = customtkinter.CTkButton(self.tools_navigation_frame, corner_radius=5,width=3, height=3, border_spacing=4, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.eraser_img, command=lambda:self.erase_event(0))
        self.eraser_button.grid(row=rows[3], column=0, padx=1, pady=5,)
        self.delete_button = customtkinter.CTkButton(self.tools_navigation_frame, corner_radius=5,width=3, height=3, border_spacing=4, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.delete_img, command=lambda:self.erase_event(1))
        self.delete_button.grid(row=rows[3], column=1, padx=1, pady=5,)

        # shape fill button
        self.checkbox_fill = customtkinter.CTkCheckBox(self.tools_navigation_frame,checkbox_width=18,checkbox_height=18,
                                                        text="Shape-Fill",onvalue=1, offvalue=0, font=("Helvetica", 13), corner_radius=3,
                                                        width=1)
        self.checkbox_fill.grid(row=rows[4], column=0, columnspan=2,pady=(10,5))
        self.checkbox_fill.deselect()

        #  shapes frames
        self.line = customtkinter.CTkButton(self.tools_navigation_frame, corner_radius=5,width=3, height=3, border_spacing=4, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.line_img, command=self.draw_line)
        self.line.grid(row=rows[5], column=0,sticky='nswe', padx=2 )
        self.free_line = customtkinter.CTkButton(self.tools_navigation_frame, corner_radius=5,width=3, height=3, border_spacing=4, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.free_line_img, command=self.draw_free_line)
        self.free_line.grid(row=rows[5], column=1,sticky='nswe', padx=2)
        self.rectangle = customtkinter.CTkButton(self.tools_navigation_frame, corner_radius=5,width=3, height=3, border_spacing=4, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.rectangle_img, command=self.draw_rectangle)
        self.rectangle.grid(row=rows[6], column=0,sticky='nswe', padx=2)
        self.circle = customtkinter.CTkButton(self.tools_navigation_frame, corner_radius=5,width=3, height=3, border_spacing=4, text="",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.circle_img, command=self.draw_circle)
        self.circle.grid(row=rows[6], column=1,sticky='nswe', padx=2)
        
        
        # slider button
        self.size_slider = customtkinter.CTkSlider(self.tools_navigation_frame,progress_color=["#36719F", "#144870"], orientation="horizontal",
                                                   number_of_steps=100,from_ = 1 ,width=15,height=15, to=100, command=self.slider_event)
        self.size_slider.grid(row=rows[7], column=0, columnspan=2,sticky='we' ,pady=(30,0))
        self.slider_label = customtkinter.CTkLabel(self.tools_navigation_frame,font=("Helvetica",13 ), text = f"Brush-Size:{self.pen_size}%")
        self.slider_label.grid(row=rows[8],column=0, columnspan=2,)
        self.size_slider.set(self.pen_size)


#################################### create white board frame
        self.white_board_frame = customtkinter.CTkScrollableFrame(self,orientation='vertical', corner_radius=0, fg_color="transparent")
        self.white_board_frame.grid_columnconfigure(1, weight=1)
        self.canvas=Canvas(self.white_board_frame,bg="white",width=self.s_width,height=self.s_height,cursor="target", scrollregion=(0,0,self.s_width,self.s_height))
        self.canvas.grid(row=1, column=0, sticky="nswe")
# shapes to draw
        self.kinds = [self.canvas.create_oval, self.canvas.create_rectangle,
                      self.canvas.create_line,]

######################################## graph frame
        self.graph_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.graph_frame.grid_rowconfigure(1,weight=1,uniform='a')
        self.graph_frame.grid_columnconfigure(0,weight=1,uniform='a')
        draw_plot(self.graph_frame)

########################################### calculator frame
        self.calculator_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", bg_color="transparent")
        self.calculator_frame.grid_rowconfigure(0,weight=3,uniform='a')
        self.calculator_frame.grid_columnconfigure((0,1,2,3,4),weight=1, uniform='a')
        self.calculator_frame.grid_rowconfigure((1,2,3,4,5,6,7,8,9),weight=1,uniform='a')
        sci_cal(self.calculator_frame)
         
########################################## button bindings
        # self.canvas.bind("<Button-1>", self.locate_xy)
        self.canvas.bind('<ButtonPress-1>', self.onStart) 
        self.canvas.bind("<B1-Motion>", self.draw_event)
        # self.canvas.bind('<B1-Motion>',     self.onGrow)  
        self.canvas.bind('<Double-1>',      self.onClear) 
        self.canvas.bind('<ButtonPress-3>', self.onMove)  

############################################### select default frame
        self.select_frame_by_name("whiteboard")
        self.select_shape_by_name('free_line')
        self.scaling_optionemenu.set("100%")

############################ Functions for controlling Widgets ###########################################

# file handling functions
    def save_call(self):
        req = askyesnocancel(title='IntractoVision', 
                            message='Do you want to save-canvas?',)
        print(req)
        if req:
            self.save_file()
            self.canvas.delete('all')
        else:
            return req

    def take_snap(self):
        req=self.save_call()
        if req==False:
            self.minimize1()
            im = ImageGrab.grab((0, 0, self.ss_width, self.ss_height))
            self.canvas.delete('all')
            im=im.resize((self.s_width-150, self.s_height-20))
            self.img_load = ImageTk.PhotoImage(im)
            self.canvas.create_image((5,5),anchor='nw',image = self.img_load)
            self.img_exist=True

    def open_file(self):
        req=self.save_call()
        if req==False:
            f = askopenfilename(title='Open-file', initialdir = '',
                                filetypes = ((('PNG', ('*.png'))),('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),
                                            ('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))
            if f:
                img=Image.open(f)
                im=img.resize((self.s_width-150, self.s_height-20))
                self.img_load = ImageTk.PhotoImage(im)
                self.canvas.create_image((5,5),anchor='nw',image = self.img_load)
                self.img_exist=True

    def save_file(self):
        x0 = self.white_board_frame.winfo_rootx()
        y0 = self.white_board_frame.winfo_rooty()
        x1 = self.winfo_width()
        y1 = self.winfo_height()
        time.sleep(1)
        im = ImageGrab.grab((x0, y0, x1, y1))
        f = asksaveasfilename(initialdir = '',title = "Save file",defaultextension='png',
                            filetypes = ((('PNG', ('*.png'))),('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),
                                         ('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))
        if f:
            im.save(f) # Can also say im.show() to display it

#Set window minimize for screenshot
    def minimize1(self): 
        #make the window minimize 
        self.state(newstate='iconic')
        time.sleep(1)
        # for make the window maximize or open
        self.state(newstate='normal') 

# func to set initial coordinates for drawing
    def onStart(self, event):
        self.start = event
        self.drawn = None

# functions to draw somthing
    def onGrow(self, event):                         
        self.canvas = event.widget
        if self.drawn: self.canvas.delete(self.drawn)
        if self.draw == 'line':
            objectId = self.shape(self.start.x, self.start.y, event.x, event.y,
                              width = self.pen_size,fill=self.color,)
        else:
            if self.checkbox_fill.get() == True:
                objectId = self.shape(self.start.x, self.start.y, event.x, event.y,
                              width = self.pen_size,outline=self.color, fill=self.color)
            else:
                objectId = self.shape(self.start.x, self.start.y, event.x, event.y,
                              width = self.pen_size,outline=self.color,)            
        if self.trace: 
            print(objectId)
        self.drawn = objectId

# func to clear all on canvas
    def onClear(self, event):
        event.widget.delete('all') 

# func to move the shape on the canvas
    def onMove(self, event):
        if self.drawn:                               
            if self.trace:print(self.drawn)
            self.canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            self.canvas.move(self.drawn, diffX, diffY)
            self.start = event

# function to check erase all or erase selective
    def erase_event(self,c):
        if c:
            self.canvas.delete('all')
        else:
            self.select_shape_by_name('eraser')
            self.draw='eraser'
            self.color_picker("white")

# function to set the color 
    def color_picker(self,color):
        self.color = color
#  open color palette dialogue box
    def palette_color(self):
        colors = askcolor(title="Color Palette")
        self.color_picker(colors[1])

# draw line function
        
    def locate_xy(self,event):
        self.current_x = event.x
        self.current_y = event.y

# select and set the shape to draw 
    def draw_event(self,event):
        if self.draw == 'free_line' or self.draw =='eraser':
            self.canvas.create_line((self.start.x, self.start.y, event.x, event.y,), width = self.pen_size,
                                capstyle=ROUND,fill=self.color, smooth=True,)
            self.start.x, self.start.y = event.x, event.y
        elif self.draw == 'line':
            self.shape = self.kinds[2]
            self.onGrow(event)
                            
        elif self.draw == 'rectangle':
            self.shape = self.kinds[1]
            self.onGrow(event)
            
        elif self.draw == 'circle':
            self.shape = self.kinds[0]
            self.onGrow(event)
            
        elif self.draw == 'triangle':
            pass

    def draw_line(self):
        if self.color==self.canvas.cget("bg"):
            self.color='black'
        self.draw='line'
        self.select_shape_by_name('line')
    def draw_free_line(self):
        if self.color==self.canvas.cget("bg"):
            self.color='black'
        self.draw='free_line'
        self.select_shape_by_name('free_line')
    def draw_rectangle(self):
        if self.color==self.canvas.cget("bg"):
            self.color='black'
        self.draw='rectangle'
        self.select_shape_by_name('rectangle')
    def draw_triangle(self):
        if self.color==self.canvas.cget("bg"):
            self.color='black'
        self.draw='triangle'
        self.select_shape_by_name('triangle')
    def draw_circle(self):
        if self.color==self.canvas.cget("bg"):
            self.color='black'
        self.draw='circle'
        self.select_shape_by_name('circle')
    
# focus the selcted widget 
    def select_shape_by_name(self, name):
        # set button color for selected button
        self.line.configure(fg_color=("gray75", "gray25") if name == "line" else "transparent")
        self.free_line.configure(fg_color=("gray75", "gray25") if name == "free_line" else "transparent")
        self.rectangle.configure(fg_color=("gray75", "gray25") if name == "rectangle" else "transparent")
        # self.triangle.configure(fg_color=("gray75", "gray25") if name == "triangle" else "transparent")
        self.circle.configure(fg_color=("gray75", "gray25") if name == "circle" else "transparent")
        self.eraser_button.configure(fg_color=("gray75", "gray25") if name == "eraser" else "transparent")

# frame selection function
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.white_board_button.configure(fg_color=("gray75", "gray25") if name == "whiteboard" else "transparent")
        # self.transperant_board_button.configure(fg_color=("gray75", "gray25") if name == "transperant" else "transparent")
        self.graph_button.configure(fg_color=("gray75", "gray25") if name == "graph" else "transparent")
        self.calculator_button.configure(fg_color=("gray75", "gray25") if name == "calculator" else "transparent")

        # show selected frame
        if name == "whiteboard":
            self.white_board_frame.grid(row=1, column=1, sticky="nsew")
            self.tools_navigation_frame.grid(row=1, column=0, sticky="ns",pady=10)

        else:
            self.white_board_frame.grid_forget()
            self.tools_navigation_frame.grid_forget()
        # if name == "transperant":
        #     self.transperant_board_frame.grid(row=1, column=1, sticky="nsew")
        # else:
        #     self.transperant_board_frame.grid_forget()
        if name == "calculator":
            self.calculator_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.calculator_frame.grid_forget()

        if name == "graph":
            self.graph_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.graph_frame.grid_forget()

    def white_board_button_event(self):
        self.select_frame_by_name("whiteboard")

    # def transperant_board_button_event(self):
    #     self.select_frame_by_name("transperant")

    def calculator_button_event(self):
        self.select_frame_by_name("calculator")

    def graph_button_event(self):
        self.select_frame_by_name("graph")


# scale the window and all widgets
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
#  change the theme
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
# change the pen brush size
    def slider_event(self,value):
        v=int(value)
        self.pen_size=v
        self.slider_label.configure(text=f"Brush-Size: {v}%")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()