from math import nan
def has_hamiltonian_cycle(adj_matrix):
    # number of nodes
    n = len(adj_matrix)
    
    # Total combinations of nodes is 2^n
    num_states = 1 << n
    
    # dp[mask][i] initialization
    # dp[mask][i] = visits the nodes in mask, starting at node 0, ending at node i
    dp = [[-1] * n for _ in range(num_states)]
    
    # Basis: path starts at node 0
    # Because bin(1) = 0001 therefore, we start and end at node 0 for this path
    dp[1][0] = 0
    
    # Iterate through all masks (subsets of nodes)
    for mask in range(num_states):
        for i in range(n):
            # If the current state is unreachable, skip it
            if dp[mask][i] == -1:
                continue
            
            # Make sure node i is part of the current mask
            if mask & (1 << i):

                # Look for a next node j
                for j in range(n):

                    # j must not be in the mask, distinct from i, and connected to i
                    if j != i and not (mask & (1 << j)) and adj_matrix[i][j]:
                        

                        # If a valid path ended at j -> i
                        next_mask = mask | (1 << j)
                        dp[next_mask][j] = i

    # Check if we can complete the cycle back to node 0 from any ending node i
    full_mask = num_states - 1

    for i in range(n):
        if dp[full_mask][i] and adj_matrix[i][0]:
            return True, dp
            
    return False, dp

adj = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

ham_check, dp = has_hamiltonian_cycle(adj)

# --- Construct Hamiltonian Cycle from bitmasks ---
if ham_check: # i.e., there exists a hamiltonian cycle somewhere in this graph
    n = len(adj)
    final_mask = (1 << n) - 1
    end_node = -1
    for i in range(n):
        # Needs to visit all nodes and connect to node 0
        if dp[final_mask][i] != -1 and adj[i][0] == 1:
            end_node = i
            break

    if end_node == -1: 
        print("No Hamiltonian Cycle")

    else:
        path = []
        curr_vertex = end_node
        curr_mask = final_mask

        while curr_mask > 0:
            path.append(curr_vertex)
            print(curr_vertex)
            prev_vertex = dp[curr_mask][curr_vertex]
            curr_mask = curr_mask ^ (1 << curr_vertex) # Remove current vertex from mask
            curr_vertex = prev_vertex

        path.reverse()
        path.append(0)  # Complete the cycle by returning to the start node

        print("Hamiltonian Cycle found:")
        print(" -> ".join(map(str, path)))
        # return path