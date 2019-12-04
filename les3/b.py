import sys

OUTPUT_FILE_NAME = 'result.txt'

input_file_name = sys.argv[1]

input_file = open(input_file_name, 'r')

lines = input_file.readlines()

lines = list(map(lambda x: list(map(lambda y: int(y), x.split())), lines))

result = []

for line in lines:
	result_line = []

	fizz, buzz, third = line
	
	for num in range(1, third + 1):
		f = num%fizz==0
		b = num%buzz==0

		if(f):
			result_line.append('F')
		elif(b):
			result_line.append('B')
		elif(f and b):
			result_line.append('FB')
		else:
			result_line.append(num)

	result.append(result_line)

output_file = open(OUTPUT_FILE_NAME, 'w+')

for line in result:
	output_file.write('{0}\n\n'.format(str(line)))

output_file.close()