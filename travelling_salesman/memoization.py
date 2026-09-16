from math import inf
def tsp(mask, pos, cost, path):
    # 1. First, find the number of nodes in the graph, n. We'll also initialize a couple variables:
    # - Since the goal of TSP is to find the minimum cost to move between all the nodes in the graph, 
    # we'll start a variable to track the minimum cost, and initialize it as inf-- a value every path
    # will be shorter than
    # - We'll also need to track the node we are moving to next, so we'll do a similar thing and make a
    # variable we can update as we move along.
    n = len(cost)
    min_cost = inf
    next_node = None

    # 2. Because this algorithm will recurse each time we fill in a bit in our bitmask, we need to 
    # check that we need to check that we are not at the full bitmask (i.e., the bitmask consisting of 
    # all 1s-- indicating that every node has been visited). If this is the case, we just need to return
    # the cost of going from our current position to node $0$ from our cost matrix. This is called the 
    # basis or base case.
    if mask == (1 << n) - 1:
        return cost[pos][0], path

    # 3. Check the DP (memoization) table to see if we have the result to this subproblem. In other words: have we 
    # tried traversing this path before?
    if (mask, pos) in path:
        return path[(mask, pos)][0], path


    # 4. Now, we'll loop through the nodes and determine which ones are next viable steps. Check that 
    # we have not yet been to node i: make sure the i-th bit in the current bitmask is set to 0. 
    # This indicates we're potentially able to move to this node next.
    for i in range(n):
        if (mask & (1 << i)) == 0:  

            # 5. We're looking for the least expensive path (in the classic TSP, this is the shortest total 
            # distance traveled) between all the nodes. So, we will calculate the hypothetical cost if we were 
            # to travel to node i next. This is where this algorithm becomes recursive in nature; to calculate 
            # the total cost, we add the cost of moving from node i to node j from the cost matrix, C_ij to the 
            # continuing with the DP algorithm as if we chose this connection next. Then, we can compare this 
            # cost to whatever is currently held as the minimum cost. If this new value is smaller, we update 
            # our variables: 
            cost_check = cost[pos][i] + tsp(mask | (1 << i), i, cost, path)[0]
            if cost_check < min_cost: # Keep shorter path
                min_cost = cost_check
                next_node = i

    # 6. When we are done with this loop, we will have found the minimum possible cost for this bitmask, 
    # starting node combination. So, record that and return the minimum cost found and associated path.
    path[(mask, pos)] = (min_cost, next_node)
    return min_cost, path

### ===== MAIN FUNCTION =====
# 0. Because of the recursive nature of this algorithm, we are going to initialize some variables in our
# function call. This way, every time the function is called these get passed along as they are currently
# set. As in previous algorithms, each element C_ij in the cost matrix represents the cost to move from 
# node i to node j.
adj = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost, dp = tsp(mask=1, pos=0, cost=adj, path={})
print("Min Distance:", min_cost)
print("Bitmask memo:", dp)

## -====== EXTRACTING PATH FROM MEMOIZATION TABLE =====
# 1. First, as always we'll initialize some variables we'll need:
    # - An empty list to append our path into
    # - The final bitmask (bitmask of all ones) indicating the end state of the TSP
    # - The current node (starting at node 0, because we are working backwards)
def get_path(memo):
    path = []
    current_mask = 1
    current_node = 0

    # 2. Now, we will loop through the memoization table, until we have reached the beginning of the path. 
    # At each iteration, append the index of the node to our list. 
    while current_node is not None:
        path.append(current_node)

        # 3. Recall that the memoization table from our algorithm maps the tuple of next bitmask and next 
        # node j to the tuple of the current bitmask and current node i. So, given the final mask and the 
        # final node, which we know to be node 0, we can find the previous bitmask and the previous node 
        # (i.e., we can figure out how we got to where we currently are). When we've reached the first bitmask,
        # obviously there's no previous step. So, we will flag the next_node as None and this will be our signal
        # to break from our loop.
        try:
            _, next_node = memo[(current_mask, current_node)]
        except:
            next_node = None
        
        if next_node is not None:
            current_mask |= (1 << next_node)
        current_node = next_node

    # 4. Finally, to complete the path we loop back to node 0. Then, return the path! 
    path.append(0) 
    return path

print("Path:", get_path(dp))
    