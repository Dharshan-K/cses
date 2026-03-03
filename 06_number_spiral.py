n = int(input())
answer = []
maximum = 0

def number_spiral(x,y):
	max_table = max(x,y)
	table_arr = [1]
	temp1 = 0

	if max_table%2 == 0:
		if max_table == x:
			temp1 = max_table*max_table - (y-1)
		else:
			temp1 = (max_table - 1)**2 +x

		
	else:
		if max_table == y:
			temp1 = max_table*max_table - (x-1)
		elif max_table == x:
			temp1 = (max_table-1)**2 + y

	return temp1


for i in range(0,n):
	x, y = map(int, input().split())
	temp = number_spiral(x,y)
	answer.append(temp)


for i in range(0,len(answer)):
	print(answer[i])





	

# number_spiral(5,5)
