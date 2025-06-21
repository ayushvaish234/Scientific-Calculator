import tkinter
import math

expression = "" 

def press(num): 
	global expression 

	expression = expression + str(num) 

	equation.set(expression) 

def equalpress(): 

	try: 

		global expression 

		expression = expression.replace('π', str(math.pi))
		expression = expression.replace('e', str(math.e))
		expression = expression.replace('^', '**')
		expression = expression.replace('√', 'math.sqrt')
		expression = expression.replace('∛', '**(1/3)')
		expression = expression.replace('sin(', 'math.sin(math.radians(')
		expression = expression.replace('cos(', 'math.cos(math.radians(')
		expression = expression.replace('tan(', 'math.tan(math.radians(')
		expression = expression.replace('cot(', '1 / math.tan(math.radians(')
		expression = expression.replace('cosec(', '1 / math.sin(math.radians(')
		expression = expression.replace('sec(', '1 / math.cos(math.radians(')
		expression = expression.replace('log', 'math.log10')
		expression = expression.replace('ln', 'math.log')

		expression = auto_close_brackets(expression)

		total = str(eval(expression)) 
		
		equation.set(total) 
		expression = "" 

	except: 

		equation.set(" ERROR ") 
		expression = "" 

def auto_close_brackets(exp):
    open_brackets = exp.count('(')
    close_brackets = exp.count(')')

    if open_brackets > close_brackets:
        exp += ')' * (open_brackets - close_brackets)
    return exp


def clear(): 
	global expression 
	expression = "" 
	equation.set("") 
	
def back(): 
	global expression
	expression = expression[:-1]
	equation.set(expression)




if __name__ == "__main__": 
	
	gui = tkinter.Tk()   #to create a canvas/window

	gui.configure(background="teal") 


	gui.title("Scientific Calculator") 

	gui.geometry("480x249")   #resolution 


	equation = tkinter.StringVar() 

	expression_field = tkinter.Entry(gui, textvariable=equation,bg ='#E3FEF7',fg='black') 
 
	expression_field.grid(columnspan=9, ipadx=180,ipady=10)

	CE = tkinter.Button(gui, text='CE', fg='black', bg='#77B0AA', 
				command=clear, height=2, width=7) 
	CE.grid(row=2, column=6) 

	back = tkinter.Button(gui, text=' Clear ', fg='black', bg='#77B0AA', 
					command=back, height=2, width=7) 
	back.grid(row=2, column=7) 

	buttonpi = tkinter.Button(gui, text='π', fg='black', bg='#77B0AA', 
					command=lambda: press('π'), height=2, width=7) 
	buttonpi.grid(row=3, column=0)
	
	buttone = tkinter.Button(gui, text=' e ', fg='black', bg='#77B0AA', 
					command=lambda: press('e'), height=2, width=7) 
	buttone.grid(row=3, column=1)

	remainder = tkinter.Button(gui, text=' % ', fg='black', bg='#77B0AA', 
					command=lambda: press('%'), height=2, width=7) 
	remainder.grid(row=3, column=2)

	power = tkinter.Button(gui, text=' a^b ', fg='black', bg='#77B0AA', 
					command=lambda: press('^'), height=2, width=7) 
	power.grid(row=3, column=3) 



	button7 = tkinter.Button(gui, text=' 7 ', fg='black', bg='#77B0AA', 
					command=lambda: press(7), height=2, width=7) 
	button7.grid(row=3, column=4) 

	button8 = tkinter.Button(gui, text=' 8 ', fg='black', bg='#77B0AA', 
					command=lambda: press(8), height=2, width=7) 
	button8.grid(row=3, column=5) 

	button9 = tkinter.Button(gui, text=' 9 ', fg='black', bg='#77B0AA', 
					command=lambda: press(9), height=2, width=7) 
	button9.grid(row=3, column=6) 

	button4 = tkinter.Button(gui, text=' 4 ', fg='black', bg='#77B0AA', 
					command=lambda: press(4), height=2, width=7) 
	button4.grid(row=4, column=4) 

	button5 = tkinter.Button(gui, text=' 5 ', fg='black', bg='#77B0AA', 
					command=lambda: press(5), height=2, width=7) 
	button5.grid(row=4, column=5) 

	button6 = tkinter.Button(gui, text=' 6 ', fg='black', bg='#77B0AA', 
					command=lambda: press(6), height=2, width=7) 
	button6.grid(row=4, column=6) 

	button1 = tkinter.Button(gui, text=1, fg='black', bg='#77B0AA', 
					command=lambda: press(1), height=2, width=7) 
	button1.grid(row=5, column=4)

	button2 = tkinter.Button(gui, text=' 2 ', fg='black', bg='#77B0AA', 
					command=lambda: press(2), height=2, width=7) 
	button2.grid(row=5, column=5) 

	button3 = tkinter.Button(gui, text=' 3 ', fg='black', bg='#77B0AA', 
					command=lambda: press(3), height=2, width=7) 
	button3.grid(row=5, column=6) 

	button0 = tkinter.Button(gui, text=' 0 ', fg='black', bg='#77B0AA', 
					command=lambda: press(0), height=2, width=7) 
	button0.grid(row=6, column=5) 
	
	power2 = tkinter.Button(gui, text=' 2^x ', fg='black', bg='#77B0AA', 
					command=lambda: press('2^'), height=2, width=7) 
	power2.grid(row=4, column=0) 
	
	recip = tkinter.Button(gui, text=' 1/x ', fg='black', bg='#77B0AA', 
					command=lambda: press('1/'), height=2, width=7) 
	recip.grid(row=4, column=1) 

	croot = tkinter.Button(gui, text=' ∛ ', fg='black', bg='#77B0AA', 
					command=lambda: press('∛('), height=2, width=7) 
	croot.grid(row=4, column=2) 

	root = tkinter.Button(gui, text=' √ ', fg='black', bg='#77B0AA', 
					command=lambda: press('√('), height=2, width=7) 
	root.grid(row=4, column=3) 

	plus = tkinter.Button(gui, text=' + ', fg='black', bg='#77B0AA', 
                command=lambda: press("+"), height=2, width=7) 
	plus.grid(row=6, column=6) 
	minus = tkinter.Button(gui, text=' - ', fg='black', bg='#77B0AA', 
                command=lambda: press("-"), height=2, width=7) 
	minus.grid(row=5, column=7) 
	multiply = tkinter.Button(gui, text=' * ', fg='black', bg='#77B0AA', 
                    command=lambda: press("*"), height=2, width=7) 
	multiply.grid(row=4, column=7) 
	divide = tkinter.Button(gui, text=' / ', fg='black', bg='#77B0AA', 
                    command=lambda: press("/"), height=2, width=7) 
	divide.grid(row=3, column=7) 
	Decimal= tkinter.Button(gui, text='.', fg='black', bg='#77B0AA', 
                    command=lambda: press('.'), height=2, width=7) 
	Decimal.grid(row=6, column=4) 
	buttonbro = tkinter.Button(gui, text=' ( ', fg='black', bg='#77B0AA', 
					command=lambda: press('('), height=2, width=7) 
	buttonbro.grid(row=2, column=4) 

	buttonclo = tkinter.Button(gui, text=' ) ', fg='black', bg='#77B0AA', 
					command=lambda: press(')'), height=2, width=7) 
	buttonclo.grid(row=2, column=5) 
	
	sine = tkinter.Button(gui, text=' sin ', fg='black', bg='#77B0AA', 
					command=lambda: press('sin('), height=2, width=7) 
	sine.grid(row=5, column=0) 
	cos = tkinter.Button(gui, text=' cos ', fg='black', bg='#77B0AA', 
					command=lambda: press('cos('), height=2, width=7) 
	cos.grid(row=5, column=1) 
	tan = tkinter.Button(gui, text=' tan ', fg='black', bg='#77B0AA', 
					command=lambda: press('tan('), height=2, width=7) 
	tan.grid(row=5, column=2) 

	cosec = tkinter.Button(gui, text=' cosec ', fg='black', bg='#77B0AA', 
					command=lambda: press('cosec('), height=2, width=7) 
	cosec.grid(row=6, column=0) 
	sec = tkinter.Button(gui, text=' sec ', fg='black', bg='#77B0AA', 
					command=lambda: press('sec('), height=2, width=7) 
	sec.grid(row=6, column=1) 
	cot = tkinter.Button(gui, text=' cot ', fg='black', bg='#77B0AA', 
					command=lambda: press('cot('), height=2, width=7) 
	cot.grid(row=6, column=2)

	log = tkinter.Button(gui, text=' log ', fg='black', bg='#77B0AA', 
					command=lambda: press('log('), height=2, width=7) 
	log.grid(row=5, column=3) 
	ln = tkinter.Button(gui, text=' ln ', fg='black', bg='#77B0AA', 
					command=lambda: press('ln('), height=2, width=7) 
	ln.grid(row=6, column=3)

	equal = tkinter.Button(gui, text=' = ', fg='black', bg='orangered', 
				command=equalpress, height=2, width=7) 
	equal.grid(row=6, column=7) 

	# start the GUI 
	gui.mainloop() 
