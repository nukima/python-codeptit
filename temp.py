# list_num = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# ele_count = {}
# for element in list_num:
#    ele_count[element] = list_num.count(element)

# for key in ele_count.keys():
#     if(ele_count[key] >= 3):
#         print(key)

# a = ("apples", "bananas", "oranges")
# print(id(a))
# a = ("test", "bananas", "oranges")
# print(id(a))

# list_num = range(1, 11)
# count = 0
# for num in list_num:
#     flag = False
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 flag = True
#                 break
#     if flag:
#         count += 1

# print(count)

# ---------------------
# diem = float(input())
# if diem >= 0 and diem < 4 :
#     print('D')
# elif diem >= 4 and diem < 6:
#     print('C')
# elif diem >= 6 and diem < 8:
#     print('B')
# elif diem >= 8.5 :
#     print('A')

#--------------------

# day_so = [2, 3, 5, 7, 11, 13]
# chan = 0
# le = 0
# for so in day_so:
#     if so % 2 == 0:
#         chan += 1
#     else:
#         le += 1

# print(chan, le)
#-------------------------

# L = [0,3,5,151,10,13]
# for so in L:
#     if so > 150:
#         break
#     if so % 5 == 0:
#         print(so)

# -------------------

# for i in range(1, 10):
#     if(i == 1):
#         print('1st')
#     if(i == 2):
#         print('2nd')
#     if(i == 3):
#         print('3rd')
#     else:
#         print(f"{i}th")
#------------------------

# list1 = ['abca', '1221', 'xyz', 1221]
# count = 0
# for ele in list1:
#     if len(ele) > 2 and ele[0] == ele[-1]:
#         count += 1
# print(count)
# ------------------

# thisdict = {
#   "name": "Manh",
#   "ID": "B19DCCN420",
#   "class": "D19CQCN12-B"
# }
# print(thisdict)

# thisdict["subject"] = "Python"

# print(thisdict)
# --------------------

# list1 = ['a', 1, 1, 'b', 4, 4, 'a', 2]
# result = {}

# for ele in list1:
#     result[ele] = list1.count(ele)

# print(result)
#--------------------

# thisdict = {}
# for i in range(1, 16):
#     thisdict[i] = i * i

# print(thisdict)
# -----------

# thisdict = {1 : 'a', 2 : 2, 3 : 2.25, 4 :'d'}
# sum = 0
# for value in thisdict.values():
#     if type(value) == int or type(value) == float:
#         sum += value

# print(sum)

# list_word = ['abcda', '123', 'xyyz', 'heheh', 1221]

# for word in list_word:
#     tmp = str(word)
#     if len(tmp) > 2 and tmp[0] == tmp[-1]:
#         print(tmp)

# list1 = [6, 9]
# result = []
# n = 4
# for ele in list1:
#     for i in range(1, n + 1):
#         tmp = str(ele) + str(i)
#         result.append(tmp)

# print(result)

# #-------------------

# list_num = [38, 12, 55]
# list_num.sort(reverse=True)
# result = ''
# for num in list_num:
#     result += str(num)
# print(result)
# #-------------------
# txt = input().split()
# NUM_ROWS = int(txt[0])
# a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]
# txt = input().split()
# i, j = int(txt[0]), int(txt[1])
# for k in range(NUM_ROWS):
#     a[k][i], a[k][j] = a[k][j], a[k][i]
# for row in a:
#     print(' '.join([str(i) for i in row]))
#------------
# counter = {}
# for i in range(int(input())):
#     line = input().split()
#     for word in line:
#         counter[word] = counter.get(word, 0) + 1

# for i in counter.items():
#     print(i)
#----------------
# tudien = {}
# for i in range(int(input())):
#     txt = input()
#     txt = [i.strip() for i in txt.split('-')]
#     words = [i.strip() for i in txt[1].split(',')] #['malum', 'pomum', 'popula']
#     for word in words:
#         if word in tudien:
#             tudien[word].append(txt[0])
#         else:
#             tudien[word] = [txt[0]]

# for l, e in sorted(tudien.items()):
#     print(f"{l} - {', '.join(e)}")
#------------
# Python3 program to implement Shortest Remaining Time First
# Shortest Remaining Time First (SRTF)

# Function to find the waiting time
# for all processes
def findWaitingTime(processes, n, wt):
	rt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rt[i] = processes[i][1]
	complete = 0
	t = 0
	minm = 999999999
	short = 0
	check = False

	# Process until all processes gets
	# completed
	while (complete != n):
		
		# Find process with minimum remaining
		# time among the processes that
		# arrives till the current time`
		for j in range(n):
			if ((processes[j][2] <= t) and
				(rt[j] < minm) and rt[j] > 0):
				minm = rt[j]
				short = j
				check = True
		if (check == False):
			t += 1
			continue
			
		# Reduce remaining time by one
		rt[short] -= 1

		# Update minimum
		minm = rt[short]
		if (minm == 0):
			minm = 999999999

		# If a process gets completely
		# executed
		if (rt[short] == 0):

			# Increment complete
			complete += 1
			check = False

			# Find finish time of current
			# process
			fint = t + 1

			# Calculate waiting time
			wt[short] = (fint - proc[short][1] -
								proc[short][2])

			if (wt[short] < 0):
				wt[short] = 0
		
		# Increment time
		t += 1

# Function to calculate turn around time
def findTurnAroundTime(processes, n, wt, tat):
	
	# Calculating turnaround time
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]

# Function to calculate average waiting
# and turn-around times.
def findavgTime(processes, n):
	wt = [0] * n
	tat = [0] * n

	# Function to find waiting time
	# of all processes
	findWaitingTime(processes, n, wt)

	# Function to find turn around time
	# for all processes
	findTurnAroundTime(processes, n, wt, tat)

	# Display processes along with all details
	print("Processes Burst Time	 Waiting",
					"Time	 Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t",
				processes[i][1], "\t\t",
				wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = ", total_tat / n)
	
# Driver code
if __name__ =="__main__":
	
	# Process id's
	proc = [[1, 12, 2], [2, 11, 0],
			[3, 7, 2], [4, 15, 3], [5, 8, 4]]
	n = 5
	findavgTime(proc, n)
	
# This code is contributed
# Shubham Singh(SHUBHAMSINGH10)
