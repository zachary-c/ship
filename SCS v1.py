import tkinter
from tkinter import PhotoImage
from tkinter import Label



img = "E:\\ColdSleepTitle0000.gif"
button_1 = "Start"
button_2 = "Exit"
window = tkinter.Tk()

window.geometry("700x500")

backgroundimage = PhotoImage(file = img)
background = Label(window, image=backgroundimage)
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

def main():
	global backgroundimage
	global background
	global img
	img = "E:\\1.gif"
	backgroundimage = PhotoImage(file = img)
	background = Label(window, image=backgroundimage)
	background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	option1 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10, text = button_1, command = start)
	option2 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10, text = button_2, command = Exit)
	option1.place(anchor = "nw", x = 100, y = 300)
	option2.place(anchor = "nw", x = 500, y = 300)


#backgroundimage = PhotoImage(file = img)
#ackground = Label(window, image=backgroundimage)

def Exit():
	exit()

def start():
	global background
	global img
	print("yo")
	print(img)
	background.destroy()
	main()
	

option1 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10, text = button_1, command = start)
option2 = tkinter.Button(window, padx = 10, fg = "white", bg = "gray", pady = 10, text = button_2, command = Exit)
option1.place(anchor = "nw", x = 100, y = 300)
option2.place(anchor = "nw", x = 500, y = 300)



#text = tkinter.Text(window, bg = "green", height = 4, width = 20)

#text.pack()

window.mainloop()
