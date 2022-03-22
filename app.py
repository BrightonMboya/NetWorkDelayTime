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

nodes = st.text_input("Enter the nodes in form of [src, dst, cost] seperate different nodes with a comma (,)", key=1)
st.write("The nodes are ", nodes)

nuOfNodes = st.text_input('Please Enter the number of Nodes', key=2)
st.write('The number of nodes is ', nuOfNodes)

dstNode = st.text_input('Please Enter the Source Node ', key=4)
st.write("The Destination node is ", dstNode)

ans = networkDelayTime
