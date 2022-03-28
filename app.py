import re
def networkDelayTime(times, n, k):
    import heapq
    from collections import defaultdict
    
    #creating the adjacency list
    edges = defaultdict(list)
    
    #add the destination and the weight it takes to reach there
    for u,v,w in times:
        edges[u].append((w, v))
        
    #creating the minHeap
    minHeap = [(0, k)]
    visited = set()
    t = 0
    
    #now do the breadth first search
    while minHeap:
        currentNode = heapq.heappop(minHeap)
        w1, n1 = currentNode
        #check if n1 is visited, if yes jump to the next iter
        if n1 in visited:
            continue
        visited.add(n1)

        t = max(t, w1)

        #consider the neighbors of n1 and add them to the queue
        for w2, n2 in edges[n1]:
            if n2 not in visited:
                heapq.heappush(minHeap, (w1+w2, n2))
            
    #here return the result if you have visited all the nodes in the graph
    return t if len(visited) == n else -1



import streamlit as st
st.title('A Network Delay Time App')
st.write("""
    This App will allow you to determine the cost that will costs sending the signal to all the nodes to node k.
    Please provide the number of nodes in the network, the source node, destination node
    Also Provide the list of nodes in terms of [source, destination, cost] 
""")

# nodes = st.text_input("Enter the nodes in form of [src, dst, cost] seperate different nodes with a comma (,)", key=1)
# st.write("The nodes are ", nodes)

# nuOfNodes = st.text_input('Please Enter the number of Nodes', key=2)
# st.write('The number of nodes is ', nuOfNodes)

# dstNode = st.text_input('Please Enter the Source Node ', key=4)
# st.write("The Destination node is ", dstNode)


nodes_ = []
node = []
nuOfNodes = int(st.number_input('Enter the number of nodes'))

st.cache()

# src = st.number_input("Enter the Source Node", key='src')
# dst = st.number_input("Enter the dst node", key='dst')
# cost = st.number_input("Enter the cost", key='cost')

# while nuOfNodes:
#     if src:
#         continue
#     if dst:
#         continue
#     if cost:
#         continue
#     cont = st.text_input("Do you need to add more nodes? yes/no")
#     if cont == 'yes':
#         continue
#     else:
#         break
    
    


def askNodes(nodes):
    srcNode = int(st.slider(label= "Enter the Source Node",   min_value= 0, max_value= 10, key='sourceNode'))
    dstNode = int(st.slider(label= "Enter the destination Node",   min_value= 0, max_value= 10, key='DstNode'))
    cost = int(st.slider(label= "Enter the cost to reach this Node",   min_value= 0, max_value=50, key='cost'))
    nodes.append([srcNode, dstNode, cost])
    cont = st.text_input("Do you need to add more nodes? yes/no")
    if cont == 'yes':
        askNodes(nodes)
    else:
        return nodes

# nodes = askNodes(nodes_)
# st.write(nodes)

# while True:
#     collectNodes = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
#     nodes = st.text_input("Please Enter the source, destination, and cost of the node", key=)
#     # st.write(collectNodes(nodes))
#     cont = st.text_input("Do you want to enter more nodes? Yes or no")
#     if cont == 'no':
#         break
#     else:
#         continue



# ans = networkDelayTime(nodes_, 4, 2)

# ans = networkDelayTime([newNode], nuOfNodes, dstNode)
# st.write(ans)
