from tkinter import *
window = Tk()
window.geometry("400x180")
window.title("Calculator")
window.config(bg="Black")

# Entrybox
e = Entry(window,width=61,borderwidth=5)
e.place(x=10,y=10)

# Creating Buttons

def click(num):
    result = e.get()
    e.delete(0)
    e.insert(0,str(result)+str(num))


b = Button(window,text="1",width=12,command= lambda :click(1))
b.place(x = 10, y = 60)

b = Button(window,text="2",width=12,command= lambda :click(2))
b.place(x = 105, y = 60)

b = Button(window,text="3",width=12,command= lambda :click(3))
b.place(x = 200, y = 60)

b = Button(window,text="4",width=12,command= lambda :click(4))
b.place(x = 10, y = 87)

b = Button(window,text="5",width=12,command= lambda :click(5))
b.place(x = 105, y = 87)

b = Button(window,text="6",width=12,command= lambda :click(6))
b.place(x = 200, y = 87)

b = Button(window,text="7",width=12,command= lambda :click(7))
b.place(x = 10, y = 114)

b = Button(window,text="8",width=12,command= lambda :click(8))
b.place(x = 105, y = 114)

b = Button(window,text="9",width=12,command= lambda :click(9))
b.place(x = 200, y = 114)

b = Button(window,text="0",width=12,command= lambda :click(0))
b.place(x = 105, y = 141)


# Operaters
def add():
    n1 = e.get()
    global math
    math ="addition"
    global i
    i = int(n1)
    e.delete(0,END)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0,END)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0,END)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0,END)

def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i+int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        try:
            e.insert(0, i / int(n2))
        except ZeroDivisionError:
            return 0
def clear():
    e.delete(0,END)



b = Button(window,text="Clear",width=12,command=clear)
b.place(x = 10, y = 141)

b = Button(window,text="=",width=12, command=equal)
b.place(x = 200, y = 141)

b = Button(window,text="/",width=12,command=div)
b.place(x = 295, y = 60)

b = Button(window,text="*",width=12,command=mult)
b.place(x = 295, y = 87)

b = Button(window,text="-",width=12,command=sub)
b.place(x = 295, y = 114)

b = Button(window,text="+",width=12,command=add)
b.place(x = 295, y = 141)



mainloop()