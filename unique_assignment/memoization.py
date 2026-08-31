from collections import defaultdict

def count_perms(hats):
    mappings = defaultdict(list)
    for i, prefs in enumerate(hats):
        for hat in prefs:
            mappings[hat].append(i)
    mappings = list(mappings.items())
    # print(mappings)

    num_ppl = len(hats)
    num_hats = max(max(h) for h in hats)

    fin = (1 << num_ppl) - 1 #all 1 = successful permutation

    # Initialize memoization table
    dp = [[0] * (1 << num_ppl) for _ in range(num_hats + 1)]

    def dfs(idx, mask):
        if mask == fin: # i.e., everyone has a hat
            return 1 # add 1 to the count

        if idx == len(mappings):
            return 0 # i.e., at least 1 person doesn't have a hat, but we're at the last hat so this perm doesn't work

        # Check memoization table for this result. If it's there, skip dfs and move on!
        if dp[idx][mask] != 0:
            return dp[idx][mask]

        num_perms = dfs(idx + 1, mask) # skip current hat

        # look at all the assignments for this hat
        for node in mappings[idx][1]:
            #if the node is already assigned an obj, move to next node
            if mask & (1 << node):
                continue

            # if the node hasn't been assigned an obj yet,
            # try assigning it an obj
            num_perms += dfs(idx + 1, mask|(1 << node))

        dp[idx][mask] = num_perms
        return num_perms

    return dfs(0,0), dp #Initial state: hat zero, zero people assigned hats. Also return the memo table

# hats = [[0, 1, 2], [0, 1], [2, 3], [3, 4]]
hats = [[0, 1, 2], [0, 1]]
res = count_perms(hats)
print(res[0])
print(res[1])