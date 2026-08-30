from math import *
def tsp(cost):
    n = len(cost)
    
    if n == 1:
        return cost[0][0]
    elif n == 0:
        return 0

    # Represents all the sub problems (partially complete routes for our salesman)
    # dp[mask][i] = min cost to visit all nodes in mask, ending at i
    dp = [[inf] * n for _ in range(2**n)]
    dp[1][0] = 0 #node 0 -> node 0 = 0 cost

    # Calculate cost of all the subproblems...
    for mask in range(1, 2**n):
        for i in range(n):
            if not (mask & (1 << i)): 
                continue # if node not in subproblem, skip
            if dp[mask][i] == inf:
                continue 

            for j in range(n): # Attempt to travel to all unvisited nodes
                if mask & (1 << j): #skip if already visited
                    continue

                # Cost to visit (new) node j from node i (skipping previously visited nodes)
                next_node = mask | (1 << j)
                dp[next_node][j] = min(dp[next_node][j], dp[mask][i] + cost[i][j])

    ans = inf
    for i in range(n):
        # for last node,  node i by our definition
        if dp[(1 << n) - 1][i] != inf:
            ans = min(ans, dp[(1 << n) -1][i] + cost[i][0])

    return ans 

if __name__ == "__main__":
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    res = tsp(cost)
    print(res)

