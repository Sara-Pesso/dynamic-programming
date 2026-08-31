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
        # # Make sure we are starting at node 0 (node 0 = bin(1) = 0001)
        # if not (mask & 1):
        #     continue
            
        for i in range(n):
            # If current state is unreachable, move on
            if dp[mask][i] == -1:
                continue

            # Look for a preceding node j
            for j in range(n):

                # Check if edge exists and node j is not yet visited in this mask
                if adj_matrix[i][j] == 1 and not (mask & (1 << j)):
                    next_mask = mask | (1 << j)
                    dp[next_mask][j] = i

    # Check if a complete cycle exists back to vertex 0
    final_mask = (1 << n) - 1
    end_vertex = -1

    for u in range(n):
        # Must visit all nodes and have a valid edge back to 0
        if dp[final_mask][u] != -1 and adj_matrix[u][0] == 1:
            end_vertex = u
            break

    # If no end vertex found, no Hamiltonian Cycle exists
    if end_vertex == -1:
        print("No Hamiltonian Cycle exists in this graph.")
        return None

    # --- Reconstruction Path ---
    path = []
    curr_vertex = end_vertex
    curr_mask = final_mask

    print(curr_vertex, curr_mask)

    while curr_mask > 0:
        path.append(curr_vertex)
        prev_vertex = dp[curr_mask][curr_vertex]
        curr_mask = curr_mask ^ (1 << curr_vertex) # Remove current vertex from mask
        curr_vertex = prev_vertex

    path.reverse()
    path.append(0)  # Complete the cycle by returning to the start node

    print("Hamiltonian Cycle found:")
    print(" -> ".join(map(str, path)))
    return path


example_graph = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

has_hamiltonian_cycle(example_graph)