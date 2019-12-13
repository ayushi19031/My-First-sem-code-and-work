import numpy as np
no_of_col = int(input("n: "))
no_of_rows = int(input("m: "))
A_ = np.array([[1,2], [3, 4]])
A = np.array(A_)
Q_1 = []
Q = []
work_A = A.transpose()
for num in A:
	num = np.array(num)
for i in range(no_of_col):
	t = np.array(work_A[i][:])
	lum = work_A[i][:]
	j = i
	while j >  0:
		j = j - 1
		lum = lum -  np.dot(Q[j], work_A[i])/np.dot(Q[j], Q[j])*Q[j]
	Q.append(lum/np.linalg.norm(lum))
Qs = np.array(Q)
Qt = Qs.transpose()
print('Q = ')
for num in Qt:
	print(num)
R = np.dot(Qs, A_)
print('R= \n', R )
