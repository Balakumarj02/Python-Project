from tkinter import *
win = Tk()
win.title('Calculator')
win.geometry('515x365')
win.resizable(0,0)

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear imput field
def bt_clear():
    global expression
    expression = ""
    input_text.set("")

# funciton equal button

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

# Input field frame
input_frame = Frame(win, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), width=45, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0)

# increase the height of input field
input_field.pack(ipady=10)

# Button frame
btns_frame = Frame(win, width=310, height=270)
btns_frame.pack()

Clear = Button(btns_frame, text='clear', width=38, height=3, command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1,pady=1)
divide = Button(btns_frame, text='/', width=10, height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)


# Button Second row (lambda is a unanomous function without name any number of arguments)

Seven = Button(btns_frame, text='7', width=10, height=3, command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
Eight = Button(btns_frame, text='8', width=10, height=3, command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
Nine = Button(btns_frame, text='9', width=10, height=3, command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text='*', width=10, height=3, command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)

# button third row

four = Button(btns_frame, text='4', width=10, height=3, command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text='5', width=10, height=3, command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text='6', width=10, height=3, command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text='-', width=10, height=3, command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)

# button fourth row

one = Button(btns_frame, text='1', width=10, height=3, command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
tow= Button(btns_frame, text='2', width=10, height=3, command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text='3', width=10, height=3, command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text='+', width=10, height=3, command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)

# Button fifth row

zero = Button(btns_frame, text='0', width=24, height=3, command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text='.', width=10, height=3, command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
equal = Button(btns_frame, text='=', width=10, height=3, command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)


win.mainloop()