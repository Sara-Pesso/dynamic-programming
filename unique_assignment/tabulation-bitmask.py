from math import inf, nan
def assignment(cost):
    # Number of things to be assigned 
    n = len(cost)

    # Total states = 2^n
    nstates = 1 << n
    
    # Initialize DP array with a large value (infinity)
    dp = [inf] * nstates
    
    # Base case: 0 cost to assign 0 objs to 0 people
    dp[0] = 0 
    
    # Iterate through every possible subset configuration
    for mask in range(nstates):
        # The number of set bits tells us which obj index we are assigning next
        obj_idx = bin(mask).count('1')
        
        # If all objs are assigned, we're done with this configuration
        if obj_idx == n:
            continue
            
        # Try to assign the 'obj_idx' to any available person 'j'
        for j in range(n):
            # Check if person j is NOT yet assigned (j-th bit is 0)
            if (mask & (1 << j)) == 0:
                next_mask = mask | (1 << j)
                new_cost = dp[mask] + cost[j][obj_idx]
                
                # Update the next state with the minimum cost
                if new_cost < dp[next_mask]:
                    dp[next_mask] = new_cost
                    
    # The final state where all bits are 1 represents all people assigned
    return dp[(1 << n) - 1]

# Example Usage:
# 3 people, 3 objs cost matrix
matrix = [
    [3,4,7],
    [11,15,8],
    [9,4,6]
]
print(assignment(matrix))
