def assign_tasks(cost_matrix):
    n = len(cost_matrix)
    full_mask = (1 << n) - 1
    
    # dp[mask] = min cost, parent[mask] = (prev_mask, last_task_assigned)
    dp = {0: 0}
    parent = {}
    
    for mask in range(full_mask):
        if mask not in dp:
            continue
        person = bin(mask).count('1')
        for task in range(n):
            if not (mask & (1 << task)):
                next_mask = mask | (1 << task)
                new_cost = dp[mask] + cost_matrix[person][task]
                if next_mask not in dp or new_cost < dp[next_mask]:
                    dp[next_mask] = new_cost
                    parent[next_mask] = (mask, task)
                    
    # Reconstruct assignments
    assignments = [-1] * n

    print(parent)
    curr_mask = full_mask
    for person in range(n - 1, -1, -1):
        print(curr_mask)
        prev_mask, task = parent[curr_mask]
        assignments[person] = task
        curr_mask = prev_mask
        
    return dp[full_mask], assignments

# Example usage:
costs = [
    [3,4,7],
    [11,15,8],
    [9,4,6]
]
total_cost, result = assign_tasks(costs)
print("Minimum Cost:", total_cost)
print("Assignments (Person -> Task):", result)
