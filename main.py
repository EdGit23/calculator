import tkinter as tk
import tkinter.ttk as ttk
from string import punctuation

class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title('Calculator')
		self.geometry('300x400')
		self.configure(bg='gray')
		self.resizable(False,False)
		self.error_message = 'ERROR DIVISION BY ZERO'
		self.variable_check = False

		self.frame1 = tk.Frame(self)
		self.frame1.grid(row=0, column=0, pady=(0,10))

		self.frame2 = tk.Frame(self)
		self.frame2.grid(row=1, column=0, pady=(0,10))


		self.frame3 = tk.Frame(self)
		self.frame3.grid(row=2, column=0, pady=(0,10))


		self.frame4 = tk.Frame(self)
		self.frame4.grid(row=3, column=0, pady=(0,10))


		self.frame5 = tk.Frame(self)
		self.frame5.grid(row=4, column=0, pady=(0,10))


		self.frame6 = tk.Frame(self)
		self.frame6.grid(row=5, column=0, pady=(0,10))


		self.frame7 = tk.Frame(self)
		self.frame7.grid(row=6, column=0, pady=(0,10))


		self.frame8 = tk.Frame(self)
		self.frame8.grid(row=7, column=0, pady=(0,10))

		#Entry widget for the calculator
		self.display_window = tk.Text(self.frame1,bd=4,bg='#a8c64e',fg='darkgreen',font=('Verdana',12), width=25, height=3)
		self.display_window.grid(row=0, column=0,padx=20,pady=10)

		#frame2
		self.button1 = ttk.Button(self.frame2,text='sin',width=9,padding=1).grid(row=0, column=0)
		self.button2 = ttk.Button(self.frame2,text='cos',width=9,padding=1).grid(row=0, column=1)
		self.button3 = ttk.Button(self.frame2,text='tan',width=9,padding=1).grid(row=0, column=2)
		self.button4 = ttk.Button(self.frame2,text='sqrt',width=9,padding=1).grid(row=0, column=3)

		#frame3
		self.button1 = ttk.Button(self.frame3,text='x^2',width=9,padding=1).grid(row=0, column=0)
		self.button2 = ttk.Button(self.frame3,text='x^3',width=9,padding=1).grid(row=0, column=1)
		self.button3 = ttk.Button(self.frame3,text='x',width=9,padding=1).grid(row=0, column=2)
		self.button4 = ttk.Button(self.frame3,text='log',width=9,padding=1).grid(row=0, column=3)

		#frame4
		self.button1 = ttk.Button(self.frame4,text='DEL',width=9,padding=1, command=self.clear_screen).grid(row=0, column=0)
		self.button2 = ttk.Button(self.frame4,text='pi',width=9,padding=1, command=lambda:self.constants_method('pi')).grid(row=0, column=1)
		self.button3 = ttk.Button(self.frame4,text='shift',width=9,padding=1).grid(row=0, column=2)
		self.button4 = ttk.Button(self.frame4,text='%',width=9,padding=1,command=lambda:self.calculate_method('%')).grid(row=0, column=3)

		#frame5
		self.button1 = ttk.Button(self.frame5,text='7',width=7,padding=7, command=lambda:self.num_clicks('7')).grid(row=0, column=0)
		self.button2 = ttk.Button(self.frame5,text='8',width=7,padding=7, command=lambda:self.num_clicks('8')).grid(row=0, column=1)
		self.button3 = ttk.Button(self.frame5,text='9',width=7,padding=7, command=lambda:self.num_clicks('9')).grid(row=0, column=2)
		self.button4 = ttk.Button(self.frame5,text='*',width=7,padding=7, command=lambda:self.calculate_method('*')).grid(row=0, column=3)

		#frame6
		self.button1 = ttk.Button(self.frame6,text='4',width=7,padding=7, command=lambda:self.num_clicks('4')).grid(row=0, column=0)
		self.button2 = ttk.Button(self.frame6,text='5',width=7,padding=7, command=lambda:self.num_clicks('5')).grid(row=0, column=1)
		self.button3 = ttk.Button(self.frame6,text='6',width=7,padding=7, command=lambda:self.num_clicks('6')).grid(row=0, column=2)
		self.button4 = ttk.Button(self.frame6,text='/',width=7,padding=7, command=lambda:self.calculate_method('/')).grid(row=0, column=3)

		#frame7
		self.button1 = ttk.Button(self.frame7,text='1',width=7,padding=7, command=lambda:self.num_clicks('1')).grid(row=0, column=0)
		self.button2 = ttk.Button(self.frame7,text='2',width=7,padding=7, command=lambda:self.num_clicks('2')).grid(row=0, column=1)
		self.button3 = ttk.Button(self.frame7,text='3',width=7,padding=7, command=lambda:self.num_clicks('3')).grid(row=0, column=2)
		self.button4 = ttk.Button(self.frame7,text='-',width=7,padding=7, command=lambda:self.calculate_method('-')).grid(row=0, column=3)

		#frame8
		self.button1 = ttk.Button(self.frame8,text='0',width=7,padding=7, command=lambda:self.num_clicks('0')).grid(row=0, column=0)
		self.button2 = ttk.Button(self.frame8,text='.',width=7,padding=7, command=lambda:self.num_clicks('.')).grid(row=0, column=1)
		self.button3 = ttk.Button(self.frame8,text='+',width=7,padding=7, command=lambda:self.calculate_method('+')).grid(row=0, column=2)
		self.button4 = ttk.Button(self.frame8,text='=',width=7,padding=7, command=self.equals).grid(row=0, column=3)

	def num_clicks(self,num):
		#Delete any error message on the screen
		if self.variable_check:
			print('It is true')
			self.display_window.delete('1.0','end')
			self.variable_check = False # Return to false so as to append numbers to other numbers

		self.num = num
		self.display_window.insert(tk.INSERT,self.num) #Very dope line of code, just saying! doooooooppppeee

	# def delete_num(self):
	# 	self.display_window.delete(1.0)

	def clear_screen(self):
		self.display_window.delete('1.0','end')
		#self.display_window.delete('1.0')

	def constants_method(self, char_z):
		self.char_z = char_z

		if self.char_z == 'pi':
			self.display_window.delete('1.0','end')			
			self.display_window.insert(tk.INSERT,3.141592653589)


			#print(self.num1_edit) #Check to see if it works
			#print(self.char_x)
			#print(self.num1_edit)

			return

	def calculate_method(self,char_x):
		self.char_x = char_x
		self.num1 = self.display_window.get('1.0',tk.END) #Check this line and understand it! 

		#Remove whitespace and convert to int
		for i in self.num1:
			if i in punctuation or i == "\n":
				self.num1_edit = self.num1.replace(i,'')
		#print(self.num1_edit) #Check to see if it works

		self.display_window.delete('1.0','end')


		#self.display_window.insert(tk.INSERT,self.addition)

	def equals(self):

		self.num2 = self.display_window.get('1.0',tk.END) # Amazing Eurika moment

		#Remove whitespace and convert
		for i in self.num2:
			if i in punctuation or i == "\n":
				self.num2_edit = self.num2.replace(i,'')

		#print(self.num2_edit) #Check to see if it works

		#CHECK TO SEE WHAT OPERATION WAS CALLED

		#ADDITION
		if self.char_x == '+':
			self.output_result = eval(self.num1_edit) + eval(self.num2_edit)

		#SUBTRACTION
		elif self.char_x == '-':
			self.output_result = eval(self.num1_edit) - eval(self.num2_edit)

		#DIVISION
		elif self.char_x == '/':
			# Exception Handling
			if eval(self.num2_edit) == 0:
				print('Zero as the second argument')

				self.display_window.delete('1.0','end')
				self.display_window.insert(tk.INSERT,self.error_message) #Insert the error message

				# A variableto clear screen after a number has been clicked
				self.variable_check = True

				return

			self.output_result = eval(self.num1_edit) / eval(self.num2_edit)

		#MULTIPLICATION
		elif self.char_x == '*':
			self.output_result = eval(self.num1_edit) * eval(self.num2_edit)

		#MULTIPLICATION
		elif self.char_x == '%':
			self.output_result = eval(self.num1_edit) % eval(self.num2_edit)

		self.display_window.delete('1.0','end')
		self.display_window.insert(tk.INSERT,self.output_result)



if __name__ == "__main__":
	app = App()
	app.mainloop()

