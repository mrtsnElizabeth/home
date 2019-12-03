# тут треба довиправляти,
# помилку не видає. хз, що не так роблю
# командний рядок відкриває, закриває файл,
# нічого не пише абсолютно
# купу варіантів спробувала з інтернету:
# початок починає працювати,
# тільки щось допишу, 0 реакції

def doc_with_nums(nums):
	infile = open('nums.txt', 'r')
	infile.readline()
	f = []
	b = []
	n = []
	for line in infile:
		nums = line.split()
		f.append(int(nums[0]))
		b.append(int(nums[1]))
		n.append(int(nums[2]))
	infile.close()
	return f, b, n

	for i in range (1, 1+n):
		if i%f == 0 and i%b == 0:
			print('FB')
		elif i%f == 0:
			print('F')
		elif i%b == 0:
			print('B')
		else:
			print(i)
	print(' ')