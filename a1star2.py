grid = [
["*", "*", "*", "*", "*"],
["*", "*", "*", "*", "*"],
["*", "*", "*", "*", "*"],
["*", "*", "*", "*", "*"],
["*", "*", "*", "q", "*"]
]
starting_point = grid[0][1]
ending_point = grid[4][3]
#global variable has number = local_value + distance from destination  
#local variable has parent and number = local value of parent+ distance from parent
class Node:
	def __init__(self, x, y,local_var, global_var):
		self.x = x
		self.y = y
		self.local_var = local_var
		self.global_var = global_var
class Local_variable:
	def __init__(self , parent, value):
		self.parent = parent
		self.value = value

for i in range(len(grid)):
	for j in range(len(grid)):
		grid[i][j] = Node(i, j, Local_variable("", 10**8),(10**8))
def neighbours(a):
	x = a.x
	y = a.y
	t = []
	if y < len(grid) - 1:
		t.append(grid[x][y+1])
	if x < len(grid) - 1:
		t.append(grid[x+1][y])
	if x > 0:
		t.append(grid[x - 1][y])
	if y > 0:
		t.append(grid[x][y - 1])
	return t
#print(neighbours(grid[1][2])) 

def am_i_done(a):
	global ending_point
	if a.x == ending_point.x and a.y == ending_point.y:
		return True
	else:
		return False
def recursive_fun(a):
	starting_point = Node(0, 1, Local_variable("", 10**8),(10**8))
	ending_point = Node(4, 3, Local_variable("", 10**8),(10**8))
	t = neighbours(a)
	name_of_neighbours = []
	global_val_of_neighbours = []
	l = []
#global variable has number = local_value + distance from destination  
#local variable has parent and number = local value of parent+ distance from parent
	if a.x == starting_point.x and a.y == starting_point.y:
		a.local_var.value = 0
		a.global_var = abs(a.x - ending_point.x) + abs(a.y - ending_point.y)

	for num in t:
		if a.local_var.value < num.local_var.value + abs(num.x - a.x)+abs(num.y - a.y):

			num.local_var.parent = a
			num.local_var.value = a.local_var.value + abs(num.x - a.x)+abs(num.y - a.y)
			num.global_var = num.local_var.value + abs(num.x - ending_point.x)+abs(num.y - ending_point.y)
			l.append(num)
			global_val_of_neighbours.append(num.global_var)
	l.sort(key = lambda num: num.global_var)
	pq = []
	for num in l:
		pq.append((num.x, num.y))
	print("pq", pq)
	return l	
class Noddy:  
    def __init__(self, data): 
        self.data = data 
        self.next = None   
class LinkmyList: 
     def __init__(self): 
        self.head = None
a_path = LinkmyList()
a_path.head = grid[0][1]
h = 0
nkb= []
nkb.append(a_path.head)
def use_recursion(t):
	global h
	if t.x == 4 and t.y == 3:
		return nkb
	else:
		u = recursive_fun(t)
		if len(u) > 0:
			m_1 = u[0]
			nkb[h].next = m_1
			nkb.append(m_1)
			h = h + 1
		return use_recursion(u[0])
#print("Hi: ", recursive_fun(grid[0][1]))	
#print("Hi ji", use_recursion(grid[0][0]))	
for num in use_recursion(grid[0][1]):
	print("iiitd: ", (num.x, num.y))
