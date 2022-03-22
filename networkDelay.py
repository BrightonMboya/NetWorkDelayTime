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

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], n=4, k=2))