"""
You are given n steps and you can either take 1 or 2 steps.
"""

def numWaysClimb(n):
    
    memo = {0: 1, -1: 0}

    def recurse(stairs):
        if stairs in memo:
            return memo[stairs]
        else:
            memo[stairs] = recurse(stairs-1) + recurse(stairs-2)
            return memo[stairs]
    
    return recurse(n)

print(numWaysClimb(2) == 2)
print(numWaysClimb(3) == 3)