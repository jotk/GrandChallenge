
# coding: utf-8

# In[67]:


EdgeList = open("Graph1.net")

Nodes = int(EdgeList.readline().split()[1])

print(Nodes)

AdjacencyList = []

for x in range(Nodes): #make the matrix
    mylist = []
    for x in range(Nodes):
        mylist.append(False) #fill matrix with false
    AdjacencyList.append(mylist)
    
Edges = int(EdgeList.readline().split()[1])

la=0
for aLine in EdgeList: #iterate through file and fill the matrix accrodingly 
    node1 = int(aLine.split()[0])
    node2 = int(aLine.split()[1])
    AdjacencyList[node1][node2]= True
    AdjacencyList[node2][node1]= True #graph is unidirectional
    la+1
    print(la)


# In[70]:


print("Size of Adjacency Matrix:", len(AdjacencyList), "x", len(AdjacencyList[0])) # testing if the size of the array is as expected



# In[ ]:


def createSubgraphs(A, G, i, counter):
    #print(A)
    
    if i == len(G):
        if isConnected(A, G):
            counter = counter + 1
        return counter
    
    if len(A)>=5:
        if isConnected(A, G):
            counter = counter + 1
        return counter
    
    #Adding ith vertex
    
    B = []
    for x in A:
        B.append(x)
    A.append(i)
    if B == A:
        print("Fail")
    counter = counter + createSubgraphs(B, G, i+1, counter) #taking ith vertex
    counter = counter + createSubgraphs(A, G, i+1, counter) #not taking ith vertex
    return counter
    
    
    
def isConnected(A, G):

    if len(A)==0:
        print("empty")
        return False
    # visits all the nodes of a graph (connected component) using BFS
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = []

    queue.append(A[0])

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbors = []
            for i in range(0, len(G[node])):
                if (G[node][i] is True) and (i in A):
                    neighbors.append(i)

            # add neighbours of node to queue
            for x in neighbors:
                if x not in explored:
                    queue.append(x)
    for x in A:
        if x not in explored:
            return False 
        
    return True


A = []
print(createSubgraphs(A, AdjacencyList, 0, 0))


# In[23]:


graphs3text = open("allgraphs3.txt")
graph3 = []
for aLine in graphs3text:
    myVals = []
    index = 0
    for x in range(0, len(aLine)):
        print(x)
        if aLine[x] in ["0","1","2","3","4","5","6","7","8"]:
            myVals.append(aLine[x])
    graph3.append([])
    for y in range(0, len(myVals)):
        if y%2==0:
            myTuple = (myVals[y], myVals[y+1])
            graph3[index].append(myTuple)    
        if y == len(myVals)-1:
            exit
    index = index + 1
#vPrime = CreateSubG()
#vPrime = [81,9,72]
#whichShape(vPrime, ):

print(graph3)
    

