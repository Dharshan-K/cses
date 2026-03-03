n=int(input())

def permutation(num):
	even = []
	odd = []
	answer = []
	for i in range(1,num+1):
		if i % 2 == 0:
			even.append(i)
		else:
			odd.append(i)

	length = max(len(even), len(odd))

	for i in range(0,len(even)):
		answer.append(even[i])

	for i in range(0,len(odd)):
		answer.append(odd[i])

	if len(answer) ==2:
		return "NO SOLUTION"

	for i in range(1,len(answer)-1):
		if answer[i+1] - answer[i] == 1 or answer[i-1] - answer[i] == 1:
			return "NO SOLUTION"

	return answer


result = permutation(n)

if result == "NO SOLUTION":
	print(result)
else:
	print(*result)