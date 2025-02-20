def calculate_score(s):
    score = 0
    consecutive_heads = 0

    for char in s:
        if char == 'H':
            score += 2
            consecutive_heads += 1
            # Check for three consecutive heads
            if consecutive_heads == 3:
                break
        elif char == 'T':
            score -= 1
            consecutive_heads = 0  # Reset the counter for heads

    return score

# Sample Input
s = "HHHTT"

# Calculating the final score
result = calculate_score(s)
print(result)  # Output: 6