num_names = int(input())


def find_first(names, two_letter):
	for name in names:
		if name[0:2] == two_letter:
			return name


while num_names != 0:
	names = []
	two_letters = {}
	for name_i in range(num_names):
		name = input()
		names.append(name)
		if name[0:2] in two_letters:
			two_letters[name[0:2]] += 1
		else:
			two_letters[name[0:2]] = 1
	
	while(len(list(two_letters.keys()))):
		to_print = find_first(names, min(list(two_letters.keys())))
		print(to_print)
		names.remove(to_print)
		if two_letters[min(list(two_letters.keys()))] == 1:
			del two_letters[min(list(two_letters.keys()))]
		else:
			two_letters[min(list(two_letters.keys()))] -= 1
	print()
	num_names = int(input())