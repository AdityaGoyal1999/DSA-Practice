

def getMaxWater(heights: list) -> int:
    left = 0
    right = len(heights) - 1
    maxWater = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        maxWater = max(maxWater, width * height)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return maxWater




heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
maxWater = getMaxWater(heights)
print(maxWater == 49)