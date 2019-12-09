import sys
import re

input_file_name = sys.argv[1]

input_file = open(input_file_name, 'r')
# text = input_file.read().split(".", maxsplit = 8)


def new_text(input_file):
	return([str[1] for i in input_file.replace('.', 'KDSGJKDNGJNDJKBDNFKJBNF!').split()])

print(input_file)