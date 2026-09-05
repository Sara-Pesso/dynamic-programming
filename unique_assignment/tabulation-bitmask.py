from math import inf, nan
def assignment(cost):
    # Number of things to be assigned 
    n = len(cost)

    # Total states = 2^n
    num_states = 1 << n
    
    # Initialize DP array with a large value (infinity)
    dp = [inf] * num_states
    
    # Base case: 0 cost to assign 0 tasks to 0 people
    dp[0] = 0 
    
    # Iterate through every possible subset configuration
    for mask in range(num_states):
        # The number of set bits tells us which task index we are assigning next
        task_idx = bin(mask).count('1')
        
        # If all tasks are assigned, we're done with this configuration
        if task_idx == n:
            continue
            
        # Try to assign the 'task_idx' to any available person 'j'
        for j in range(n):
            # Check if person j is NOT yet assigned (j-th bit is 0)
            if not (mask & (1 << j)):
                next_mask = mask | (1 << j)
                new_cost = dp[mask] + cost[j][task_idx]
                
                # Update the next state with the minimum cost
                if new_cost < dp[next_mask]:
                    dp[next_mask] = new_cost
                    
    # The final state where all bits are 1 represents all people assigned
    return dp[(1 << n) - 1]

# Example Usage:
# 3 people, 3 tasks cost matrix
matrix = [
    [0, 1, 1],
    [1, 0, 1],
    [0, 1, 0]
]
print("Minimum Cost:", assignment(matrix)) 
