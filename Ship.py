import tkinter
from tkinter import PhotoImage
from tkinter import Label

skillset = ""
carrier = ""
img = "Title.gif"#E:\\zachary\\Programming\\Python\\ColdSleep\\gif files\\ColdSleepTitle0000.gif"
combination = []
over_2 = False

window = tkinter.Tk()
deckadoorstate = False

window.geometry("700x500")

backgroundimage = PhotoImage(file = img)
background = Label(window, image=backgroundimage)
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

option4 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "4", command = lambda: deckAterminal("Terminal4.gif"))	
option5 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "5", command = lambda: deckAterminal("Terminal5.gif"))	
option6 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "6", command = lambda: deckAterminal("Terminal6.gif"))	
option7 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "7", command = lambda: deckAterminal("Terminal7.gif"))	
option8 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "8", command = lambda: deckAterminal("Terminal8.gif"))	
option9 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "9", command = lambda: deckAterminal("Terminal9.gif"))	
option10 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^")

def Exit():
	exit()

def HallTwo5():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "Hall24.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = HallTwo3)
	option1.place(anchor = "nw", x = 310, y = 450)	

def HallTwo4():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "Hall25.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = HallTwo2)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = HallTwo3)
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)

def HallTwo3():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "Hall23.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = HallTwo4)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^")
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = HallTwo5)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)


def HallTwo2():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "Hall22.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = HallTwo1)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Junctiondoor)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = HallTwo1)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)

def HallTwo1():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "Hall21.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = HallTwo2)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = HallTwo3)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = HallTwo2)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)

def Junction4():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	background.destroy()
	img = "Junction5.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = Junctiondoor)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = HallTwo1)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = Junction1)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)

def Junction3():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	background.destroy()
	img = "Junction6.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = Junction1)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Hall4)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = Junctiondoor)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)

def Junction1():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	background.destroy()
	img = "Junction4.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = Junction2)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Junction3)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = Junctiondoor)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)

def Junction2():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	background.destroy()
	img = "Junction1.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = Junctiondoor)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Junction4)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = Junction1)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)

def Junctiondoor():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	background.destroy()
	img = "Junctiondoor.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = Junction1)
#	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^")
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = Junction2)
	option1.place(anchor = "nw", x = 310, y = 450)	
#	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)

def Hall4():
	global img
	global option1
	global option2
	global option3
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	background.destroy()
	img = "Hall4.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = Hall3)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Hall1)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = Hall3)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)
	

def Hall3():
	global img
	global option1
	global option2
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	background.destroy()
	img = "Hall3.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = Hall4)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Junctiondoor)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = Hall4)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)
	option3.place(anchor = "nw", x = 360, y = 450)


def Hall2():
	global img
	global option1
	global option2
	global background
	global backgroundimage
	option1.destroy()
	background.destroy()
	img = "Hall2.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = Hall1)# command = south4)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Hall3)# command = west3)
	option1.place(anchor = "nw", x = 310, y = 450)	
	option2.place(anchor = "nw", x = 335, y = 420)

def Hall1():
	global img
	global option1
	global option2
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	background.destroy()
	img = "Hall1.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = west4)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = Hall2)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 335, y = 420)

def Hall15():
	global img
	global option1
	global option2
	global option3
	global option10
	global background
	global backgroundimage
	option1.destroy()
	option2.destroy()
	option3.destroy()
	option10.destroy()
	background.destroy()
	img = "Hall1_5.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Hall2)# command = west3)
	option1.place(anchor = "nw", x = 335, y = 420)

def deckAterminal(IMG):
	global img 
	global option1
	global option2
	global option3
	global option4
	global option5
	global option6
	global option7
	global option8
	global option9
	global deckadoorstate
	global combination
	global backgroundimage
	global background
	global over_2
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	option4.destroy()
	option5.destroy()
	option6.destroy()
	option7.destroy()
	option8.destroy()
	option9.destroy()
	img = IMG
#	print(combination)
	if IMG == "Terminal1.gif":
		combination.append(1)
	elif IMG == "Terminal2.gif":
		combination.append(2)
	elif IMG == "Terminal3.gif":
		combination.append(3)
	elif IMG == "Terminal4.gif":
		combination.append(4)
	elif IMG == "Terminal5.gif":
		combination.append(5)
	elif IMG == "Terminal6.gif":
		combination.append(6)
	elif IMG == "Terminal7.gif":
		combination.append(7)
	elif IMG == "Terminal8.gif":
		combination.append(8)
	elif IMG == "Terminal9.gif":
		combination.append(9)
	if combination == [2, 1]:
		deckadoorstate = True
#		print(deckadoorstate)
		img = "TerminalblankOpen.gif"
	if len(combination) == 2:
		over_2 = True
		img = "Terminalnumbers.gif"
#	print(combination)
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option0 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "v", command = east4)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "1", command = lambda: deckAterminal("Terminal1.gif"))
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "2", command = lambda: deckAterminal("Terminal2.gif"))
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "3", command = lambda: deckAterminal("Terminal3.gif"))
	option4 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "4", command = lambda: deckAterminal("Terminal4.gif"))	
	option5 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "5", command = lambda: deckAterminal("Terminal5.gif"))	
	option6 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "6", command = lambda: deckAterminal("Terminal6.gif"))	
	option7 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "7", command = lambda: deckAterminal("Terminal7.gif"))	
	option8 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "8", command = lambda: deckAterminal("Terminal8.gif"))	
	option9 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "9", command = lambda: deckAterminal("Terminal9.gif"))	
	option0.place(anchor = "nw", x = 335, y = 420)	
	if over_2 == True:
		pass
	else:
		option1.place(anchor = "nw", x = 235, y = 192)	
		option2.place(anchor = "nw", x = 331, y = 192)	
		option3.place(anchor = "nw", x = 427, y = 192)	
		option4.place(anchor = "nw", x = 230, y = 252)	
		option5.place(anchor = "nw", x = 331, y = 252)	
		option6.place(anchor = "nw", x = 432, y = 252)	
		option7.place(anchor = "nw", x = 225, y = 317)	
		option8.place(anchor = "nw", x = 331, y = 317)	
		option9.place(anchor = "nw", x = 437, y = 317)	

def south4():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "4south.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = west4)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = east4)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	

def west4():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "4west.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = north4)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = south4)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = west3)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	
	option3.place(anchor = "nw", x = 335, y = 420)

def north4():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "4north.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = east4)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = west4)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	

def east4():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	global combination
	global over_2
	over_2 = False
	combination = []
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	if deckadoorstate == True:
		img = "4eastopen.gif"
	else:
		img = "4east.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = south4)
	if deckadoorstate == True:
		option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = lambda: deckAterminal("TerminalblankOpennumbers.gif"))
		option10 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = Hall15)
		option10.place(anchor = "nw", x = 275, y = 275)
	else:
		option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = lambda: deckAterminal("Terminalblank.gif"))
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = north4)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)
	option3.place(anchor = "nw", x = 335, y = 420)


def south3():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "3south.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = west3)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = east3)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	

def west3():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "3west.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = north3)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = west2)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = south3)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	
	option3.place(anchor = "nw", x = 335, y = 420)

def north3():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "3north.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = east3)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = west3)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	

def east3():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	if deckadoorstate == True:
		img = "3eastopen.gif"
	else:
		img = "3east.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = south3)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = east4)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = north3)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	
	option3.place(anchor = "nw", x = 335, y = 420)

def east2():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	if deckadoorstate == True:
		img = "2eastopen.gif"
	else:
		img = "2east.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = south2)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = east3)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = north2)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	
	option3.place(anchor = "nw", x = 335, y = 420)

def north2():
	global img
	global option1
	global option2
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "2north.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = east2)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = west2)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)

def west2():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "2west.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = north2)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = east1)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = south2)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)
	option3.place(anchor = "nw", x = 335, y = 420)

def south2():
	global img
	global option1
	global option2
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "2south.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = west2)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = east2)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)

def north1():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "1north.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = east1)
	option1.place(anchor = "nw", x = 360, y = 450)

def south1():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	img = "1south.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = east1)
	option1.place(anchor = "nw", x = 310, y = 450)

def east1():
	global img
	global option1
	global option2
	global option3
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	option3.destroy()
	if deckadoorstate == True:
		img = "1eastopen.gif"
	else:
		img = "1east.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = ">", command = south1)
	option3 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = east2)
	option2 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "<", command = north1)
	option1.place(anchor = "nw", x = 360, y = 450)
	option2.place(anchor = "nw", x = 310, y = 450)	
	option3.place(anchor = "nw", x = 335, y = 420)

def in_capsuleA():
	global img
	global option1
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	img = "Wakeup3.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, height = 1, width = 4, fg = "white", bg = "gray", text = "^", command = south2)
	option1.place(anchor = "nw", x = 338, y = 420)

def awake():
	global img
	global option1
	global backgroundimage										
	global background
	background.destroy()									
	option1.destroy()
	img = "Wakeup2.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image = backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10, text = "Open Doors", command = in_capsuleA)	
	option1.place(anchor = "nw", x = 300, y = 350)

def start():
	global option1
	global option2
	global backgroundimage
	global background
	background.destroy()
	option1.destroy()
	option2.destroy()
	img = "Wakeup.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image=backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10, text = "Lean Forward", command = awake)	
	option1.place(anchor = "nw", x = 300, y = 350)
	
option1 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10, text = "Start", command = start)
option2 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10, text = "Exit", command = Exit)
option3 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10)
option1.place(anchor = "nw", x = 150, y = 300)
option2.place(anchor = "nw", x = 500, y = 300)

window.mainloop()