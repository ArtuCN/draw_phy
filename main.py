#!/usr/bin/env python3

import tkinter as tk


def color_square(event):


def makeSquares(root):
	global canvas
	canvas = tk.Canvas(root, width = 500, height = 500)
	canvas.pack()
	for i in range(20):
		for j in range(20):
			x = i * 25
			y = j * 25
			canvas.create_rectangle(x, y, x + 25,  y + 25, fill = "white", outline = "black")
	canvas.bind("<Button-1>", color_square)


def main():
	root = tk.Tk()
	makeSquares(root)
	root.mainloop()

if __name__ == "__main__":
	main()