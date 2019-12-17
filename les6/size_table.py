lingerine_international = {
"XXS": ['63-65', '89-92', '42', '36', '8', '38', '24'],
"XS": ['66-69', '93-96', '44', '38', '10', '40', '26'],
"S": ['70-74', '97-101', '46', '40', '12', '42', '28'],
"M": ['75-78', '102-204', '48', '42', '14', '44', '30'],
"L": ['79-83', '105-108', '50', '44', '16', '46', '32'],
"XL": ['84-89', '109-112', '52', '46', '18', '48', '34'],
"XXL": ['90-94', '113-117', '54', '48', '20', '50', '36'],
"XXXL": ['95-97', '118-122', '56', '50', '22', '52', '38']}

first_ph = input("Enter your international size (for example: S): ")
first_ph = first_ph.upper()

second_ph = input("\nIf you want to know waist and hip sizes, print 1.\nIf you want to know sizes of other countries, print 2.\nIf you want to know all of this, print 3.\nEnter: ")

result = lingerine_international[first_ph][0]
result_two = lingerine_international[first_ph][1]
size_rus = lingerine_international[first_ph][2]
size_ge = lingerine_international[first_ph][3]
size_usa = lingerine_international[first_ph][4]
size_fr = lingerine_international[first_ph][5]
size_uk = lingerine_international[first_ph][6]

if second_ph is "1":
	print("\nFor your size waist size is: " + result + ".\nFor your size hip size is: " + result_two + ".")

elif second_ph is "2":
	print("\nRussian: " + size_rus + "\nGerman: " + size_ge + "\nUSA: " + size_usa + "\nFrance: " + size_fr + "\nUK: " + size_uk)

elif second_ph is "3":
	print("\nFor your size waist size is: " + result + ".\nFor your size hip size is: " + result_two + ".")
	print("\nRussian: " + size_rus + "\nGerman: " + size_ge + "\nUSA: " + size_usa + "\nFrance: " + size_fr + "\nUK: " + size_uk)

else:
	print("\nError!!! Try again!")