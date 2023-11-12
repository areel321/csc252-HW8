'''
Name: Allison Reel
Peers: N/A
References: N/A

'''
import csv

def createGraph():
    neighborGraph = {}
    colorGraph = {}
    #TODO: create a graph from csv file
    with open('states.csv', newline='') as csvfile:
        statesreader = csv.reader(csvfile)
        for row in statesreader:
            #print(row[0])
            #print(row[1])
            statesList = row[1].split(";")
            neighborGraph[row[0]] = statesList
            colorGraph[row[0]] = -1
    print(neighborGraph)
    return neighborGraph, colorGraph


def randomStart(neighborGraph, colorGraph):
    #TODO: color in the graph from a random start point
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
        print(state)
        #color it in as color 0
        colorGraph[state] = 0
        #check the neighbors
        for v in neighborGraph[state]:
            if v != '':
                if colorGraph[v] == colorGraph[state]:
                    colorGraph[state] +=1
                    numColors+=1

        
        statesUnColored.remove(state)
        
            



    return neighborGraph, colorGraph, numColors+1




def mostNeighbors(neighborGraph, colorGraph):
    #TODO: color in the graph starting with the most neighbors
    #initiate number of colors needed as 0
    numColors = 0
    #find the state with the most neighbors
    statesUnColored = []
    numNeighbors = 0
    key = ''
    for k in neighborGraph:
        newNum = len(neighborGraph[k])
        if numNeighbors < newNum:
            numNeighbors = newNum
            key = k
            statesUnColored.append(key)

    while statesUnColored:
        #get the next state
        state = statesUnColored[0]
        print(state)
        #color it in as color 0
        colorGraph[state] = 0
        #check the neighbors
        for v in neighborGraph[state]:
            if v != '':
                if colorGraph[v] == colorGraph[state]:
                    colorGraph[state] +=1
                    numColors+=1
        statesUnColored.remove(state)

    return neighborGraph, colorGraph, numColors+1



def main():
    #TODO read in csv file
    neighborGraph, colorGraph = createGraph()
    #TODO prompt user to select strategy
    print("We have a dataaset of states to color in, would you like to start with a random start or the state with the most neighbors?")
    strategy = input("Enter R for random start or M for most neighbors:")
    #TODO run selected method
    if strategy == "R":
        neighborGraph, colorGraph, numColors = randomStart(neighborGraph, colorGraph)
    elif strategy == "M":
        neighborGraph, colorGraph, numColors = mostNeighbors(neighborGraph, colorGraph)
    else:
        print("invalid input")
    #TODO return results in readable way
    print("The maximum color is: ", numColors, "the color graph is: ", colorGraph)




if __name__ == '__main__':
    main()