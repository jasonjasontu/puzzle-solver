#!/usr/bin/env python
from Tkinter import *
import tkSimpleDialog

def buttonOne(event):
	Matrix[event.x/15][event.y/15]+=1
	print("Mouse clicked: (%s %s)" % (event.x, event.y))
	printGrid()
	return

def buttonTwo(event):
	Matrix[event.x/15][event.y/15]-=1
	print("Mouse right clicked: (%s %s)" % (event.x, event.y))
	printGrid()
	return

def printGrid():
	print "printingGrid"
	w.delete("all")
	for x in range(len(Matrix)):
		for y in range(len(Matrix[x])):
			if Type[x][y] == 'i':
				color = 'red'
			if Type[x][y] == 't':
				color = 'blue'
			if Type[x][y] == 'n':
				color = 'black'
			w.create_text([((x+1)*15)-5,((y+1)*15)-5], text=str(Matrix[x][y]),fill=color) 

def saveLevel(event):
	print "saving"
	file = open(name + ".txt", "w")
	for x in range(len(Matrix)):
		for y in range(len(Matrix[x])):
			if Matrix[x][y]>0: file.write("{\n\"type\":\"number\",\n\"location\":[\n"),file.write(str(x)),file.write(",\n"),file.write(str(Matrix[x][y])),file.write(",\n"),file.write(str(y)),file.write("\n]\n},\n"),
	file.write("\n")

        
def makeInfinite(event):
	Type[event.x/15][event.y/15] = 'i'
	px,py = event.widget.winfo_pointerxy()
	cx,cy = px-rx, py-ry
	print("Infinite at (%s %s)" % ( cx, cy))

def makeTeleporter(event):
	Type[event.x/15][event.y/15] = 't'
	px,py = event.widget.winfo_pointerxy()
	cx,cy = px-rx, py-ry
	print("Teleportor at (%s %s)" % (cx, cy))

master = Tk()
master.resizable(width=0, height=0) 

name =tkSimpleDialog.askstring("Name", "Enter Project Name" )
size =tkSimpleDialog.askinteger("Size", "Enter Project Demensions" )

Matrix = [[0 for x in xrange(size)] for x in xrange(size)] 
Type = [['n' for x in xrange(size)] for x in xrange(size)] 

w = Canvas(master, width=(size*15), height=(size*15))
w.bind('<Button-1>', buttonOne)
w.bind('<Button-2>', buttonTwo)
w.bind_all('s',saveLevel)
w.bind_all('i',makeInfinite)
w.bind_all('t',makeTeleporter)

w.pack()

printGrid()
mainloop()
