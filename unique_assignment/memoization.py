from collections import defaultdict

def count_perms(objs):
    # 0. Determine the number of objects to be assigned and the number of people to assign to 
    mappings = defaultdict(list)
    for i, prefs in enumerate(objs):
        for obj in prefs:
            mappings[obj].append(i)
    mappings = list(mappings.items())

    num_ppl = len(objs)

    # Also need to define our stop criteria. All 1s in our bitmask means that every person
    # has been assigned one of their allowable objects. 
    fin = (1 << num_ppl) - 1 #all 1 = successful permutation

    # 1. Initialize memoization (DP) table
    dp = {}


    def dfs(idx, mask):
        if mask == fin: # i.e., everyone has a object
            return 1 # add 1 to the count

        if idx == len(mappings):
            return 0 # i.e., at least 1 person doesn't have a object, but we're at the last object so this perm doesn't work

        # Check memoization table for this result. If it's there, skip dfs and move on!
        # if dp[idx][mask] != 0:
        if (idx, mask) in dp:
            return dp[(idx, mask)]

        num_perms = dfs(idx + 1, mask) # skip current object

        # look at all the assignments for this object
        for node in mappings[idx][1]:
            #if the node is already assigned an obj, move to next node
            if mask & (1 << node):
                continue

            # if the node hasn't been assigned an obj yet,
            # try assigning it an obj
            new_mask =  mask|(1 << node)
            num_perms += dfs(idx + 1, new_mask)


        dp[(idx, mask)] = num_perms
        return num_perms

    return dfs(0,0), dp, mappings #Initial state: object zero, zero people assigned objects. Also return the memo table

### ==== MAIN FUNCTION ====
objs = [[0, 1, 2], 
        [2, 3], 
        [0, 1], 
        [3, 4]]

count, dp, mappings = count_perms(objs)

### ==== EXTRACT UNIQUE ASSIGNMENT ====

if dp[(0,0)] == 0: 
    print("There is no unique assignment of objects to the nodes in this matrix.")

else: # i.e., there is at least one unique assignment solution

    # Number of nodes
    num_objs = max(map(max, objs)) 

    # Start with nothing assigned
    current_mask = 0
    # Stop criteria is when we assign everyone. So, stop at
    full_mask = (1 << num_objs) - 1

    # Initialize something to hold the assignment pairings
    assignments = {}

    for i in range(num_objs):
        # If all nodes are assigned an object, break out of loops
        if current_mask == full_mask:
            break

        # # If we can complete assigning all nodes an objects without this obj, skip it
        # if dp[(i, current_mask)] > 0: 
        #     continue #skip on to next i

        # Else, assign this object to a node
        assigned_obj = False

        # Try assigning object i
        for j in mappings[i][1]: # List of nodes object i can be assigned to
            if not (current_mask & (1 << j)): # Check node j is not assigned in this mask
                # Check if object i+1 (the next) can be assigned in a future mask
                new_mask = current_mask | (1 << j)
                if new_mask != full_mask:
                    if dp[(i + 1, new_mask)]:
                        assignments[j] = i
                        current_mask = new_mask
                        assigned_obj == True
                        break
                else: # new_mask == full_mask (i.e., we're done!- just need to assign last node)
                    assignments[j] = i
                    break

        if assigned_obj and current_mask == full_mask:
            break

# Print out a unique solution!
print(assignments)



        
    


