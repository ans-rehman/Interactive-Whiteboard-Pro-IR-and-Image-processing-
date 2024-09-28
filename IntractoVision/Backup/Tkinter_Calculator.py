# Import packages
from tkinter import *
import math
import numpy as np
# from wi_prt import App

# Variables
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'

class calculator():
    def __init__(self,f):
        # super().__init__()
        # self.configure(bg="#293C4A", bd=10)
        # self.title("Scientific Calculator")

        self.calc_operator = ""
        self.text_input = StringVar()

        text_display = Entry(f, font=('sans-serif', 20, 'bold'), textvariable=self.text_input,
                            bd=5, insertwidth = 10, bg='#BBB', justify='right').grid(row=0,columnspan=5, padx = 10, pady = 15, sticky='nswe')

        button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
        button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

        '''
        Buttons
        '''
        #--1st row--
        # Absolute value of a number
        abs_value = Button(f, button_params, text='abs',
                        command=lambda:self.button_click('abs(')).grid(row=1, column=0, sticky="nsew")
        # Remainder of a division
        modulo = Button(f, button_params, text='mod',
                        command=lambda:self.button_click('%')).grid(row=1, column=1, sticky="nsew")
        # Integer division quotient
        int_div = Button(f, button_params, text='div',
                        command=lambda:self.button_click('//')).grid(row=1, column=2, sticky="nsew")
        # self.Factorial of a number
        factorial_button = Button(f, button_params, text='x!',
                        command=self.fact_func).grid(row=1, column=3, sticky="nsew")
        # Euler's number e
        eulers_num = Button(f, button_params, text='e',
                            command=lambda:self.button_click(str(math.exp(1)))).grid(row=1, column=4, sticky="nsew")

        #--2nd row--
        # self.Sine of an angle in degrees
        sine = Button(f, button_params, text='sin',
                    command=self.trig_sin).grid(row=2, column=0, sticky="nsew")
        # self.Coself.sine of an angle in degrees
        cos = Button(f, button_params, text='cos',
                    command=self.trig_cos).grid(row=2, column=1, sticky="nsew")
        # self.Tangent of an angle in degrees
        tangent = Button(f, button_params, text='tan',
                    command=self.trig_tan).grid(row=2, column=2, sticky="nsew")
        # self.Coself.tangent of an angle in degrees
        trig_cot = Button(f, button_params, text='cot',
                    command=self.trig_cot).grid(row=2, column=3, sticky="nsew")
        # Pi(3.14...) number 
        pi_num = Button(f, button_params, text='π',
                        command=lambda:self.button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew")

        #--3rd row--
        # Power of 2
        second_power = Button(f, button_params, text='x\u00B2',
                    command=lambda:self.button_click('**2')).grid(row=3, column=0, sticky="nsew")
        # Power of 3
        third_power = Button(f, button_params, text='x\u00B3',
                    command=lambda:self.button_click('**3')).grid(row=3, column=1, sticky="nsew")
        # Power of n
        nth_power = Button(f, button_params, text='x^n',
                    command=lambda:self.button_click('**')).grid(row=3, column=2, sticky="nsew")
        # Inverse number
        inv_power = Button(f, button_params, text='x\u207b\xb9',
                    command=lambda:self.button_click('**(-1)')).grid(row=3, column=3, sticky="nsew")
        # Powers of 10
        tens_powers = Button(f, button_params, text='10^x', font=('sans-serif', 15, 'bold'),
                            command=lambda:self.button_click('10**')).grid(row=3, column=4, sticky="nsew")

        #--4th row--
        # Square root of a number
        square_root = Button(f, button_params, text='\u00B2\u221A',
                            command=self.square_root).grid(row=4, column=0, sticky="nsew")
        # Third root of a number
        third_root = Button(f, button_params, text='\u00B3\u221A',
                            command=self.third_root).grid(row=4, column=1, sticky="nsew")
        # nth root of a number
        nth_root = Button(f, button_params, text='\u221A',
                        command=lambda:self.button_click('**(1/')).grid(row=4, column=2, sticky="nsew")
        # Logarithm of a number with base 10
        log_base10 = Button(f, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),
                        command=lambda:self.button_click('log(')).grid(row=4, column=3, sticky="nsew")
        # Logarithm of a number with base e (ln)
        log_basee = Button(f, button_params, text='ln',
                        command=lambda:self.button_click('ln(')).grid(row=4, column=4, sticky="nsew")

        #--5th row--
        # Add a left parentheses
        left_par = Button(f, button_params, text='(',
                        command=lambda:self.button_click('(')).grid(row=5, column=0, sticky="nsew")
        # Add a right parentheses
        right_par = Button(f, button_params, text=')',
                        command=lambda:self.button_click(')')).grid(row=5, column=1, sticky="nsew")   
        # Change the sign of a number
        signs = Button(f, button_params, text='\u00B1',
                    command=self.sign_change).grid(row=5, column=2, sticky="nsew")
        # Transform number to percentage
        percentage = Button(f, button_params, text='%',
                    command=self.percent).grid(row=5, column=3, sticky="nsew")
        # Calculate the function e^x
        ex = Button(f, button_params, text='e^x',
                    command=lambda:self.button_click('e(')).grid(row=5, column=4, sticky="nsew")

        #--6th row--
        button_7 = Button(f, button_params_main, text='7',
                        command=lambda:self.button_click('7')).grid(row=6, column=0, sticky="nsew")
        button_8 = Button(f, button_params_main, text='8',
                        command=lambda:self.button_click('8')).grid(row=6, column=1, sticky="nsew")
        button_9 = Button(f, button_params_main, text='9',
                        command=lambda:self.button_click('9')).grid(row=6, column=2, sticky="nsew")
        delete_one = Button(f, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
                    text='DEL', command=self.button_delete, bg='#db701f').grid(row=6, column=3, sticky="nsew")
        delete_all = Button(f, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
                    text='AC', command=self.button_clear_all, bg='#db701f').grid(row=6, column=4, sticky="nsew")

        #--7th row--
        button_4 = Button(f, button_params_main, text='4',
                        command=lambda:self.button_click('4')).grid(row=7, column=0, sticky="nsew")
        button_5 = Button(f, button_params_main, text='5',
                        command=lambda:self.button_click('5')).grid(row=7, column=1, sticky="nsew")
        button_6 = Button(f, button_params_main, text='6',
                        command=lambda:self.button_click('6')).grid(row=7, column=2, sticky="nsew")
        mul = Button(f, button_params_main, text='*',
                    command=lambda:self.button_click('*')).grid(row=7, column=3, sticky="nsew")
        div = Button(f, button_params_main, text='/',
                    command=lambda:self.button_click('/')).grid(row=7, column=4, sticky="nsew")

        #--8th row--
        button_1 = Button(f, button_params_main, text='1',
                        command=lambda:self.button_click('1')).grid(row=8, column=0, sticky="nsew")
        button_2 = Button(f, button_params_main, text='2',
                        command=lambda:self.button_click('2')).grid(row=8, column=1, sticky="nsew")
        button_3 = Button(f, button_params_main, text='3',
                        command=lambda:self.button_click('3')).grid(row=8, column=2, sticky="nsew")
        add = Button(f, button_params_main, text='+',
                    command=lambda:self.button_click('+')).grid(row=8, column=3, sticky="nsew")
        sub = Button(f, button_params_main, text='-',
                    command=lambda:self.button_click('-')).grid(row=8, column=4, sticky="nsew")

        #--9th row--
        button_0 = Button(f, button_params_main, text='0',
                        command=lambda:self.button_click('0')).grid(row=9, column=0, sticky="nsew")
        point = Button(f, button_params_main, text='.',
                    command=lambda:self.button_click('.')).grid(row=9, column=1, sticky="nsew")
        exp = Button(f, button_params_main, text='EXP', font=('sans-serif', 16, 'bold'),
                    command=lambda:self.button_click(E)).grid(row=9, column=2, sticky="nsew")
        equal = Button(f, button_params_main, text='=',
                    command=self.button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")


    '''
    Functions
    '''
    # Function to add in the entry of text display
    def button_click(self,char):
        self.calc_operator += str(char)
        self.text_input.set(self.calc_operator)

    # Function to clear the whole entry of text display
    def button_clear_all(self):
        self.calc_operator = ""
        self.text_input.set("")

    # Function to delete one by one from the last in the entry of text display
    def button_delete(self):
        text = self.calc_operator[:-1]
        self.calc_operator = text
        self.text_input.set(text)

    # Function to calculate the self.factorial of a number
    def factorial(self,n):
        if n==0 or n==1:
            return 1
        else:
            return n*self.factorial(n-1)

    def fact_func(self,):
        result = str(self.factorial(int(self.calc_operator)))
        self.calc_operator = result
        self.text_input.set(result)

    # Function to calculate trigonometric numbers of an angle
    def trig_sin(self,):
        result = str(math.sin(math.radians(int(self.calc_operator))))
        self.calc_operator = result
        self.text_input.set(result)

    def trig_cos(self):
        result = str(math.cos(math.radians(int(self.calc_operator))))
        self.calc_operator = result
        self.text_input.set(result)

    def trig_tan(self):
        result = str(math.tan(math.radians(int(self.calc_operator))))
        self.calc_operator = result
        self.text_input.set(result)

    def trig_cot(self):
        result = str(1/math.tan(math.radians(int(self.calc_operator))))
        self.calc_operator = result
        self.text_input.set(result)

    # Function to find the square root of a number
    def square_root(self):
        if int(self.calc_operator)>=0:
            temp = str(eval(self.calc_operator+'**(1/2)'))
            self.calc_operator = temp
        else:
            temp = "ERROR"
        self.text_input.set(temp)

    # Function to find the third root of a number
    def third_root(self):
        if int(self.calc_operator)>=0:
            temp = str(eval(self.calc_operator+'**(1/3)'))
            self.calc_operator = temp
        else:
            temp = "ERROR"
        self.text_input.set(temp)

    # Function to change the sign of number
    def sign_change(self):
        if self.calc_operator[0]=='-':
            temp = self.calc_operator[1:]
        else:
            temp = '-'+self.calc_operator
        self.calc_operator = temp
        self.text_input.set(temp)    

    # Function to calculate the percentage of a number
    def percent(self):
        temp = str(eval(self.calc_operator +'/100'))
        self.calc_operator = temp
        self.text_input.set(temp)

    # Funtion to find the result of an operation
    def button_equal(self):
        print(self.calc_operator)
        temp_op = str(eval(self.calc_operator))
        self.text_input.set(temp_op)
        self.calc_operator = temp_op

if __name__ == "__main__":
    app = calculator()
    app.mainloop()
