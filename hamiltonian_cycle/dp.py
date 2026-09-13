def find_hamiltonian_cycle(adj_matrix):
    # 1. Initialize variables needed for DP algorithm: find n the (number of nodes), calculate
    #  the total number of states ($2^n$, represented by a n-bit bitmask).

    # Number of nodes
    n = len(adj_matrix)
    # Total combinations of nodes is 2^n
    num_states = 1 << n
    
    # 2. Also, initialize the DP table: 1, nan, or other values that do not appear as node 
    # indices are appropriate. This DP table will map the tuple containing the resultant bitmask 
    # from traveling to node j to the node one step previous, node i.Also, we can (arbitrarily) start 
    # at node 0, so dp[0][0] = 0, and we can initialize dp[1][0] = 0. This is equivalent to 
    # realizing that at bitmask 1, we had to have come from node 0. 
    dp = [[-1] * n for _ in range(num_states)]
    
    # Basis: path starts at node 0
    dp[1][0] = 0
    
    # 3. Iterate through all the bitmasks and in a nested loop, iterate through each node.
    # Recall that the bitmask simply represents the nodes that have already been visited on our path.
    for mask in range(num_states):
        for i in range(n):

            # 4. Check the DP table for the current bitmask and node i combination. If the 
            # value currently stored in the DP table is $-1$ (or whatever empty value you have 
            # (chosen) we need to skip, as the bitmask is unattainable. This may be slightly 
            # confusing to think about at first, but because we are excluding edges from our graph 
            # (i.e., connections between nodes), there are going to be certain bitmask-object 
            # combinations that lead to invalid results. So, skip to the next bitmask and repeat.
            if dp[mask][i] == -1:
                continue

            # 5. Since we are first iterating through the bitmasks, as we iterate through the 
            # nested loop of nodes we need to verify that node i is actually passed through in 
            # the current bitmask. We can do this by checking that the i-th bit is set in the 
            # current bitmask using the bitwise operators we discussed previously. 
            if mask & (1 << i):

                # 6. Begin looping through the *next* nodes-- another nested loop 
                # iterating through the nodes. Now, we will have node i (the node we are 
                # currently stationed at) and node j (a possible next node to move to).
                for j in range(n):

                # 7. So now we can check if we can see if moving from node i to node j is a valid move:
                    # - We've previously verified that node i appears in the current bit mask.
                    # - Next, we'll need to check that i != j (obviously we can't move from a node to itself)
                    # - Check that node j is not already in the bitmask using the bitwise operators 
                    # (if the j-th bit is already set, it means we've already passed through node j in this bitmask)
                    # - And finally, verify that node i is allowed to connect to node j, using the adjacency matrix
                    if j != i and not (mask & (1 << j)) and adj_matrix[i][j]:

                        # 8. If all these checks are passed, then the connection is valid. Add it to the bitmask and 
                        # the DP table. Simply, the next bitmask will have the j-th bit set, and the DP table will map 
                        # this new mask and node j, back to the previous node i. Recording it like this will make it 
                        # easier to decode the DP table later on an report the Hamiltonian Path we are currently 
                        # working to find.
                        next_mask = mask | (1 << j)
                        dp[next_mask][j] = i

    # 9. Finally, once the nested loops are completed all we need to do is finish the 
    # loop by verifying that the last node i != 0 can in fact connect back to node 0 
    # (the starting point) at the "full" bitmask-- that is, the bitmask of all ones. 
    # If this is the case, terminate the function by returning True (is in a Hamiltonian
    # Cycle through the graph exists) and the DP table. Otherwise, return False and the 
    # DP table. 
    full_mask = num_states - 1

    for i in range(n):
        if dp[full_mask][i] and adj_matrix[i][0]:
            return True, dp
            
    return False, dp


## ===== MAIN FUNCTION =====

# 0. Like we discussed previously in the original SSQ blog post, our function will in 
# take a an adjacency matrix to describe valid connections between nodes, let's call 
# this matrix C. Then, a element C_{ij} represents whether there is a valid path from 
# node i to node j-- 1 means there is a connection, 0 means there is not. 
adj = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

ham_check, dp = find_hamiltonian_cycle(adj)

# --- Construct Hamiltonian Cycle from bitmasks ---
# 1. Our function outputs a boolean variable indicating whether there is a valid Hamiltonian Cycle 
# somewhere in the graph. So, first we will check that it's been set to True in our algorithm. 
# Otherwise, there's no Hamiltonian Cycle and we'll output that as the result.
if ham_check: 

    #2. Set some variables with values we will need:
    # - n = the number of nodes in the graph
    # - The full mask; the bitmask of all 1s that will indicate we have traveled through all the nodes
    # - A flag indicating whether the final was able to loop back to node 0
    n = len(adj)
    final_mask = (1 << n) - 1
    end_node = -1

    # 3. Loop through all the nodes: before we start working backwards through the DP table to 
    # decode the Hamiltonian Cycle it hold, we need to find the final node that the Hamiltonian 
    # Cycle passes through before heading back to node 0. If the DP table of the full mask 
    # (bitmask of all ones indicating we've passed through all the nodes) and the node i is not -1 
    # (i.e., we visit all nodes) and node i can connect to node 0, we'll overwrite the end_node
    # flag with index i. This will tell us the final node i != 0 in the Hamiltonian Cycle.
    for i in range(n):
        if dp[final_mask][i] != -1 and adj[i][0] == 1:
            end_node = i
            break

    # 4. If we make it through this process and the end_node flag is never overwritten with the index of a
    # valid end node, there is no Hamiltonian Cycle and we report as such.
    if end_node == -1: 
        print("No Hamiltonian Cycle")

    # 5. If there is a valid end_node set in our flag, we will proceed decoding the DP table! 
    # First, we'll set some more variables we will need to complete this task:
        # - Initialize an empty list that we will fill in with the node order as we go (we are 
        # going from the final node backwards, so eventually we will reverse the order of this list)
        # - Set the current node to end_node-- this is where we will start (at the end!)
        # - And since we are starting at the end, we will start at the "full" mask (again, the 
        # bitmask of all ones indicating we've passed through all the nodes). 
    else:
        ham_cycle = []
        current_node = end_node
        current_mask = final_mask

        # 6. To actually work our way through the DP table to decode the Hamiltonian we found is 
        # fairly straight forward. Starting from the last node and "full" bitmask, find the 
        # previous node from the DP table. You'll remember from earlier we set up our DP table 
        # to map the tuple of node j and resultant bitmask, to the previous node i we originally 
        # came from (after a series of checks to make sure the transition was valid). 
        # So, it's as simple as just finding the previous node from that fact. Then, we can update 
        # the bitmask (with our bitwise operators) *removing* the current node from the bitmask. 
        # This is what the bitmask looked like when we originally recorded this transition in the 
        # DP table. Now we have the previous node and bitmask we need to repeat this process, 
        # recording the reverse order of the nodes as we go. We'll repeat this until we are at 
        # bitmask 0 (where no nodes have been passed through).
        while current_mask > 0:
            ham_cycle.append(current_node)
            prev_node = dp[current_mask][current_node]
            current_mask = current_mask ^ (1 << current_node) # Remove current node from mask
            current_node = prev_node

        # 7. Reverse the order of the list using Python list operations since we start working 
        # backwards from the last node. Then, for posterity's sake, record that we are ending back at node 0 
        # by appending it to the end of our list. 
        ham_cycle.reverse()
        ham_cycle.append(0)  

        print("Hamiltonian Cycle found:")
        print(" -> ".join(map(str, ham_cycle)))
