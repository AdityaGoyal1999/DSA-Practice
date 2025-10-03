"""
Merge 2 sorted arrays.
"""


# O(n + m)
# O(1) auxillary and only O(n+m) for outputting the result
def mergeArrays(nums1: list, nums2: list) -> list:
    
    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    # These are more space consuming that a simple iteration
    # result.extend(nums1[i:])
    # result.extend(nums2[j:])

    while i < len(nums1):
        result.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        result.append(nums2[j])
        j += 1

    return result


nums1 = [1, 2, 3, 4]
nums2 = [2, 3, 4, 5]

print(mergeArrays(nums1, nums2))