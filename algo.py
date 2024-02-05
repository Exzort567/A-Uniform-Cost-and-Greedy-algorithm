class Node(object):
    #X coordinate
    x = None

    #Y coordinate
    y = None

    #Label of the node
    label = None
    #Cost so far g(n)
    cost = 0
    #Heuristics (straight line distance from node to destination)
    sld = 0
    #Parent node of this node
    parent = None

    #constructor
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    #print to string method
    def __str__(self):
        return self.label +"("+str(self.x)+","+str(self.y)+") g(n):"+str(self.cost)
   
#Custom priority queue data structure for implementing sorting via cost
class PriorityQueue(object):
    array = None
    type = None

    def __init__(self, type):
        self.array = []
        self.type = type

    def enqueue(self, n):
        self.array.append(n)
        self.array.sort(reverse=True, key=self.sortBy)
   
    def size(self):
        return len(self.array)
   
    def dequeue(self):
        n = self.array.pop()
        return n
   
    def sortBy(self, n):
        if self.type == "ucs":
            return n.cost
        elif self.type == "greedy":
            return n.sld
        elif self.type == "a":
            return n.cost + n.sld 
    
    def getArr(self):
        return self.array

#Graph class
class Graph(object):
    edges = None
    vertices = None
    dist = None
    visited = None
    fringe = None

    #default constructor
    def __init__(self):
        self.edges = {}
        self.dist = {}
        self.vertices = {}

   # method to add a vertex
    def addVertex(self, v):
        self.edges[v.label] = []
        self.vertices[v.label] = v

    # method to connect two nodes
    def addEdge(self, v, n):
        self.edges[v.label].append(n)

    # method to remove a node
    def removeVertex(self, v):
        for key, value in self.edges.items():
            if (v.label in value):
                value.remove(v.label)
        if (v.label in value):
            del self.edges[v.label]

    #method to print the shortest path
    def backtrack(self, stack, goal):
        path = "\nBacktracking from the end node to the start node... The shortest path is: "
        while len(stack) != 0:
            n = stack.pop()
            if n:
                path += n.label +" "
        path += "\npath cost = "+ str(goal.cost)
        return path

    #method to manually calcuate the distance between two points(nodes)
    def calculateDist(self, v1, v2):
        return ((v1.x-v2.x)**2+(v1.y-v2.y)**2)**(1/2)

    #search function
    #params:
    #start - start node
    #end - end node
    #type - ucs, greedy_bfs, a  
    def search(self, start, end, type):
        #list of visited nodes
        self.visited = []

        #queue containing the unexplored nodes, specifying what to sort      
        self.fringe = PriorityQueue(type)

        #set current selected node
        current = None

        #create the start node
        n = start

        #set the start node's cost to 0
        n.cost = 0
        
        #set the start node's sld
        n.sld = self.calculateDist(start, end)

        #add the start node in the queue
        self.fringe.enqueue(n)
       

        #While the length of the queue is greater than 0;
        while self.fringe.size() > 0:
            #Select the node with the least g(n) by using dequeue
            #set the dequeued node as the current node
            current = self.fringe.dequeue()
            print("\nCurrent node", current.label, "is selected from the queue having: ", current.cost)

            #Check if current examined node is already visited
            if current.label in self.visited:
               continue
            else:
                self.visited.append(current.label)
                #Append the dequeued node to the explored list
               
                print("Goal test if current node is the destination node...")
                
                #Stop if goal is found
                if  current.label == end.label:
                    print("Stopping search. Destination found:", current.label)
                    break
                #Else, continue expansion
                else:
                    print("Current node is not the goal node... Proceeding exploration...")
                    #Loop the current node's neighbors and update the path cost and parent, then add to queue
                    for i in range(len(self.edges[current.label])):
                        #get the adjacent node from the graph
                        adj = self.edges[current.label][i]
                       
                        #get/compute the distance
                        d = self.calculateDist(adj, current)


                        #get the sld (for greedy and a*)
                        sld = self.calculateDist(adj, end)

                        #create the node for the neighbor
                        n = Node(adj.label, adj.x, adj.y)

                        #set the sld (for greedy and a*)
                        n.sld = sld
                        
                        #set the cost (g(n)) by using the formula, cost = prev cost + distance
                        n.cost = current.cost + d

                        #set the current node as the child node's parent
                        n.parent = current
                        
                       
                        #enqueue the neighbor node to the priority queue
                        self.fringe.enqueue(n)
                        
                       
        #If goal is found, display the explored nodes
        print("Visited vertices:", self.visited)

        #perform backtracking
        stack = []
        stack.append(current)
        current_node = current
        while current.parent != None:
            c = current.parent
            stack.append(c)
            current = c

        #display the shortest path    
        print(self.backtrack(stack, current_node))
   
if __name__ == '__main__':
    g = Graph()
    A = Node("A", 1, 3)
    B = Node("B", 2, 6)
    C = Node("C", 3, 2)
    D = Node("D", 5, 8)
    E = Node("E", 4, 4)
    F = Node("F", 6, 3)
    G = Node("G", 7, 5)
    H = Node("H", 9, 8)
    I = Node("I", 8, 3)
    J = Node("J", 10, 9)
   

    #Setting the nodes and edges
    g.addVertex(A)
    g.addEdge(A, B)
    g.addEdge(A, C)
    

    g.addVertex(B)
    g.addEdge(B, D)
    g.addEdge(B, A)
    
    g.addVertex(C)
    g.addEdge(C, E)
    g.addEdge(C, A)
    
   
    g.addVertex(D)
    g.addEdge(D, B)
    g.addEdge(D, H)
    g.addEdge(D, E)

    g.addVertex(E)
    g.addEdge(E, C)
    g.addEdge(E, F)
    g.addEdge(E, D)
    
    g.addVertex(F)
    g.addEdge(F, E)
    g.addEdge(F, I)
    
    g.addVertex(G)
    g.addEdge(G, I)
    g.addEdge(G, H)

    g.addVertex(H)
    g.addEdge(H, G)
    g.addEdge(H, D)
    g.addEdge(H, J)

    g.addVertex(I)
    g.addEdge(I, F)
    g.addEdge(I, G)

    g.addVertex(J)
    g.addEdge(J, H)

    
    

    #Performing the Uniform Cost Search, using the start node and end node
    #A as the start 
    #J as the end
    g.search(J, E,"a")