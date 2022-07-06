###############################################
#                Programming Fever   		  #
# This script is given by Mahin Bin hasan     #
#https://www.facebook.com/root.mahin          #
#https://www.youtube.com/AlMahin              #
###############################################

from tkinter import *

root = Tk()
root.title('Meaw Calculator')
root.geometry('345x460')
root.resizable(False,False)
inp = " "
strr = " "
num1 = 0
num2 = 0
op =" "
def click(i):
    global inp
    global strr
    global num1
    global num2
    if strr ==" ":
        inp = inp+i
        out.config(text=inp)
    else:
        inp = inp + i
        num2 = float(inp)
        strr = strr+i
        out.config(text = strr)
def calc():
    global op
    global num1
    global num2
    global strr
    global inp
    if op =="x":
        res = num1*num2
    if op =="+":
        res = num1+num2
    if op == "-":
            res = num1 - num2
    num1 = res
    strr = str(res)
    inp= strr
    out.config(text = res)

def oper(opp):
    global inp
    global num1
    global num2
    global strr
    global op
    op = opp
    num1 = float(inp)
    strr = inp+op
    inp = " "
    out.config(text=strr)
    pass
Display = Frame(root,bg = 'black',width=400,height=100)
Display.pack(fill=BOTH)
out = Label(Display,bg = 'black',width=40,text = '',fg = "green",font=('','38'))
out.pack()

keypad = Frame(root,width=390,height=490,bg="hotpink",borderwidth=5)
keypad.pack(fill=BOTH)
Buttons = Frame(keypad,width=390,height=490,bg="hotpink",borderwidth=5)
Buttons.grid(row=0,column=0)
b7 = Button(Buttons,text='7',width=10,height=5,command= lambda: click('7'))
b7.grid(row=0,column=0)
b8 = Button(Buttons,text='8',width=10,height=5,command= lambda: click('8'))
b8.grid(row=0,column=1)
b9 = Button(Buttons,text='9',width=10,height=5,command= lambda: click('9'))
b9.grid(row=0,column=2)

b4 = Button(Buttons,text='4',width=10,height=5,command= lambda: click('4'))
b4.grid(row=1,column=0)
b5 = Button(Buttons,text='5',width=10,height=5,command= lambda: click('5'))
b5.grid(row=1,column=1)
b6 = Button(Buttons,text='6',width=10,height=5,command= lambda: click('6'))
b6.grid(row=1,column=2)

b1 = Button(Buttons,text='1',width=10,height=5,command= lambda: click('1'))
b1.grid(row=2,column=0)
b2 = Button(Buttons,text='2',width=10,height=5,command= lambda: click('2'))
b2.grid(row=2,column=1)
b3 = Button(Buttons,text='3',width=10,height=5,command= lambda: click('3'))
b3.grid(row=2,column=2)
b00 = Button(Buttons,text='00',width=10,height=5,command= lambda: click('00'))
b00.grid(row=3,column=0)
b0 = Button(Buttons,text='0',width=10,height=5,command= lambda: click('0'))
b0.grid(row=3,column=1)
bdt = Button(Buttons,text='.',width=10,height=5,command= lambda: click('.'))
bdt.grid(row=3,column=2)


op = Frame(keypad)
op.grid(row=0,column=1)
mul = Button(op,text='X',width=10,height=5,command= lambda: oper('x'))
mul.grid(row=0,column=0)
minus = Button(op,text='-',width=10,height=5,command= lambda: oper('-'))
minus.grid(row=1,column=0)
pl = Button(op,text='+',width=10,height=5,command= lambda: oper('+'))
pl.grid(row=2,column=0)
eql = Button(op,text='=',width=10,height=5,command= lambda: calc())
eql.grid(row=3,column=0)
root.mainloop()