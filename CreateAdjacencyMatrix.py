
# coding: utf-8

# In[72]:


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

for aLine in EdgeList: #iterate through file and fill the matrix accrodingly 
    node1 = int(aLine.split()[0])
    node2 = int(aLine.split()[1])
    AdjacencyList[node1][node2]= True
    AdjacencyList[node2][node1]= True #graph is unidirectional


# In[75]:


print("Size of Adjacency Matrix:", len(AdjacencyList), "x", len(AdjacencyList[0])) # testing if the size of the array is as expected

#print(AdjacencyList)

if AdjacencyList[0][101]==True and AdjacencyList[101][0]==True:
    print("File Read and Upload works")

