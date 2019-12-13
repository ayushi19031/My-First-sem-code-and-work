import numpy as np
''' linalg.norm'''
no_of_col = int(input("n: "))
no_of_rows = int(input("m: "))

A_ = np.array([[1, 4, 4, 5], [2, 5, 6, 6], [3, 6, 7, 8]])

# for i in range(no_of_rows):
# 	rowi = []
# 	for j in range(no_of_col):
# 		rowi.append(float(input("entry: ")))
# 	A_.append(rowi)

A = np.array(A_)
Q_1 = []
Q = []
'''[
[1, 4],
[2, 5],
[3, 6]
]
for j i
u = [3, 6]
if i am using column no2:
	for k in range(2):
		[3, 6] - numpy.dot(matrix[k], matrix[2])*matrix[k]//np.dot(matrix[2], matrix[2])
		OR
listy = work_A[0]
Q.append(listy)
for i in range(1, no_of_col):
	lum = work_A[i] - (numpy.dot(Q[i - 1], work_A[i])/np.dot(Q[i-1],Q[i - 1]))*Q[i - 1] 
	Q.append(listy - )
'''
work_A = A.transpose()
for num in A:
	num = np.array(num)
listy = work_A[0]
Q.append(listy/np.linalg.norm(listy))
for i in range(no_of_col):
	t = np.array(work_A[i][:])
	# 
	# for j in range(i):
	# 	work_A[j] = np.array(work_A[j])
	# 	listy = listy - np.dot(t, )
	for i in range(1, no_of_col):
		#lum = work_A[i] - (np.dot(Q[i - 1], work_A[i])/np.dot(Q[i-1],Q[i - 1]))*Q[i - 1]
		lum = work_A[i][:]
		j = i
		while j >  0:
			j = j - 1
			lum = lum -  np.dot(Q[j], work_A[i])/np.dot(Q[j], Q[j])*Q[j]
		
		Q.append(lum/np.linalg.norm(lum))
Qs = np.array(Q)
Qt = Qs.transpose()
for num in Qt:

	print(num)

