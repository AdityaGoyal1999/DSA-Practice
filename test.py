# Convert decimal num to binary

def decimal2Binary(num: int) -> str:
    
    res = []

    while num > 0:
        bit = num % 2
        res.append(str(bit))
        num = num // 2
    
    return ''.join(res[::-1])


print(decimal2Binary(27))

def binary2Decimal(num: str) -> int:

    res = 0
    power = 0
    for i in range(len(num)-1, -1, -1):
        if num[i] == "1":
            res += 2**power
        power += 1
    
    return res

print(binary2Decimal("11011"))