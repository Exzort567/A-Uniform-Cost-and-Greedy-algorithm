class Node(object):
    # X coordinate
    x = None
    # Y coordinate
    y = None
    # Label of the node
    label = None
    # Cost so far g(n)
    cost = 0
    # Heuristics (straight line distance from node to destination)
    sld = 0
    # Parent node of this node
    parent = None

    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def __str__(self):
        return self.label + "(" + str(self.x) + "," + str(self.y) + ") g(n):" + str(self.cost)

class PriorityQueue(object):
    array = None

    def __init__(self, n):
        self.array = []
        self.type = n


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
                           
        elif self.type == "greedy_bfs":
            return n.sld

        elif self.type == "a":
            return n.cost + n.sld      

class Graph(object):
    edges = None
    vertices = None
    dist = None
    visited = None
    fringe = None

    # default constructor
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
        self.edges[v.label].append(n.label)

    # method to remove a node
    def removeVertex(self, v):
        for key, value in self.edges.items():
            if (v.label in value):
                value.remove(v.label)
        if (v.label in value):
            del self.edges[v.label]

   
    def calculatePathCost(self, goal):
        pathCost= 0

    # Start from the goal node and traverse back to the start node
        current = goal
        while current.parent is not None:
            pathCost += self.dist[current.parent.label][self.edges[current.parent.label].index(current.label)]
            current = current.parent

        return pathCost

    # method to print the shortest path
    def backtrack(self, stack, goal):
        path = "\nBacktracking from the end node to the start node... The shortest path is: "
        while len(stack) != 0:
            n = stack.pop()
            if n:
                path += n.label +" "
        return path

    # method to manually calculate the distance between two points(nodes)
    def calculateDist(self, v1, v2):
        # Euclidean distance formula
        return ((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2) ** 0.5

    def search(self, start, end, type):
        # list of visited nodes
        self.visited = []

        # queue containing the unexplored nodes
        self.fringe = PriorityQueue(type)

        # set current selected node
        current = None


        # create the start node
        n = Node(start, 0, 0)
        if type == "ucs":

        # set the start node's cost to 0
            n.cost = 0
        elif type == "greedy_bfs":
            n.cost = self.vertices[start].sld
        elif type == "a":
            n.cost = self.vertices[start].sld

        # add the start node in the queue
        self.fringe.enqueue(n)
        print(n, "was added to queue.")
        current = None

        # While the length of the queue is greater than 0;
        while self.fringe.size() > 0:
            # Select the node with the least g(n) by using dequeue
            node = self.fringe.dequeue()
            print("\nCurrent node", node.label, "is selected from the queue having g(n):", node.cost)

            # set the dequeued node as the current node
            current = node
           
            # Check if the current examined node is already visited
            if node.label in self.visited:
                print("Current node", node.label, "was already visited. Skipping... ")
            else:
                self.visited.append(node.label)
                current = node
                print("Goal test if the current node is the destination node...")
                # Stop if the goal is found
                if node.label == end:
                    print("\nStopping search. Destination found:", node)
                    break
                # Else, continue expansion
                else:
                    print("Current node is not the goal node... Proceeding exploration...")
                    # Loop its neighbors and update the path cost and parent, then add to queue
                    for i in range(len(self.edges[node.label])):
                        # get the adjacent node from the graph
                        adj = self.edges[node.label][i]

                        # get the distance
                        d = self.dist[node.label][i]

                        # get the sld
                        sld = self.vertices[adj].sld

                        # create the node
                        n = Node(adj, 0, 0)

                        # set the sld
                        n.sld = sld
                        # set the cost (g(n)) by using the formula, cost = prev cost + distance
                        if type == "ucs":
                            n.cost = node.cost + d
                           
                        elif type == "greedy_bfs":
                            n.cost = n.sld

                        elif type == "a":
                            n.cost = node.cost + d
                           
                        #set the current node as the child node's parent  
                        n.parent = node
                       
                        # add the child node to the queue
                        self.fringe.enqueue(n)
                        print(n, "was added to queue.")

        # After searching, display the explored nodes
        print("\nVisited vertices:", self.visited)

        # perform backtracking
        stack = []
        stack.append(node)
        while current != None:
            c = current.parent
            stack.append(c)
            current = c

        # print the shortest path
        print(self.backtrack(stack, node, ))

        pathCost = self.calculatePathCost(node)
        print("path cost: ", pathCost)
       
if __name__ == '__main__':
    #Creating the graph (Romania)
    g = Graph()
    Ar = Node("Ar", 0, 0)
    Ze = Node("Ze", 0, 0)
    Ti = Node("Ti", 0, 0)
    Or = Node("Or", 0, 0)
    Si = Node("Si", 0, 0)
    Lu = Node("Lu", 0, 0)
    Me = Node("Me", 0, 0)
    Do = Node("Do", 0, 0)
    Cr = Node("Cr", 0, 0)
    Ri = Node("Ri", 0, 0)
    Pi = Node("Pi", 0, 0)
    Fa = Node("Fa", 0, 0)
    Bu = Node("Bu", 0, 0)

    #Setting the nodes and edges
    g.addVertex(Ar)
    g.addEdge(Ar, Ze)
    g.addEdge(Ar, Ti)
    g.addEdge(Ar, Si)

    g.addVertex(Ze)
    g.addEdge(Ze, Ar)
    g.addEdge(Ze, Or)

    g.addVertex(Or)
    g.addEdge(Or, Ze)
    g.addEdge(Or, Si)
   
    g.addVertex(Ti)
    g.addEdge(Ti, Ar)
    g.addEdge(Ti, Lu)

    g.addVertex(Si)
    g.addEdge(Si, Ar)
    g.addEdge(Si, Or)
    g.addEdge(Si, Fa)
    g.addEdge(Si, Ri)
   
    g.addVertex(Lu)
    g.addEdge(Lu, Ti)
    g.addEdge(Lu, Me)

    g.addVertex(Me)
    g.addEdge(Me, Lu)
    g.addEdge(Me, Do)

    g.addVertex(Do)
    g.addEdge(Do, Me)
    g.addEdge(Do, Cr)

    g.addVertex(Cr)
    g.addEdge(Cr, Do)
    g.addEdge(Cr, Ri)
    g.addEdge(Cr, Pi)

    g.addVertex(Pi)
    g.addEdge(Pi, Cr)
    g.addEdge(Pi, Ri)
    g.addEdge(Pi, Bu)

    g.addVertex(Ri)
    g.addEdge(Ri, Si)
    g.addEdge(Ri, Cr)
    g.addEdge(Ri, Pi)

    g.addVertex(Fa)
    g.addEdge(Fa, Si)
    g.addEdge(Fa, Bu)

    g.addVertex(Bu)
    g.addEdge(Bu, Fa)
    g.addEdge(Bu, Pi)

    #set the distances for the node's neighbors, this is just to set the distance to each edge
    #because in the example there was no x,y coordinates of the nodes
    g.dist = {}
    g.dist[Ar.label] = [75, 118, 140]
    g.dist[Ze.label] = [75, 71]
    g.dist[Or.label] = [71, 151]
    g.dist[Ti.label] = [118, 111]
    g.dist[Si.label] = [140, 151, 99, 80]
    g.dist[Lu.label] = [111, 70]
    g.dist[Me.label] = [70, 75]
    g.dist[Do.label] = [75, 120]
    g.dist[Cr.label] = [120, 146, 138]
    g.dist[Pi.label] = [138, 97, 101]
    g.dist[Ri.label] = [80, 146, 97]
    g.dist[Fa.label] = [99, 211]
    g.dist[Bu.label] = [211, 101]

    #Performing the Uniform Cost Search, using the start node and end node
    #Ti as the start
    #Fa as the end
    g.search("Ar", "Bu", "ucs")