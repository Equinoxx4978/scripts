import tkinter as tk
from random import randint

title = "Hydra"
description = "Cut one off and two more shall take its place."
w = 300
h = 100

def generate():
	
	# Create a new Tkinter window
	window = tk.Tk()
	
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()
	xpos = randint(1, screen_width)
	ypos = randint(1, screen_height)

	# Set the window title
	window.title(title)

	# Set the window size
	window.geometry('%dx%d+%d+%d' % (w, h, xpos, ypos))

	# Create a label with the text "This is a popup"
	label = tk.Label(window, text=description)
	label.pack()
	
	def closeWindow():
		generate2()
		window.destroy()

	# Bind the window close event to the on_close function
	window.protocol("WM_DELETE_WINDOW", closeWindow)

def generate2():
	generate()
	generate()


# Create a new Tkinter window
window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
xpos = randint(1, screen_width)
ypos = randint(1, screen_height)

# Set the window title
window.title(title)

# Set the window size
window.geometry('%dx%d+%d+%d' % (w, h, xpos, ypos))

# Create a label with the text "This is a popup"
label = tk.Label(window, text=description)
label.pack()

def closeWindow():
	generate2()
	window.destroy()

# Bind the window close event to the on_close function
window.protocol("WM_DELETE_WINDOW", closeWindow)

# Show the window
window.mainloop()
