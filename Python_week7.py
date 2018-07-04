from tkinter import *
root = Tk()
root.title("Shreyas's calculator")
root.configure(background = "Red")

def compute():

	txt.delete(0.0, "end")
	txtname = etName.get()
	Score1 = int(etScore1.get())
	Score2 = int(etScore2.get())
	Score3 = int(etScore3.get())

	ave = (Score1 + Score2 + Score3)//3

	if ave < 50: 
		g = "Grade is F"
	elif ave >= 50 and ave < 80: 
		g = "Grade is C"
	elif ave >= 80 and ave < 100: 
		g = "Grade is B"
	else: 
		g = "Grade is A"
	txt.insert(0.0, txtname + " got " + str(ave) + " his " + g)

root.geometry("250x250")
Name1 = Label(root, text = "Name", font = "Times 12 bold", relief = "solid",
bg="Yellow")
Name1.grid(row = 0, column = 0)\

etName = Entry(root)
etName.config(background = "Orange")
etName.grid(row = 0, column = 1)

Score1 = Label(root, text = "Score1", font = "Times 12 bold", relief = "solid",
bg="Yellow")
Score1.grid(row = 1, column = 0)
etScore1 = Entry(root)
etScore1.config(background = "Green")
etScore1.grid(row = 1, column = 1)

Score2 = Label(root, text = "Score2", font = "Times 12 bold", relief = "solid",
bg="Blue")
Score2.grid(row = 2, column = 0)
etScore2 = Entry(root)
etScore2.config(background = "Yellow")
etScore2.grid(row = 2, column = 1)

Score3 = Label(root, text = "Score3", font = "Times 12 bold", relief = "solid",
bg="White")
Score3.grid(row = 3, column = 0)
etScore3 = Entry(root)
etScore3.config(background = "Blue")
etScore3.grid(row = 3, column = 1)

btn = Button(root, text = "Compute", command = compute)
btn.grid(row = 4, columnspan = 2)

txt = Text(root, width = 35, height = 5, background = "White", wrap = WORD)
txt.grid(row = 5, columnspan = 2, sticky = W)

root.mainloop()