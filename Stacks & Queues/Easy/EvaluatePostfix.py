"""
Evaluate postfix operation.

Example: 23+ -> 5

Solution -> Use stack. Given the expression will be valid, operator will act upon 2 operands.

Constraint: Operations: +, -, /, * and 0-9 numbers in the string.
"""

# O(1)
# O(1)
def evaluate(first: int, second: int, operator: int) -> int:
    if operator == "/":
        # This is different from first // second -> rounds to 0
        return int(first / second) # synonymous with floor operation
    elif operator == "*":
        return first * second
    elif operator == "+":
        return first + second
    else:
        return first - second


# O(n)
# O(n)
def postfixCalculation(s: str) -> int:
    stack = []

    for c in s:
        if c in "*-/+":
            second = stack.pop()
            first = stack.pop()

            stack.append(evaluate(first, second, c))
        else:
            stack.append(int(c))
    
    return stack[-1]

print(postfixCalculation("23+"))