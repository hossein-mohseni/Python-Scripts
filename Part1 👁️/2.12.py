# Define lists for base and exponent
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

# Compute the result for each (a, b) pair using a loop
r = []
for i in range(len(a)):
    r.append(a[i] ** b[i])

# Display the results using formatted strings with color and style
print("\033[96m{:<5}\033[0m\033[95m{:<5}\033[0m\033[94m{}\033[0m".format("a", "b", "a ** b"))
for i in range(len(a)):
    print("\033[92m{:<5}\033[0m\033[93m{:<5}\033[0m\033[91m{}\033[0m".format(a[i], b[i], r[i]))
