'''
Name: Allison Reel
Peers: N/A
References: N/A

'''
import csv

def createGraph():
    #DOCSTRING
    neighborGraph = {}
    colorGraph = {}
    #create a graph from csv file
    with open('states.csv', newline='') as csvfile:
        statesreader = csv.reader(csvfile)
        for row in statesreader:
            statesList = row[1].split(";")
            neighborGraph[row[0]] = statesList
            colorGraph[row[0]] = -1
    return neighborGraph, colorGraph


def randomStart(neighborGraph, colorGraph):
    #DOCSTRING
    #color in the graph from a random start point
    #initiate number of colors needed as 0
    numColors = 0
    #create a list of states we havent covered
    statesUnColored = []
    for k in neighborGraph:
        statesUnColored.append(k)
    #go through the list removing states as we color them
    while statesUnColored:
        #get the next state
        state = statesUnColored[0]
        #color it in as color 0
        colorGraph[state] = 0
        #check the neighbors
        for v in neighborGraph[state]:
            if v != '':
                if colorGraph[v] == colorGraph[state]:
                    colorGraph[state] +=1
                    if colorGraph[state] >= numColors:
                        numColors = colorGraph[state]
        statesUnColored.remove(state)
    return colorGraph, numColors


def mostNeighbors(neighborGraph, colorGraph):
    #DOCSTRING
    #color in the graph starting with the most neighbors
    #initiate number of colors needed as 0
    numColors = 0
    #find the state with the most neighbors
    statesUnColored = []
    numNeighbors = 0
    key = ''
    #FIXHERE
    newdict = neighborGraph.copy()
    for i in range(0,50):
        for k in newdict:
            newNum = len(newdict[k])
            if k not in statesUnColored:
                if numNeighbors < newNum:
                    numNeighbors = newNum
                    key = k
        numNeighbors = 0
        statesUnColored.append(key)
    while statesUnColored:
        #get the next state
        state = statesUnColored[0]
        #color it in as color 0
        colorGraph[state] = 0
        #check the neighbors
        for v in neighborGraph[state]:
            if v != '':
                if colorGraph[v] == colorGraph[state]:
                    colorGraph[state] +=1
                    if colorGraph[state] >= numColors:
                        numColors = colorGraph[state]
        statesUnColored.remove(state)
    return colorGraph, numColors


def main():
    #DOCSTRING
    #read in csv file
    neighborGraph, colorGraph = createGraph()
    #prompt user to select strategy
    print("We have a dataaset of states to color in, would you like to start with a random start or the state with the most neighbors?")
    strategy = input("Enter R for random start or M for most neighbors:")
    #run selected method
    if strategy == "R":
        colorGraph, numColors = randomStart(neighborGraph, colorGraph)
    elif strategy == "M":
        colorGraph, numColors = mostNeighbors(neighborGraph, colorGraph)
    else:
        return print("invalid input")
    #return results in readable way
    return print("The maximum color is:", numColors, "the color graph is:", colorGraph)


if __name__ == '__main__':
    main()