

def waterTrapped(heights: list) -> int:
    left = 0
    right = len(heights) - 1
    leftMax = 0
    rightMax = 0
    water = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] < leftMax:
                water += leftMax - heights[left]
            else:
                leftMax = heights[left] 
            left += 1
        else:
            if heights[right] < rightMax:
                water += rightMax - heights[right]
            else:
                rightMax = heights[right]

            right -= 1

    return water
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
result = 6

print(waterTrapped(heights) == result)