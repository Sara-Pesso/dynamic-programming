def totalCost(mask, pos, cost, path):
    n = len(cost) # number of nodes in graph

    # Basis: if every node has been visited, return to pos = 0
    if mask == (1 << n) - 1:
        return cost[pos][0]

    # Check if we have already traversed this path (memoization)
    if (mask, pos) in path:
        return path[(mask, pos)]

    min_cost = float('inf')
    next_node = None

    #Try visiting the nodes not yet visited
    for i in range(n):
        if (mask & (1 << i)) == 0: #Compares bit mask to node i's bit; 
            # if the node i's bit is the same as in the bit mask (i.e., both 1) 
            # the & operator will return 2^n (the same as 1 << n in Python-ese).
            # Therefore, if the statement != 0, we've already been to that node
            # and need to skip to evaluating the next node. 


            # We are looking for the next shortest edge between nodes. So, we evaluate 
            # whether the current TSP path we ave stored (min_cost) is smaller than the one
            # currently being calculated. 
            cost_check = cost[pos][i] + totalCost(mask | (1 << i), i, cost, path)
            if cost_check < min_cost: # Keep shorter path
                min_cost = cost_check
                next_node = i
                
            
            # Note: totalCost(mask | (1 << i), i, cost) is updating the bitmask with
            # node i's bit (the | operator).

    path[(mask, pos)] = (min_cost, next_node)
    return min_cost

def tsp(cost):

    mask = 1
    pos = 0
    path = {}

    return totalCost(mask, pos, cost, path), path

if __name__ == "__main__":
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    result = tsp(cost)
    print("Min Distance:",result[0])
    print("Bitmasked memo:", result[1])

    # Reserve bitmasking to see the path!
    def get_path(memo):
        path = []
        current_mask = 1
        current_pos = 0
        
        while current_pos is not None:
            path.append(current_pos)
            # Look up what the best next city was from this state
            _, next_node = memo.get((current_mask, current_pos), (None, None))
            
            if next_node is not None:
                current_mask |= (1 << next_node)
            current_pos = next_node
            
        path.append(0) # Return back to start to complete the tour

        return path

    print("Path:", get_path(result[1]))
    