import math
from tkinter import *

#Creating the scientific calculator widget
calculator = Tk()
calculator.title("Scientific Calculator")
calculator.geometry("330x425+500+150")
calculator.resizable(0,0)

#Declaring two global variables for proper functionality of codes
value = "0"                 #Global Variable for display. Setting default display to 0.
operation = ""              #Global Variable for performing calculation

#Function taking input from buttons in calculator
def button_input(symbol, sym_calc):
    global value
    global operation
    if value == "0":            #Ensuring default display is 0
        operation = ""          #Ensuring calculation variable is empty
        value = ""              #Emptying display value variable
    value += symbol             #Storing button name as what will be displayed onto screen
    operation += str(sym_calc)  #Converting what is displayed into proper string function for calculation afterwards
    input_text.set(value)       #Displaying onto screen

#Creating function that will become the command for delete button
def delete():
    global value
    global operation
    value = ""              #Clearing the value variable
    operation = ""          #Clearing the calculation variable
    input_text.set("0")     #Setting the default display back to 0

#Creating function that will become the command for equal button
def equal():
    global value
    global operation
    try:
        answer = str(eval(operation)) #Evaluating mathematically stored information from calculation variable and storing it as a string
                                                                                                                    # in the answer variable
        input_text.set(answer)                   #Displaying the answer obtained onto calculator screen
        value = ""                               #Emptying value variable for next operations
        operation = ""                           #Emptying calculation variable for next operations
    except ZeroDivisionError:                    #Ensuring that user sees error in case of division by 0
        input_text.set("ERROR. [DEL]:Cancel")    #Displaying error and prompting user to press DEL button to go back to calculator


input_text = StringVar()    #Creating input_text variable which will ensure what is displayed onto screen
input_text.set("0")         #Setting default display as 0

#Creating a frame for better presentation of screen in GUI
calc = Frame(calculator)
calc.grid()
#Creating the display screen of the calculator and making the numbers to be displayed justified to the right
screen = Entry(calc, font=('Serif', 20), textvariable = input_text, bg="light grey", bd=15, width=19, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=4, padx=7, pady=5)

#Creating a list of the buttons' names and the signs shown on the button
signs = ["√(", "ln(", "log(", "sin(",
         "cos(", "tan(", "π","Abs(",
         "(",")",  ".", "*",
         "/", "+", "-", "^2"]
#Creating a list of the command for the button's name and sign respectively
sign_function = ["math.sqrt(", "math.log(", "math.log10(", "math.sin(",
                 "math.cos(", "math.tan(", "math.pi", "abs(",
                 "(",")",  ".", "*",
                 "/", "+", "-", "**2"]

#Using a for loop to create the button in the row of range 1-5 and column 0-4
#Using the lambda function inside the command function to assign the functionality of the buttons
i = 0
for row in range(1,5):
    for column in range(0,4):
        Button(calc, text=signs[i], width=8, height=2, font=('Serif', 10), bd=4, bg="SkyBlue4", command=lambda symbol=signs[i], sym_calc=sign_function[i]: button_input(symbol, sym_calc)).grid(row=row, column=column, padx=1, pady=1)
        i += 1

#Creating a string variable for the numbers of the number pad and appending them in a list
#Using a for loop to display the button and a lambda function to assign the command function of each button
number = "123456789"
x = 0
buttons = []
for i in range(5, 8):
    for j in range(3):
        buttons.append(Button(calc, width=8, height=2, font=('Serif', 10), bd=4, bg="LightSteelBlue3", text=number[x], command=lambda symbol=number[x], sym_calc=number[x]: button_input(symbol, sym_calc)))
        buttons[x].grid(row=i, column=j, pady=1)

        x += 1
#Creating the remaining buttons of the calculator assigning each button to their respective function
zero_button = Button(calc, text='0', width=8, height=5, font=('Serif', 10), bd=4, bg="LightSteelBlue3", command=lambda symbol="0", sym_calc="0": button_input(symbol, sym_calc)).grid(row=6, column=3, rowspan=2, padx=1, pady=1)
delete_button = Button(calc, text='DEL', width=8, height=2, font=('Serif', 10), bd=4, bg="brown2", command= lambda:delete()).grid(row=4, column=3, padx=1, pady=1)
equal_button = Button(calc, text='=', width=8, height=2, font=('Serif', 10), bd=4, bg="SkyBlue4", command= lambda:equal()).grid(row=5, column=3, padx=1, pady=1)

#Calling the tkinter mainloop() function to ensure everything runs smoothly
mainloop()
