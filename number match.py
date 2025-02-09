def determine_winner(n, arr):
    from collections import Counter

    # Count occurrences of each number
    counts = Counter(arr)

    team_a_support = 0
    team_b_support = 0

    for num, count in counts.items():
        if num % 2 == 0:  # Even number
            if count % 2 == 0:
                team_a_support += num * count  # Supports team A
            else:
                team_b_support += num * count  # Supports team B
        else:  # Odd number
            if count % 2 == 0:
                team_b_support += num * count  # Supports team B
            else:
                team_a_support += num * count  # Supports team A

    # Determine the winner or tie
    if team_a_support > team_b_support:
        return f"A {team_a_support}"
    elif team_b_support > team_a_support:
        return f"B {team_b_support}"
    else:
        return "T 0"

# Sample Input
n = 6
arr = [1, 2, 2, 3, 4, 4]

# Finding the winner
result = determine_winner(n, arr)
print(result)  # Output: "A 4"