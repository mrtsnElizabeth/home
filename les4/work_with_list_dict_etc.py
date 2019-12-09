# 1
list_a = [-58, -31, 0, 1, 4, 6, 89]
list_b = [x for x in list_a]
print(list_b)
print(list_a is list_b)

# 2
list_a = [-58, -31, 0, 1, 4, 6, 89]
list_b = [x for x in list_a if x % 2 == 0]
print(list_b)

# 3
list_a = [-58, -31, 0, 1, 4, 6, 89]
list_b = [x for x in list_a if x % 2 == 0 and x > 0]

# 4
list_a = [-58, -31, 0, 1, 4, 6, 89]
list_b = [x**2 for x in list_a]
print(list_b)

# 5
list_a = ['cat', 'chill', 'football']
list_b = [len(x) for x in list_a]
print(list_b)

# 6
list_a = [-58, -31, 0, 1, 4, 6, 89]
list_b = [x if x < 0 else x**2 for x in list_a]
print(list_b)

# 7
list_a = [-58, -31, 0, 1, 4, 6, 89]
list_b = [x**3 if x < 0 else x**2 for x in list_a if x % 2 == 0]
print(list_b)

# 8
numbers = range(10)

squared_evens = [n**2 for n in numbers if n % 2 == 0]

squared_evens = [
	n ** 2
	for n in numbers
	if n % 2 == 0
]

print(squared_evens)

# 9
numbers = range(10)
squared_evens = []
for n in numbers:
	if n % 2 == 0:
		squared_evens.append(n**2)
print(squared_evens)

# 10
numbers = range(10)
squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
print(squared_evens)
print(list(squared_evens))

# 11
list_a = [-58, -31, 0, 1, 4, 6, 89]
my_gen = (i for i in list_a)
print(next(my_gen))
print(next(my_gen))

# 12
list_a = [-58, -31, 0, 1, 4, 6, 89]
my_gen = (i for i in list_a)
my_list = list(my_gen)
print(my_list)

# 13
list_a = [-58, -31, 0, 1, 4, 6, 89]
my_list = list(i for i in list_a)
print(my_list)

# 14
list_a = [-58, -31, 0, 1, 4, 6, 89]
my_list = [i for i in list_a]
print(my_list)

# 15
list_a = [-58, -31, 0, 1, 4, 6, 89]
my_set = {i for i in list_a}
print(my_set)

# 16
dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
dict_123 = {v: k for k, v in dict_abc.items()}
print(dict_123)

# 17
list_a = [-58, -31, 0, 1, 4, 6, 89]
dict_a = {x: x**2 for x in list_a}
print(dict_a)

# 18
list_a = [-58, -31, 0, 1, 4, 6, 89]
my_str = ''.join(str(x) for x in list_a)
print(my_str)

# 19
list_a = [-58, -31, 0, 1, 4, 6, 89]
list_b = [(i, x) for i, x in enumerate(list_a)]
print(list_b)

# 20
list_a = [-58, -31, 0, 1, 4, 6, 89]
list_b = [x for i, x in enumerate(list_a, 1) if i % 3 == 0]
print(list_b)

# 21
first_ten_even = [(i, x) for i, x in enumerate(range(10)) if x % 2 == 0]
print(first_ten_even)

# 22
import itertools
first_ten = (itertools.islice((x for x in range(1000000000) if x % 2 == 0), 10))
print(list(first_ten))

# 23
rows = 1, 2, 3
cols = 'a', 'b'
my_dict = {(col, row): 0 for row in rows for col in cols}
print(my_dict)

# 24
rows = 1, 2, 3, -60, -71
cols = 'a', 'b', 'mmm'

my_dict = {
	(col, row): 0
	for row in rows if row > 0
	for col in cols if len(col) == 1
}
print(my_dict)

# 25
matrix = [[0, 2, 8, 100],
	[10, 22, 88, 888],
	[56, 90, 999, 1234]]

flattened = [n for row in matrix for n in row]
print(flattened)

# 26
w, h = 5, 3
matrix = [[0 for x in range(w)] for y in range(h)]
print(matrix)

# 27
# Общий синтаксис:
# [[expression for y in x] for x in iterator]
# Применение: Обходим двумерную структуру данных,
# сохраняя результат в другую двумерную структуру.

matrix = [[1, 2, 3, 4], 
	[5, 6, 7, 8], 
	[9, 10, 11, 12]]

squared = [[cell**2 for cell in row] for row in matrix]
print(squared)

# 28
list_a = [x for x in range(-2, 4)]
list_b = [x**2 for x in list_a]
print(list_b)

# 29
list_c = [x**2 for x in [x for x in range(-2, 4)]]
print(list_c)

# 30
# Преимущество от комбинирования генераторов
# на примере сложной функции f(x) = u(v(x))
list_c = [t + t ** 2  for t in (x ** 3 + x ** 4 for x in range(-2, 4))]
print(list_c)

# 31
import itertools
l1 = [1, 2, 3]
l2 = [15, 88, 91]
result = [l*2 for l in itertools.chain(l1,l2)]
print(result)

# 32
matrix = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]]

# варіант 1

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

# варіант 2

transposed = []
for i in range(len(matrix[0])):
	new_row = []
	for row in matrix:
		new_row.append(row[i])
	transposed.append(new_row)
print(transposed)

# варіант 3

transposed = list(map(list, zip(*matrix)))
print(transposed)

# 33
days = [d for d in range(1, 32)]
weeks = [days[i:i+7] for i in range(0, len(days), 7)]
print(weeks)

work_weeks = [week[0:5] for week in weeks]
print(work_weeks)

w_days = [item for sublist in work_weeks for item in sublist]
print(w_days)