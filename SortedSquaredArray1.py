def sorted_squared(array):
    squared = [x ** 2 for x in array]
    return sorted(squared)

result = sorted_squared([2, -9,2 ])
print(result)
