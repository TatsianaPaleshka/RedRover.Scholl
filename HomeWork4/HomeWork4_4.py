# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
from functools import reduce
my_list = [20, -3, 15, 2, -1, -21]
result = reduce(lambda x, y: x * y, my_list)
print(result)
