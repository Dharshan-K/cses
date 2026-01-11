def repetitions(string):
	maximum = 0
	count = 0
	for i in range(0,len(string)-1):
		if string[i] == string[i+1]:
			count = count+1
		else:
			if count >= maximum:
				maximum = count + 1
			count = 0

	if count >= maximum:
		maximum = count + 1
	return maximum

string = str(input())
print(repetitions(string))
