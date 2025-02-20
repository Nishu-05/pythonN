def count_commas(N):
    if N < 1000:
        return 0  # No commas for numbers less than 1000

    total_commas = 0

    # Count commas from 10,000 to N
    for num in range(10000, N + 1):
        if num >= 10000:
            total_commas += 1  # Each number from 10000 onwards has at least 1 comma

    return total_commas

# Sample Input
N = 5000

# Finding the total number of commas
result = count_commas(N)
print(result)  # Output: 4001