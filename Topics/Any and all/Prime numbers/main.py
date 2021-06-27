prime_numbers = [2, 3, 5, 7, 11, 13, 17]
i = 18
while i < 1001:
    if any(i % j == 0 for j in range(2, i - 1)):
        i += 1
    else:
        prime_numbers.append(i)
        i += 1
