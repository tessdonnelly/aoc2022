from collections import deque
import numpy as np

with open("input12.txt", "r") as f:
    lines = f.readlines()

rows = len(lines)
cols = len(lines[0].strip())

class Coord():
    def __init__(self,x,y,height):
        self.x = x
        self.y = y
        self.height = int(height)

class Node():
    def __init__(self,coord,dist):
        self.coord = coord
        self.dist = dist

def coord_in_map(x,y):
    return (x >= 0 and x < rows and y >=0 and y < cols)

def BFS(map,source,dest):
    visited = [[False for i in range(cols)] for j in range(rows)]
    visited[source.x][source.y]=True
    q = deque()
    s = Node(source,0)
    q.append(s)
    while q:
        current = q.popleft()
        coord = current.coord
        height = coord.height
        #print (f'exploring coord {coord.x,coord.y} with height {coord.height}')
        # check if reached dest
        if coord.x == dest.x and coord.y == dest.y:
            print (f'found path with dist {current.dist}')
            return current.dist
        # check all possible coords for moves 
        rowNum = [-1, 0, 0, 1]
        colNum = [0, -1, 1, 0]
        for i in range(4):
            x = coord.x + rowNum[i]
            y = coord.y + colNum[i]
            #print (f'checking coord {x,y}')

            if coord_in_map(x,y) and int(map[x][y]) <= height+1 and not visited[x][y]:
                visited[x][y] = True
                new = Node(Coord(x,y,int(map[x][y])),current.dist + 1)
                q.append(new)
                #print (f'adding coord {x,y} with height {int(map[x][y])}')
    return -1 


def initialize_heightmap(input):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha_map = {}
    for i in range(0,26):
        alpha_map.update({alphabet[i]:i})

    heightmap = np.zeros((rows,cols))
    for x in range(rows):
        l = input[x].strip()
        for y in range(cols):
            c = l[y]
            if c == 'S': 
                c = 'a'
                source = Coord(x,y,alpha_map.get(c))
            if c == 'E': 
                c = 'z'
                dest = Coord(x,y,alpha_map.get(c)) 
            heightmap[x][y]= alpha_map.get(c)
    return heightmap, source, dest

# part 1         
heightmap, source, dest = initialize_heightmap(lines)
print(f'shortest path from source = {BFS(heightmap, source, dest)}')

# part 2 

def initalize_part2(input):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha_map = {}
    for i in range(0,26):
        alpha_map.update({alphabet[i]:i})

    heightmap = np.zeros((rows,cols))
    sources = []
    for x in range(rows):
        l = input[x].strip()
        for y in range(cols):
            c = l[y]
            if c == 'S' or c == 'a':
                c = 'a'
                sources.append(Coord(x,y,alpha_map.get(c)))
            if c == 'E': 
                c = 'z'
                dest = Coord(x,y,alpha_map.get(c)) 
            heightmap[x][y]= alpha_map.get(c)
    return heightmap, sources, dest

heightmap, sources, dest = initalize_part2(lines)
min = 10000000
for s in sources:
    dist = BFS(heightmap,s,dest)
    if dist < min and dist > 0: min = dist
print (f'smallest dist from any a = {min}')


