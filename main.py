from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Basic Calculator")

def button_click(number):
	current_value = entry_widget.get()
	entry_widget.delete(0,END)

	entry_widget.insert(0,str(current_value) + str(number))

def calculate_method(character):
	global character_value
	global number1, number2

	number1 = eval(entry_widget.get())

	entry_widget.delete(0,END)
	
	character_value = character


def equals_method():
	number2 = eval(entry_widget.get())

	entry_widget.delete(0,END)

	if character_value == '+':
		total = number1 + number2
		entry_widget.insert(0,str(total))

	elif character_value == '-':
		total = number1 - number2
		entry_widget.insert(0,str(total))

	elif character_value == '*':
		total = number1 * number2
		entry_widget.insert(0,str(total))

	elif character_value == '/':
		total = number1 / number2
		entry_widget.insert(0,str(total))

def clear_method():
	entry_widget.delete(0,END)

frame0 = ttk.Frame(root,padding=10)
frame1 = ttk.Frame(root,padding=1)
frame2 = ttk.Frame(root,padding=1)
frame3 = ttk.Frame(root,padding=1)
frame4 = ttk.Frame(root,padding=1)
frame5 = ttk.Frame(root,padding=1)
frame6 = ttk.Frame(root,padding=1)


frame0.grid()
frame1.grid()
frame2.grid()
frame3.grid()
frame4.grid()
frame5.grid()
frame6.grid()


entry_widget = ttk.Entry(frame0, width=30)
entry_widget.grid()

ttk.Button(frame1, text=str(1),padding=12,width=5,command=lambda:button_click(1)).grid(row=0, column=0)
ttk.Button(frame1, text=str(2),padding=12,width=5,command=lambda:button_click(2)).grid(row=0, column=1)
ttk.Button(frame1, text=str(3),padding=12,width=5,command=lambda:button_click(3)).grid(row=0, column=2)
ttk.Button(frame2, text=str(4),padding=12,width=5,command=lambda:button_click(4)).grid(row=1, column=0)
ttk.Button(frame2, text=str(5),padding=12,width=5,command=lambda:button_click(5)).grid(row=1, column=1)
ttk.Button(frame2, text=str(6),padding=12,width=5,command=lambda:button_click(6)).grid(row=1, column=2)
ttk.Button(frame3, text=str(7),padding=12,width=5,command=lambda:button_click(7)).grid(row=2, column=0)
ttk.Button(frame3, text=str(8),padding=12,width=5,command=lambda:button_click(8)).grid(row=2, column=1)
ttk.Button(frame3, text=str(9),padding=12,width=5,command=lambda:button_click(9)).grid(row=2, column=2)
ttk.Button(frame4, text="+",padding=12,width=5, command=lambda:calculate_method('+')).grid(row=0,column=0)
ttk.Button(frame4, text=str(0),padding=12,width=5,command=lambda:button_click(0)).grid(row=0, column=1)
ttk.Button(frame4, text="/",padding=12,width=5, command=lambda:calculate_method('/')).grid(row=0,column=2)
ttk.Button(frame5, text="CLR",padding=12,width=5, command=clear_method).grid(row=0,column=0)
ttk.Button(frame5, text="-",padding=12,width=5,command=lambda:calculate_method('-')).grid(row=0,column=1)
ttk.Button(frame5, text="*",padding=12,width=5,command=lambda:calculate_method('*')).grid(row=0,column=2)
ttk.Button(frame6, text="=", command=equals_method, width =15, padding=12).grid(row=0,column=0)
ttk.Button(frame6, text=".", command=lambda:button_click('.'), width =5, padding=12).grid(row=0,column=1)



root.mainloop()
