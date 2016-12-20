#!/usr/bin/env python
from Tkinter import *
import tkSimpleDialog

def buttonOne(event):
    Matrix[event.x/15][event.y/15]+=1  
    Location[0] = event.x/15
    Location[1] = event.y/15
    print "height increases at " , Location  
    printGrid()
    return

def buttonTwo(event):
    Matrix[event.x/15][event.y/15]-=1  
    Location[0] = event.x/15
    Location[1] = event.y/15
    print "height decreases at " , Location  
    printGrid()
    return

def printGrid():
	w.delete("all")
	for x in range(len(Matrix)):
            for y in range(len(Matrix[x])):
                if Type[x][y] == 'f':
                    color = 'white'
                if Type[x][y] == 'p':                         # bold the playercube 
                    color = 'green'
                if Type[x][y] == 'i':
                    color = 'red'
                if Type[x][y] == 't':
                    color = 'blue'
                if Type[x][y] == 'n':
                    color = 'black'
                w.create_text([(x*15)+10,(y*15)+10], text=str(Matrix[x][y]),fill=color) 

def saveLevel(event):
	print "saving"
        i = 0
        file = open(name + ".json", "w")
        file.write("{\n  \"meta\": {\n    \"color\": \"red\"\n  },\n")
        for x in range(len(Matrix)):
            for y in range(len(Matrix[x])):
                if Type[x][y] == 'p': 
                    file.write("  \"actor\": {\n    \"color\": \"red\",\n    \"location\": [\n      ")
                    file.write(str(x))
                    file.write(",\n      ")
                    file.write(str(Matrix[x][y] + 1))
                    file.write(",\n      ")
                    file.write(str(y))
                    file.write("\n    ]\n  },\n"),
	file.write("  \"pillars\": [\n")
	for x in range(len(Matrix)):
            for y in range(len(Matrix[x])):
                height = Matrix[x][y]
                if Matrix[x][y]>0: 
                    if i == 1: file.write(",\n")
                    file.write("    {\n      \"type\": \"")
                    if Type[x][y] == 'f':
                        height = 0
                        file.write("finish")
                    if Type[x][y] == 'n' or Type[x][y] == 'p':
                        file.write("number")
                    if Type[x][y] == 't':
                        file.write("teleporter")
                    if Type[x][y] == 'i':
                        file.write("infinite")
                    file.write("\",\n      \"location\": [\n        ")
                    file.write(str(x))
                    file.write(",\n        ")
                    file.write(str(height))
                    file.write(",\n        ")
                    file.write(str(y))
                    file.write("\n      ]\n    }")
                    i = 1
	file.write("]\n}")

def makeInfinite(event):
    Type[Location[0]][Location[1]] = 'i'
    print "Infinite at " , Location
    printGrid()
    
def makeTeleporter(event):
    Type[Location[0]][Location[1]] = 't'
    print "Teleproter at " , Location
    printGrid()

def makePlayerCube(event):
    Type[Location[0]][Location[1]] = 'p'
    print "PlayerCube at " , Location
    printGrid()
	
def makeFinishBlock(event):
    Type[Location[0]][Location[1]] = 'f'
    print "FinishBlock at " , Location
    printGrid()

def makeNumber(event):
    Type[Location[0]][Location[1]] = 'n'
    print "Make it back to Number at " , Location
    printGrid()
	
def testingmode(event):
    Testingmode[0] += 1
    if Testingmode[0] == 5:
        Testingmode[0] = 0
        print "close testing mode"
    else:  print "Open testing mode" , Testingmode

def hardEvaluation(event):
    Solving = [[0 for x in xrange(size+1)] for x in xrange(size+1)]                                                                       #set up
    cube = [[0 for x in xrange(2)] for x in xrange(5)]                                                            #maximum player cube is 5
    totalstep = 0
    loop_index = 2
    step = 0
    solutions = 0
    dead = 0
    amountofinfinte = 1
    playercube = 0
    for x in range(len(Matrix)):		
        for y in range(len(Matrix[x])):
            if Type[x][y] == 'p': 
                cube[playercube][0] = x
                cube[playercube][1] = y
                playercube += 1
            if Type[x][y] == 'i':
                amountofinfinte += 1
            totalstep = totalstep + Matrix[x][y]
            Solving[x][y] = Matrix[x][y]
    Printsolution = [ '' for x in xrange(playercube)]
    Solution = [[0 for x in xrange(4*playercube)] for x in xrange(totalstep*amountofinfinte*playercube)]

    while loop_index > 0:
        option = 0
        for ia in range(4*playercube):
            if Solution[step][ia] == 2: option = 1
        if option == 0:
            blocks = []
            deadorsolution = 1
            for ib in range(playercube):                                                                                                  #looking for options
                if Type[cube[ib][0]][cube[ib][1]] != 'f': blocks.append(ib)
            for ic in blocks:
                    if Solving[cube[ic][0]+1][cube[ic][1]] > 0 and 2 > Solving[cube[ic][0]][cube[ic][1]] - Solving[cube[ic][0]+1][cube[ic][1]] > -2: 
                        if Solving[cube[ic][0]+1][cube[ic][1]] - Solving[cube[ic][0]][cube[ic][1]] != 1 or Solving[cube[ic][0]-1][cube[ic][1]] <= Solving[cube[ic][0]][cube[ic][1]]:
                            solving_index = 1
                            for ib in range(playercube):
                                if cube[ic][0]+1 == cube[ib][0] and cube[ic][1] == cube[ib][1]: solving_index = 0
                            if solving_index == 1:
                                Solution[step][ic*4-4]=2
                    if Solving[cube[ic][0]][cube[ic][1]+1] > 0 and 2 > Solving[cube[ic][0]][cube[ic][1]] - Solving[cube[ic][0]][cube[ic][1]+1] > -2: 
                        if Solving[cube[ic][0]][cube[ic][1]+1] - Solving[cube[ic][0]][cube[ic][1]] != 1 or Solving[cube[ic][0]][cube[ic][1]-1] <= Solving[cube[ic][0]][cube[ic][1]]:
                            solving_index = 1
                            for ib in range(playercube):
                                if cube[ic][0] == cube[ib][0] and cube[ic][1]+1 == cube[ib][1]: solving_index = 0
                            if solving_index == 1:
                                Solution[step][ic*4-3]=2                    
                    if Solving[cube[ic][0]-1][cube[ic][1]] > 0 and 2 > Solving[cube[ic][0]][cube[ic][1]] - Solving[cube[ic][0]-1][cube[ic][1]] > -2: 
                        if Solving[cube[ic][0]-1][cube[ic][1]] - Solving[cube[ic][0]][cube[ic][1]] != 1 or Solving[cube[ic][0]+1][cube[ic][1]] <= Solving[cube[ic][0]][cube[ic][1]]:
                            solving_index = 1
                            for ib in range(playercube):
                                if cube[ic][0]-1 == cube[ib][0] and cube[ic][1] == cube[ib][1]: solving_index = 0
                            if solving_index == 1:
                                Solution[step][ic*4-2]=2
                    if Solving[cube[ic][0]][cube[ic][1]-1] > 0 and 2 > Solving[cube[ic][0]][cube[ic][1]] - Solving[cube[ic][0]][cube[ic][1]-1] > -2: 
                        if Solving[cube[ic][0]][cube[ic][1]-1] - Solving[cube[ic][0]][cube[ic][1]] != 1 or Solving[cube[ic][0]][cube[ic][1]+1] <= Solving[cube[ic][0]][cube[ic][1]]:
                            solving_index = 1
                            for ib in range(playercube):
                                if cube[ic][0] == cube[ib][0] and cube[ic][1]-1 == cube[ib][1]: solving_index = 0
                            if solving_index == 1:
                                Solution[step][ic*4-1]=2
            if Testingmode[0] > 3:    
                print "Solving:" , Solving
                print "Solution:" , Solution
            while deadorsolution == 1 and loop_index > 0:                                                                                      #dead or solution
                for ia in range(4*playercube):
                    if Solution[step][ia] != 0: deadorsolution = 0       # using break to break the while???
                if loop_index == 2 and deadorsolution == 1 :
                    blockleft = 0
                    for x in range(len(Matrix)):		
                            for y in range(len(Matrix[x])):
                                if Solving[x][y] > 0 and Type[x][y] != 'i' and Type[x][y] != 'f':
                                    blockleft += 1
                    for ib in range(playercube):
                        if Type[cube[ib][0]][cube[ib][1]] == 'f' or cube[ib][0] == -1: blockleft += 1
                    if blockleft == playercube:
                        for ib in range(playercube): Printsolution[ib] = 'Cube' + str(ib+1)
                        for x in range(len(Solution)):		
                            for y in range(len(Solution[x])):
                                if Solution[x][y] == 1:
                                    if y%4 == 0: Printsolution[y//4] = Printsolution[y//4] + ' right'
                                    if y%4 == 1: Printsolution[y//4] = Printsolution[y//4] + ' down'
                                    if y%4 == 2: Printsolution[y//4] = Printsolution[y//4] + ' left'
                                    if y%4 == 3: Printsolution[y//4] = Printsolution[y//4] + ' up'
                                    for ib in range(playercube):
                                        if ib != y//4: Printsolution[ib] = Printsolution[ib] + ' wait'
                        solutions += 1
                        print "solution" , solutions , ":" , Printsolution                        
                    else:
                        dead += 1
                        if Testingmode[0] > 0:
                            for ib in range(playercube): Printsolution[ib] = 'Cube' + str(ib+1)
                            for x in range(len(Solution)):		
                                for y in range(len(Solution[x])):
                                    if Solution[x][y] == 1:
                                        if y%4 == 0: Printsolution[y//4] = Printsolution[y//4] + ' right'
                                        if y%4 == 1: Printsolution[y//4] = Printsolution[y//4] + ' down'
                                        if y%4 == 2: Printsolution[y//4] = Printsolution[y//4] + ' left'
                                        if y%4 == 3: Printsolution[y//4] = Printsolution[y//4] + ' up'
                                        for ib in range(playercube):
                                            if ib != y//4: Printsolution[ib] = Printsolution[ib] + ' wait'
                            print "dead " , dead , ":" , Printsolution 
                    if Testingmode[0] > 1: print Solving
                    if Testingmode[0] > 2: print Solution
                    loop_index = 1
                if step == 0 and loop_index == 1 and deadorsolution == 1:
                    loop_index = 0
                if loop_index == 1 and deadorsolution == 1 and step != 0:
                    step -= 1                                                                                                             #going back
                    for ic in range(playercube):
                        if Solution[step][ic*4-4] == 1: 
                            Solution[step][ic*4-4] = 0
                            cube[ic][0] -= 1
                            id = ic
                        if Solution[step][ic*4-3] == 1: 
                            Solution[step][ic*4-3] = 0
                            cube[ic][1] -= 1
                            id = ic
                        if Solution[step][ic*4-2] == 1: 
                            Solution[step][ic*4-2] = 0
                            cube[ic][0] += 1
                            id = ic
                        if Solution[step][ic*4-1] == 1: 
                            Solution[step][ic*4-1] = 0
                            cube[ic][1] += 1
                            id = ic
                    if Type[cube[id][0]][cube[id][1]] != 'i':
                        Solving[cube[id][0]][cube[id][1]] += 1
                    loop_index = 1
        if option == 1:                                                                                                                   #moving cube
            solution_index = 0
            for ic in range(playercube):
                if Solution[step][ic*4-4] == 2 and solution_index == 0:
                        solution_index = 1
                        Solution[step][ic*4-4] = 1
                        if Type[cube[ic][0]][cube[ic][1]] != 'i':
                            Solving[cube[ic][0]][cube[ic][1]] -= 1
                        cube[ic][0] += 1
                if Solution[step][ic*4-3] == 2 and solution_index == 0:
                        solution_index = 1
                        Solution[step][ic*4-3] = 1
                        if Type[cube[ic][0]][cube[ic][1]] != 'i':
                            Solving[cube[ic][0]][cube[ic][1]] -= 1
                        cube[ic][1] += 1
                if Solution[step][ic*4-2] == 2 and solution_index == 0:
                        solution_index = 1
                        Solution[step][ic*4-2] = 1
                        if Type[cube[ic][0]][cube[ic][1]] != 'i':
                            Solving[cube[ic][0]][cube[ic][1]] -= 1
                        cube[ic][0] -= 1
                if Solution[step][ic*4-1] == 2 and solution_index == 0:
                        solution_index = 1
                        Solution[step][ic*4-1] = 1
                        if Type[cube[ic][0]][cube[ic][1]] != 'i':
                            Solving[cube[ic][0]][cube[ic][1]] -= 1
                        cube[ic][1] -= 1
            step += 1
            loop_index = 2
    hard = dead*100.00/(dead + solutions)
    print "Solutions:" , solutions , "Dead end:" , dead , "Hard" , hard, "%"
    
master = Tk()
master.resizable(width=0, height=0) 

name =tkSimpleDialog.askstring("Name", "Enter Project Name" )
size =tkSimpleDialog.askinteger("Size", "Enter Project Demensions" )

Matrix = [[0 for x in xrange(size)] for x in xrange(size)] 
Type = [['n' for x in xrange(size)] for x in xrange(size)] 
Location = [0 for x in xrange(2)]
Testingmode = [0 for x in xrange(1)]

w = Canvas(master, width=(size*15), height=(size*15))
w.bind('<Button-1>', buttonOne)
w.bind('<Button-2>', buttonTwo)
w.bind_all('s',saveLevel)
w.bind_all('i',makeInfinite)
w.bind_all('t',makeTeleporter)
w.bind_all('h',hardEvaluation)
w.bind_all('p',makePlayerCube)
w.bind_all('f',makeFinishBlock)
w.bind_all('n',makeNumber)
w.bind_all('j',testingmode)

w.pack()

printGrid()
mainloop()
