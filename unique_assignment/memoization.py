from collections import defaultdict

def assignment_permutations(objs):
    # 0. First, we need to turn our input LOLs (which maps node $i$ to allowed objects)
    # into a list of dictionaries that maps each *object* to those nodes which it 
    # is allowed to be assigned.
    obj_to_node = defaultdict(list)
    for i, allowed_objs in enumerate(objs):
        for obj in allowed_objs:
            obj_to_node[obj].append(i)
    obj_to_node = list(obj_to_node.items())

    # 1. Initialize memoization (DP) table and final bitmask
    # Find the number of nodes to which we will assign objects.
    n = len(objs)

    # Also need to define our stop criteria. All ones in our bitmask 
    # means that every node has been assigned (an allowed) object. So, we know we
    # can break out of our loop.
    fin = (1 << n) - 1 

    # Initial DP Table
    dp = {}


    def dfs(i, mask):
        # 1. Check if every node has successfully been assigned an object.
        # If so, return 1 (adding 1 to our successful permutations count)
        if mask == fin:
            return 1

        # 2. If the bitmask is not full, but the current object index is n+1, return 0. 
        # This means we have iterated through all n objects, but at least one node is still not assigned. 
        # So, we do not have a successful permutation, and we add nothing to the count.
        if i == len(obj_to_node):
            return 0 

        # 3. Check the memoization (DP) table to see if we've completed this subproblem before. 
        # Recall the DP table is storing the current object index being assigned at the 
        # current bitmask to the running count of possible permutations after that 
        # combination. So, checking for the already solved subproblem and returning that 
        # result instead of recursing:
        if (i, mask) in dp:
            return dp[(i, mask)]

        # 4. DFS Skip! We do this so we can see if we can assign an object to every node without
        # this particular object. This way we can get accurate counts for all P(n,k) permutations.
        # (this notation means "choose $k$ objects from $n$ total objects, where the order matters).
        # Note: this step really only matters if there are less nodes than objects! In the case
        # of the SSQ, this step is moot, but doesn't do any harm.
        # This is also how we can start tracking the *total* number of permutations possible!
        num_perms = dfs(i + 1, mask) 

        # 5. DFS: Loop through each object and then in a nested loop, loop through all the nodes
        # to which that object is able to be assigned. 
        for node in obj_to_node[i][1]:
            # a. If the current node is already assigned (i.e., the corresponding 
            # bit in our mit mask is already set to 1), skip to the next node. 
            if mask & (1 << node):
                continue

            # b. If the current node hasn't yet been assigned an object (i.e., the corresponding bit 
            # is a 0 in the current bitmask), assign the current object and then update the bitmask by 
            # setting the node's bit to 1.
            new_mask =  mask|(1 << node)

            # c. Recurse by running the DFS step again, moving on to the next object's 
            # index and the new bitmask (keeping track of which nodes have already been 
            # assigned in our callstack)
            num_perms += dfs(i + 1, new_mask)

        dp[(i, mask)] = num_perms
        return num_perms
    
    # 7. Finally, once DFS is complete the function terminates, returning the total 
    # number of possible permutation, the memoization table, and our object-to-node 
    # list of dictionaries.
    return dfs(0,0), dp, obj_to_node 

### ==== MAIN FUNCTION ====
objs = [[0, 1, 2], 
        [2, 3], 
        [0, 1], 
        [3, 4]]

count, dp, mappings = assignment_permutations(objs)

### ==== EXTRACT UNIQUE ASSIGNMENT ====

# 1. First, make sure there is at least one solution.
if dp[(0,0)] == 0: 
    print("There is no unique assignment of objects to the nodes in this matrix.")

else: 
    # 2. If there is at least one unique assignment solution, we'll need to grab the 
    # number of objects. We will also initialize our bitmask to 0 
    # (i.e., nothing is assigned).
    # And, again define the "full mask"-- a bitmask of all ones we'll use as our stopping criteria. 
    num_objs = max(map(max, objs)) 
    current_mask = 0
    full_mask = (1 << num_objs) - 1

    # 3. Initialize a dictionary to hold the assignment pairings
    assignments = {}

    # 4. Begin looping thru the index of each object
    for i in range(num_objs):

        # 5. Set a flag that will indicate whether this object is assigned. If it 
        # happens that this object is assigned to some node in the assignment 
        # permutation being mapped from the DP table, this flag will be set to True.
        # When the loop moves on to object i+1, this flag will be reset to False. 
        assigned_obj = False

        # 6. Attempt to assign object i to some node j by looping through each allowed node 
        # in the object-to-node mapping derived from the user defined input matrix. By comparing 
        # these to the number of possible permutations counted up after each bitmask (which we 
        # have mapped in the memoization/DP table), we can determine if node j is actually a 
        # viable pairing for object $i$. For example, if we see that in the object-to-node map 
        # object i is allowed to be assigned to node $j$ and this assignment can lead to viable 
        # permutations via the DP table, we can report it in our final assignment. But, if the 
        # DP table indicates there are 0 ways to make a viable full assignment after assigning 
        # object i to node j, we can not do it.
        for j in mappings[i][1]: 

            # a. Verify node j is not already assigned in the current mask (i.e., make sure the 
            # jth bit is 0)
            if not (current_mask & (1 << j)):

                # b. Compare assigning object i to node j in the current bitmask, to viable 
                # assignments for object i+1 in the next bitmask (assuming that we continue 
                # with this particular assignment). If the next mask is the full mask, then we 
                # don't need (or have to) assign any more objects to nodes. Then, verify that 
                # the number of possible permutations counted after object i+1 and the new 
                # bitmask stored in the DP table is greater than 0 (i.e., there is at least one 
                # path to a complete assignment).
                new_mask = current_mask | (1 << j)
                if new_mask != full_mask:
                    if dp[(i + 1, new_mask)]:

                        # c. Assuming all these checks are passed, assign object i to node j in 
                        # the dictionary, move on to evaluating the new bitmask, and switch the 
                        # flag to False. Finally, break out of the loop and move on to object i+1.
                        assignments[j] = i
                        current_mask = new_mask
                        assigned_obj == True
                        break

                # d. If the new mask is the bitmask of all ones (the full mask), make the final 
                # assignment and break out if the loop.
                else: 
                    assignments[j] = i
                    break

        # e. For the sake of saving a bit of speed, if we've reached the full mask and previous object was 
        # able to be assigned, we are done and can break out of the nested loops. 
        if assigned_obj and current_mask == full_mask:
            break

## ==== FINAL SOLUTION! ====
for i in assignments:
    print(f"Node {i} --> Object {assignments[i]}")



        
    


