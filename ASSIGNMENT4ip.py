import os
import copy
import time
import random
N = int(input("size of grid: "))

flag = True # a variable which can be true or false, initialised to True for sake of taking input till declared false

class Grid :
    def __init__(self, n, start, end, myObstacles, myRewards):
        self.n = n
        self.start = start
        self.end = end
        self.myObstacles= myObstacles
        self.myRewards = myRewards
        
    def rotateClockwise(self, n):
        #'''rotates the grid clockwise n time by 90 degree keeping original position same'''
        global g
        if n%4 == 1:
            g_0 = copy.deepcopy(g)#create deepcopy of the original grid

            for i in range(len(g)):
                for j in range(len(g)):
                    g_0[i][j] = g[len(g) -j - 1][i] # to reassign values to deepcopy to form clockwise version of original grid
            pq = g_0 # a variable pq which is equal to fina grid obtained after rotation of original grid
        
        if n%4 == 2:
            g_1 = copy.deepcopy(g)#create deepcopy of the original grid

            for i in range(len(g)):
                for j in range(len(g)):
                    g_1[i][j] = g[len(g) -j - 1][i] #to reassign values to deepcopy to form clockwise version of original grid
            g_2 = copy.deepcopy(g_1)#to create deepcopy of grid after rotation of one time

            for i in range(len(g)):
                for j in range(len(g)):
                    g_2[i][j] = g_1[len(g) -j - 1][i]#to reassign values to deepcopy of the grid to form new grid
            pq = g_2 # a variable pq which is equal to fina grid obtained after rotation of original grid
        if n%4 == 3:
            g_1 = copy.deepcopy(g)#create deepcopy of original grid

            for i in range(len(g)):
                for j in range(len(g)):
                    g_1[i][j] = g[len(g) -j - 1][i]#to reassign values to deepcopy of original grid

            g_2 = copy.deepcopy(g_1) #deepcopy of gris after one time
            for i in range(len(g)):
                for j in range(len(g)):
                    g_2[i][j] = g_1[len(g) -j - 1][i] #reassigning values to deepcopy of grid
        
            g_3 = copy.deepcopy(g_2) #create deepcopy of gris after two tomes clockwise rotation
            for i in range(len(g)):
                for j in range(len(g)):
                    g_3[i][j] = g_2[len(g) -j - 1][i]#reassign vaues after three times clockwise rotation
            pq = g_3# a variable pq which is equal to fina grid obtained after rotation of original grid
        if n%4 ==0 :
            pq = g#clockwise rotation 4 times means original grid
        if pq[p.x][p.y] != '#':
            g = pq
            for nambiar in range(len(g)):
                for nambiarhari in range(len(g)):
                    if g[nambiar][nambiarhari] == 'O':
                        g[nambiar][nambiarhari] = '.'# as the O would be rotated on clockwise rotation and position of player is not to be changed, the new O is irrelevent. So we assign it '.'
            g[p.x][p.y] = 'O'
                        
            return g
        else: #if after rotation the O coincides with an obstacle, rotation not allowed
            print('grid cant be rotated')
            return g
        
    def rotateAntiClockwise(self, n):
       # '''implementation of anticlockwiserotation of grid by 90 degrees with position of obstacle same
        #and carried out n times'''
        g = gt.rotateClockwise(n)# three tmes clockwise rotation is equal to one times anticlockwise rotation
        g = gt.rotateClockwise(n)
        g = gt.rotateClockwise(n)
        
        return g
    def showGrid(self):
        #'''function to showgrid, displays obstacles, rewards and sart, end position'''
        t = []
        grid = [["." for i in range(self.n)] for i in range(self.n)]
        grid[self.start[0]][self.start[1]] = "O" #assign the start position with symbol O
        grid[self.end[0]][self.end[1]] = "E"#assign the final position with symbol E
        for num in self.myObstacles:
            grid[num[0]][num[1]] = "#"# assign obstacles with symbol '#'
        for num in self.myRewards:#assign reward cells with any random integer 
            grid[num[0]][num[1]] = num[2]
            
        return grid
class Player:
    
    def __init__(self, x, y, energy):
        self.x = x # initialise X coordinate of Player
        self.y = y # initialise Y coordinate of Player
        self.energy = 2*(gt.n)
        if g[self.x][self.y] == "E":
            print("You won")
            flag = False # since the player reached E, no further input to be taken. So flag = False
    def increasepoints(self):
        #function to increase or decrese your points according to moves
        if g[self.x][self.y] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])
        elif g[self.x][self.y] == "#":
            self.energy = self.energy - 4*((gt.n))
        else:
            self.energy = self.energy - 1
                
    def makeMove(self, s):
        #'''implementation of moving L, R, U, D, C, A based on given command'''
        global flag
        t = []
        s_a = s[::2] #to take alternate values of string that is only L, R, U , D, A, C commands
        s_a1 = [d for d in s_a]
        
        s_b = s[1::2] #to take alternate values of string for number of steps to be taken
        s_b1 = [d for d in s_b]
        
        for hn in range(len(s_a)):
            t.append((s_a1[hn], int(s_b1[hn]))) # to form a list of tuples; each tuple having direction as first element and number of steps as second element
        for k in range(len(t)):
            os.system('cls' if os.name == 'nt' else 'clear')
            if t[k][0] == 'R':
             
                for a in range(int(t[k][1])):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for num in g:
                        print(*num)
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if self.y < gt.n - 1:
                        self.y = self.y + 1 # to move Right on console
                        
                        if g[self.x][self.y] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])
                        elif str(g[self.x][self.y]) == "#":
                            self.energy = self.energy - 4*((gt.n))
                        else:
                            self.energy = self.energy - 1
                        if g[self.x][self.y] == "E":
                            print("Won")
                            flag = False
                        
                        g[self.x][self.y] = '*'
                    elif self.y >= gt.n - 1 :
                        #To ensure object does not move out of grid'''
                        self.y = 0
                        #object appears on starting of grid
                        if g[self.x][self.y] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])
                        elif g[self.x][self.y] == "#":
                            self.energy = self.energy - 4*((gt.n))
                        else:
                            self.energy = self.energy - 1
                        if g[self.x][self.y] == "E":
                            print("Won")
                            flag = False
                        
                        g[self.x][self.y] = "*"
                                            
            elif t[k][0] == "L":
                
                for b in range(int(t[k][1])):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    for num in g:
                        print(*num)

                    os.system('cls' if os.name == 'nt' else 'clear')
                    if self.y >= 0:
                        self.y = self.y - 1
                        
                        if str(g[self.x][self.y]) in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])
                        elif g[self.x][self.y] == "#":
                            self.energy = self.energy - 4*((gt.n))
                        else:
                            self.energy = self.energy - 1
                        if g[self.x][self.y] == "E":
                            print("Won")
                            flag = False
                        
                        g[self.x][self.y] = '*'
                    elif self.y <= 0: 
                        #'''To ensure object does not move out of grid'''
                        self.y = gt.n - 1
                        #to make object come at end of the row of grid so it moves left
                        if str(g[self.x][self.y]) in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])#points increase by value*n
                        elif g[self.x][self.y] == "#":
                            self.energy = self.energy - 4*((gt.n))#points decrease by 4*n
                        else:
                            self.energy = self.energy - 1 #point decrease y 1 on each move
                        if g[self.x][self.y] == "E":
                            print("Won")
                            flag = False
                        
                        g[self.x][self.y] = '*'
            elif t[k][0] == "D":
                 # to make object move down
                 for c in range(int(t[k][1])):
                     os.system('cls' if os.name == 'nt' else 'clear')
                     
                     for num in g:
                         print(*num)
                     if g[self.x][self.y] == "E":
                         print("You won!")
                         flag = False
                         break
                     os.system('cls' if os.name == 'nt' else 'clear')
                     if self.x < gt.n - 1 :
                         self.x = self.x + 1
                    
                         if str(g[self.x][self.y]) in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                             self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])#points increase by value*n
                         elif str(g[self.x][self.y]) == "#":
                             self.energy = self.energy - 4*((gt.n)) #points decrease by 4*n
                         else:
                             self.energy = self.energy - 1 #point decrease y 1 on each move
                         if g[self.x][self.y] == "E":
                             print("Won")
                             flag = False
                         
                         g[self.x][self.y] = '*'
                     elif self.x >= gt.n - 1:
                        # '''To ensure object does not move out of grid''' and comes to top of column
                         self.x = 0
                        
                         if str(g[self.x][self.y]) in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: #points increase by value*n
                            self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])
                         elif str(g[self.x][self.y]) == "#":
                             self.energy = self.energy - 4*((gt.n)) #points decrease by 4*n
                         else:
                             self.energy = self.energy - 1 #point decrease y 1 on each move
                         if g[self.x][self.y] == "E":
                             print("Won")
                             flag = False
                         g[self.x][self.y] = '*'
                         
            elif t[k][0] == 'U':
                #to move up in grid
                for d in range(int(t[k][1])):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    for num in g:
                        print(num)
                    if g[self.x][self.y] == "E":
                        print("You won!")
                        flag = False
                        break
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if self.x >= 0 : 
                         if str(g[self.x][self.y]) in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                             self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])
                         elif str(g[self.x][self.y]) == "#":
                             self.energy = self.energy - 4*((gt.n))
                         else:
                             self.energy = self.energy - 1
                         self.x = self.x - 1
                         if g[self.x][self.y] == "E":
                            print("Won")
                            flag = False #person won, no input required
                
                         g[self.x][self.y] = '*'
                    elif self.x > gt.n - 1:
                        #'''To ensure object does not move out of grid and comes to bottom of column
                        self.x = gt.n - 1
                        
                        if str(g[self.x][self.y]) in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            self.energy = self.energy + ((gt.n)//2)*int(g[self.x][self.y])
                        elif str(g[self.x][self.y]) == "#":
                            self.energy = self.energy - 4*((gt.n))
                        else:
                            self.energy = self.energy - 1
                        if g[self.x][self.y] == "E":
                            print("Won")
                            flag = False#person won, no further input needed
                        g[self.x][self.y] = '*'
                
            elif t[k][0] == 'C':
                gt.rotateClockwise(t[k][1])
                self.energy = self.energy - gt.n//3
            elif t[k][0] == 'A':
                gt.rotateAntiClockwise(t[k][1])
                self.energy = self.energy - gt.n//3# energy decrease by n//3 units
            if self.energy <= 0:
            
                if g[self.x][self.y] == "E":
                    print("Won")
                    flag = False # energy i zero, so no more inputs will be taken
                else:
                    print('Lost :-(')
                    flag = False
            else:
                if g[self.x][self.y] == "E":
                    print("Won")
                    flag = False
            
        return (self.energy)
class Obstacles:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rewards:
    def __init__(self, x, y):
        self.x = x
        self.y = y
                    
Start = []
End  = []
myRewards = []
while len(Start) != 2:
    k = random.randint(0, 2)
    if k== 0:
        Start.append(0)
        Start.append(random.randint(0, N - 1))#coordinate at first row
    elif k== 1:
          
        Start.append((random.randint(0, N-1))) #coordinate at first column
        Start.append(0)
        
    elif k == 2:
        Start.append(N-1)
        Start.append((random.randint(0, N-1))) #coordinate in last row

myObstacles = []
for aj in range(N):
    t1 = random.randint(0, N - 1)
    t2 = random.randint(0, N - 1)
    if t1 != Start[0] and t2 != Start[1] :
        
        myObstacles.append((t1, t2)) # randome obstacles placed 

while len(End) != 2:
    k = random.randint(0, 2)
    if k== 0:
        End.append(0)
        End.append(random.randint(0, N - 1)) # coordinate at first row
    elif k== 1:
        
        End.append((random.randint(0, N-1))) # coordinate at first column
        End.append(0)
        
    elif k == 2:
        End.append(N-1)
        End.append((random.randint(0, N-1))) # coordinate at last row
    
for aj in range(N - 2):
    t_a = random.randint(0, N-2)
    t_b = random.randint(0, N -2)
    t_c = random.randint(0, N - 1)
    if t_a != Start[0] and t_b != Start[1] and t_a != End[0] and t_b != End[1] and (t_a, t_b) not in myObstacles:
        myRewards.append((t_a, t_b, t_c))# to introduce random rewards
gt = Grid(N, Start, End, myObstacles, myRewards)# creating new object of grid
g = gt.showGrid()  #calling showgrid function to display grid

          
p = Player(Start[0], Start[1], N*2) # new object player

for num in g:
    print(*num)

while flag:#(keeps taking input while flag = True, will stop taking input when flag = False)
    
    command = input("whats your command melord: ")
    
    print(p.makeMove(command))
    for num in g:
        print(*num)