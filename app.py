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
import random

st.title('A Network Delay Time App')
st.write("""
    This App will allow you to determine the cost that will costs sending the signal to all the nodes to node k.
    Please provide the number of nodes in the network, the source node, destination node
    Also Provide the list of nodes in terms of [source, destination, cost] 
""")


nodes= []

nuOfNodes = int(st.number_input('Enter the number of nodes'))
keys = random.sample(range(1000, 99999), nuOfNodes+1)

for i in range(nuOfNodes):
    nodes.append([])

st.cache()
if nuOfNodes > 1:
    st.cache()
    for i in range(nuOfNodes):
        st.cache()
        srcNode = int(st.slider(label= "Enter the Source Node",   min_value= 0, max_value= 10, key=keys[i]))
        nodes[i].append(srcNode)
        dstNode = int(st.slider(label= "Enter the destination Node",   min_value= 0, max_value= 10, key=keys[i]))
        nodes[i].append(dstNode)
        cost = int(st.slider(label= "Enter the cost to reach this Node",   min_value= 0, max_value=50, key=keys[i]))
        nodes[i].append(cost)
        nodes.append([srcNode, dstNode, cost])
        
st.write(nodes)



# ans = networkDelayTime(nodes, 4, 2)

# ans = networkDelayTime([newNode], nuOfNodes, dstNode)
# st.write(ans)
