import sys

def tsp(cost):
    n = len(cost)
    if n <= 1:
        return cost[0][0] if n == 1 else 0
    
    # maximum cost to visit all cities
    INF = sys.maxsize
    FULL = 1 << n
    fullMask = FULL - 1
    
    # dp[mask][i] represents the minimum cost to visit all cities
    # corresponding to the set bits in 'mask', ending at city 'i'
    dp = [[INF] * n for _ in range(FULL)]
    dp[1][0] = 0
    
    # iterate over all subsets of cities
    for mask in range(1, FULL):
        for i in range(n):
            
            # skip if city i is not included in mask
            if not (mask & (1 << i)):
                continue
            if dp[mask][i] == INF:
                continue
            
            # try to go to every unvisited city j
            for j in range(n):
                
                # skip if city j is already visited
                if mask & (1 << j):
                    continue
                
                # cost to visit new city j from city i
                # such that previously visited cities
                # remain visited
                nxt = mask | (1 << j)
                dp[nxt][j] = min(dp[nxt][j], dp[mask][i] + cost[i][j])
    
    ans = INF
    for i in range(n):
        
        # if last city on path is i and 
        # cost of path is not infinity
        if dp[fullMask][i] != INF:
            
            # update net cost such that city 0 is visited in last
            ans = min(ans, dp[fullMask][i] + cost[i][0])
    
    return ans

if __name__ == "__main__":
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    res = tsp(cost)
    print(res)
