# Python Code to Assign Unique Cap To Every Person
# using Recursion
def dfs(assigned_count, assigned_people, cap, cap_to_people, total_people, num_caps):
    
    # Base case: if all people have a cap assigned, return 1
    if assigned_count == total_people:
        return 1
    
    # If we've considered all caps and not everyone
    # has a cap, return 0
    if cap > num_caps:
        return 0

    # Case: skip the current cap
    ways = dfs(assigned_count, assigned_people, 
               cap + 1, cap_to_people, total_people,num_caps)

    # Assign the current cap to each person who likes it
    for person in cap_to_people[cap]:

        # Check if the person already has a cap assigned
        if not assigned_people[person]:
            
            # Assign current cap to the person
            assigned_people[person] = True
            
            # Recurse with increased assigned count
            ways += dfs(assigned_count + 1, assigned_people, 
                        cap + 1, cap_to_people, total_people,num_caps)
            
            # Backtrack: unassign the cap for other possibilities
            assigned_people[person] = False

    return ways

# Main function to calculate the number
# of ways to assign caps
def number_ways(caps):
    n = len(caps) #people
    # caps = 100
    num_caps = max(map(max, caps))

    # Map each cap to the list of people who prefer it
    cap_to_people = [[] for _ in range(num_caps + 1)]
    for i in range(n): #people
        for cap in caps[i]: #caps allowed by each person
            cap_to_people[cap].append(i)

    # Initialize assigned_people list to track assigned caps
    assigned_people = [False] * n
    
    # Call the recursive function starting from the first cap
    # return dfs(0, assigned_people, 1, cap_to_people, n, num_caps)
    return cap_to_people

if __name__ == "__main__":
  
    caps = [[1, 2, 3], [1, 2], [3, 4], [4, 5]]
    print(number_ways(caps))