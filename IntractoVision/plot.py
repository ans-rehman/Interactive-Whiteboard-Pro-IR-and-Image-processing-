import numpy as np
from tkinter import *
import tkinter
import customtkinter
import matplotlib.pyplot as plt



sin=np.sin
cos=np.cos
tan=np.tan
cot='1/tan'
pi=np.pi
exp=np.exp
sin_inv=np.arcsin
cos_inv=np.arccos
tan_inv=np.arctan
log, ln = np.log10, np.log

class draw_plot():
    def __init__(self,f):

# X axis param set

        self.xy_axis_param_frame = customtkinter.CTkFrame(f) 
        self.xy_axis_param_frame.grid(row=1,column=0, sticky='ns',ipadx=30,pady=20)
        # self.xy_axis_param_frame.grid_rowconfigure(1,weight=1,uniform='a')
        # self.xy_axis_param_frame.grid_columnconfigure(0,weight=1,uniform='a')

        x_axis_label = customtkinter.CTkLabel(self.xy_axis_param_frame, text="Set X-Axis", font=('Helvatica',20),
                                              fg_color=["#36719F", "#144870"], corner_radius=10)
        x_axis_label.grid(row=0, column=0, columnspan=6, sticky='we', padx=20, pady=20)
        # self.xy_axis_param_frame.grid_rowconfigure(1,weight=1)
        
        self.radio_var_x = tkinter.IntVar(value=0)
        self.x_axis_range = customtkinter.CTkRadioButton(self.xy_axis_param_frame,text="Range", variable=self.radio_var_x, value=0,
                                                         border_width_checked=8, command=lambda:self.x_axis_call(0))
        self.x_axis_range.grid(row=1, column=0,columnspan=3,pady=10,sticky='we')
        self.x_axis_custom = customtkinter.CTkRadioButton(self.xy_axis_param_frame,text="Custom values", variable=self.radio_var_x, value=1,
                                                          border_width_checked=8, command=lambda:self.x_axis_call(1))
        self.x_axis_custom.grid(row=1, column=3,columnspan=3,sticky='we')

        # self.xy_axis_param_frame = customtkinter.CTkFrame(self.xy_axis_param_frame)
        # self.xy_axis_param_frame.grid(row=1,column=0)
        self.start_label = customtkinter.CTkLabel(self.xy_axis_param_frame, text='Start:',anchor='e')
        self.start_label.grid(row=2, column=0,padx=5,pady=10, sticky='we' )
        self.start_entry = customtkinter.CTkEntry(self.xy_axis_param_frame, )
        self.start_entry.grid(row=2, column=1,sticky='we')

        self.steps_label = customtkinter.CTkLabel(self.xy_axis_param_frame, text='Step-size:',anchor='e')
        self.steps_label.grid(row=2, column=2,padx=5 , sticky='we')
        self.steps_entry = customtkinter.CTkEntry(self.xy_axis_param_frame, )
        self.steps_entry.grid(row=2, column=3,sticky='we')

        self.end_label = customtkinter.CTkLabel(self.xy_axis_param_frame, text='End:',anchor='e')
        self.end_label.grid(row=2, column=4,padx=5, sticky='we' )
        self.end_entry = customtkinter.CTkEntry(self.xy_axis_param_frame, )
        self.end_entry.grid(row=2, column=5,sticky='we')

        self.custom_value_label_x = customtkinter.CTkLabel(self.xy_axis_param_frame, text='Custom values (val1,val2,...):',
                                                           anchor='e')
        self.custom_value_label_x.grid(row=3, column=0,columnspan=2,padx=5 , pady=(20,10), sticky='we')
        self.custom_value_entry_x = customtkinter.CTkEntry(self.xy_axis_param_frame)
        self.custom_value_entry_x.grid(row=3, column=2,columnspan=4,sticky='we',padx=5)

        y_axis_label = customtkinter.CTkLabel(self.xy_axis_param_frame, text="Set Y-Axis", font=('Helvatica',20),
                                              fg_color=["#36719F", "#144870"], corner_radius=10)
        y_axis_label.grid(row=4, column=0, columnspan=6,padx=10,pady=10, sticky='we')

        self.radio_var_y = tkinter.IntVar(value=0)
        self.function = customtkinter.CTkRadioButton(self.xy_axis_param_frame,text="Function", variable=self.radio_var_y, value=0,
                                                         border_width_checked=8, command=lambda:self.y_axis_call(0))
        self.function.grid(row=5, column=0, columnspan=3,pady=10,sticky='we')
        self.y_axis_custom = customtkinter.CTkRadioButton(self.xy_axis_param_frame,text="Custom values", variable=self.radio_var_y, value=1,
                                                          border_width_checked=8, command=lambda:self.y_axis_call(1))
        self.y_axis_custom.grid(row=5, column=3, columnspan=3,sticky='we')

        self.custom_value_label_y = customtkinter.CTkLabel(self.xy_axis_param_frame, text='Custom values (val1,val2,...):',
                                                           anchor='e')
        self.custom_value_label_y.grid(row=6, column=0,columnspan=2,padx=5 , pady=(20,10), sticky='we')
        self.custom_value_entry_y = customtkinter.CTkEntry(self.xy_axis_param_frame, )
        self.custom_value_entry_y.grid(row=6, column=2, columnspan=4, sticky='we',padx=5)

        self.function_label = customtkinter.CTkLabel(self.xy_axis_param_frame, text='Function:', anchor='e')
        self.function_label.grid(row=7, column=0,padx=5 , columnspan=2, sticky='we')
        self.function_entry = customtkinter.CTkEntry(self.xy_axis_param_frame, )
        self.function_entry.grid(row=7, column=2, columnspan=4,sticky='we',padx=5)


#  plt button
        self.plot_graph_button = customtkinter.CTkButton(f,text='Plot', command=self.value_check)
        self.plot_graph_button.grid(row=3,column=0, padx=20,pady=10,)

        self.custom_value_entry_x.configure(state="disabled")
        self.custom_value_entry_y.configure(state="disabled")

        self.plot_check_x_2 , self.plot_check_y_2 = None, None
        self.plot_check_x_1 , self.plot_check_y_1 = None, None

# key buttons
        # self.keypad_frame = customtkinter.CTkFrame(f) 
        # self.keypad_frame.grid(row=1,column=0, sticky='ns',ipadx=30,pady=20)


    def value_check(self):
# X axis value check
        if self.start_entry.cget('state')=='normal':
            # print('range', self.start_entry.cget('state'))
            start_val = self.start_entry.get()
            step_val = self.steps_entry.get()
            stop_val = self.end_entry.get()
            # print(start_val,step_val, stop_val)
            try:
                self.start_val = float(start_val)
                self.step_val = float(step_val)
                self.stop_val = float(stop_val)
                self.plot_check_x_1 = True
            except ValueError:
                self.plot_check_x_1 = False
                print("value type error")
        else:
            print('custom')
            self.v_x=[]
            s_x = self.custom_value_entry_x.get()
            s_x = s_x.split(',')
            for i in s_x:
                try:
                    self.v_x.append(float(i))
                    self.plot_check_x_2 = True
                    # print(self.v_x)
                except ValueError:
                    print('error array')
                    self.plot_check_x_2 = False
                    break
# y axis value check
        if self.function_entry.cget('state') == 'normal':
            self.func_val = self.function_entry.get()
            self.plot_check_y_1=True
        else:
            self.v_y = []
            s_y = self.custom_value_entry_y.get()
            s_y = s_y.split(',')
            for i in s_y:
                try:
                    self.v_y.append(float(i))
                    # print(self.v_y)
                    self.plot_check_y_2 = True
                except ValueError:
                    self.plot_check_y_2 = False
                    print('error array')
                    break
        self.plot()

    def plot(self):
        if self.plot_check_x_2 and self.plot_check_y_2:
            plt.plot(self.v_x,self.v_y)
            plt.show()
        elif self.plot_check_x_1 and self.plot_check_y_1:
            x = np.arange(self.start_val,self.stop_val,self.step_val)
            y = eval(self.func_val)
            # print(x, self.start_entry)
            # print(y,self.func_val)
            plt.plot(x,y)
            plt.show()

    def x_axis_call(self,event):
        if event:
            self.start_entry.delete(0,END)
            self.steps_entry.delete(0,END)
            self.end_entry.delete(0,END)

            self.start_entry.configure(state="disabled")
            self.end_entry.configure(state="disabled")
            self.steps_entry.configure(state="disabled")
            self.custom_value_entry_x.configure(state='normal')
        else:
            self.custom_value_entry_x.delete(0,END)
            self.start_entry.configure(state="normal")
            self.end_entry.configure(state="normal")
            self.steps_entry.configure(state="normal")
            self.custom_value_entry_x.configure(state="disabled")

    def y_axis_call(self,event):
        if event:
            self.function_entry.delete(0,END)
            self.custom_value_entry_y.configure(state="normal")
            self.function_entry.configure(state="disabled")
        else:
            self.custom_value_entry_y.delete(0,END)
            self.function_entry.configure(state="normal")
            self.custom_value_entry_y.configure(state="disabled")