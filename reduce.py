from functools import reduce
import math

print(reduce(max, [34, 21, 99, 67, 10]))

print(list(filter(lambda x: x > 50, [34, 65, 10, 100])))
print(list(map(math.sqrt, [9, 25, 36])))
