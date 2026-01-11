n = int(input())
numbers = list(map(int, input().split()))

def increasingArray(numbers):
	moves = 0
	maximum = 0
	for i in range(0,n):
		if numbers[i] < maximum:
			moves = moves + (maximum - numbers[i])
		if numbers[i] > maximum:
			maximum = numbers[i]

	return moves

print(increasingArray(numbers))