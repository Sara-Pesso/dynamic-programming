from math import inf
def assignment(cost):
    # Number of things to be assigned 
    n = len(cost)

    # 1. We will do this using a bitmask. 
    # Each person will represent one bit in our mask. 
    # This will represent the subset of people assigned an object. 
    # So, we will need to work through 2^n states
    nstates = 1 << n
    
    # 2. Initialize the DP table, filling in the minimum cost at each intermediate state with infinity
    dp = [inf] * nstates
    
    # 3. Basis: because assigning 0 objects to 0 people will always cost nothing
    dp[0] = 0 

    # 3.5. Initializing a Python dictionary that maps our *new mask* to a tuple of 
    # the *previous mask* and *person j* (for extracting the assignment solution later)
    previous_assignment = {}

    # ---- Begin Tabulation & Bitmasking ----
    # 4. Iterate through all the possible bitmasks (that is, subsets of people assigned an object)
    for mask in range(nstates):
        # Determine which object we are about to assign to someone. This can be determined by determining how many bits in our bitmask have already been set.
        obj_idx = bin(mask).count('1')
        
        # Because we are iterating from 0, if obj_id = n$ we have already assigned all the objects to a person and we continue out of the loop.
        if obj_idx == n:
            continue
            
        # 5. Try to assign object i to any available person, j, by looping through 
        # the n bits in the mask and determining if they haven't yet been assigned 
        # an object. We can do this by using the AND (&) operator to determine if 
        # bit j is unset (i.e, if bit j = 0):
        for j in range(n):
            # If bit j=0, we assign object $i$ to bit j using the OR (|) operator. Then, we 
            # calculate the cost make that assign which is as simple as finding element (j,i) 
            # in our cost matrix and adding it to the *current* cost held for the current mask 
            # in our DP table:
            if (mask & (1 << j)) == 0:
                new_mask = mask | (1 << j)
                new_cost = dp[mask] + cost[j][obj_idx]
                
                # Because we are looking for the *minimum* cost of assigning all n 
                # objects, we only accept the new cost derived from assign object i 
                # to person j with respect to the *new* mask if our *new* 
                # cost is less than whatever is *currently* held in the DP table for 
                # the *new* mask.
                if new_cost < dp[new_mask]:
                    dp[new_mask] = new_cost
                    # every time we find a new current minimum cost in our search, we update the previous 
                    # assignment table at the same time as the DP table. This keeps track of where the minimum solution "came from".
                    previous_assignment[new_mask] = (mask, j)
                    
    # Ultimately, because this a tabulation solution, once our program has 
    # looped through all bitmasks, the final entry in our DP table, 
    # DP((1 << n) - 1) -- that is, the bitmask that contains all 1s -- will hold the minimum cost to assign n objects to n people. 
    
    # --- Extracting Assignments from the DP Table ----
    # Extracting the final optimal assignments is then pretty straight forward. 
    # We initialize an empty list to hold the assignments where the list's index j
    # corresponds to person j. Then, we simply loop *backward* through each person 
    # n > j > 0 (since person n was assigned last). Each iteration we find the 
    # previous bitmask and task assigned for each current bitmask, assign person j
    # to that task, and loop again using the previous bitmask as the current mask:
    n = len(costs)
    assignments = [-1] * n
    curr_mask = (1 << n) - 1

    for person in range(n - 1, -1, -1):
        prev_mask, task = previous_assignment[curr_mask]
        assignments[person] = task
        curr_mask = prev_mask
    return dp[(1 << n) - 1], assignments

## ---- MAIN ----
# Example Usage:
# 3 people (rows), 3 objs (columns) cost matrix
# Where each c_{ji} represents the cost of assigning object i to person j
costs = [
    [3,4,7],
    [11,15,8],
    [9,4,6]
]

## ---- RESULTS ----
min_cost, assignments = assignment(costs)
for i in range(len(assignments)):
    print(f"Person {i} -> Object {assignments[i]}: Cost {costs[i][assignments[i]]}")
print("Min. Cost:", min_cost)