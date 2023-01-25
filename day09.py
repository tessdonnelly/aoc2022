import numpy as np

with open("input09.txt", "r") as f:
    lines = f.readlines()

class Knot():
    def __init__(self,name,start):
        self.name = name
        self.positions = set()
        self.coord = None
        self.move(start)
        
    def move(self,coord):
        self.coord = coord
        self.positions.add(tuple(coord))
    
    def head_move(self,dir):
        start = np.array(self.coord)
        if dir == 'R': new_c = [1,0]
        elif dir == 'L': new_c = [-1,0]
        elif dir == 'U': new_c = [0,1]
        elif dir == 'D': new_c = [0,-1]
        self.move(np.add(start,np.array(new_c)))

    def follow_head(self,head_coord):
        dist = np.subtract(np.array(head_coord),np.array(self.coord))
        if abs(dist[0]) > 1 or abs(dist[1]) > 1:
            # move laterally
            if dist[0] == 0 or dist[1] == 0:
                m = list(map(int,dist/2))
                c = np.add(self.coord,m)
            # move diagonally
            elif dist [0] > 0 and dist[1] > 0:
                c = np.add(self.coord,np.array([1,1]))
            elif dist [0] < 0 and dist[1] > 0:
                c = np.add(self.coord,np.array([-1,1]))
            elif dist [0] < 0 and dist[1] < 0:
                c = np.add(self.coord,np.array([-1,-1]))
            elif dist [0] > 0 and dist[1] < 0:
                c = np.add(self.coord,np.array([1,-1]))
            self.move(c)    

def do_steps(knots,dir,steps):
    for i in range(0,steps):
        j = 0
        knots[j].head_move(dir)
        for j in range(0,len(knots)-1):
            knots[j+1].follow_head(knots[j].coord)

def rope_motions(input,n):
    # n = number of knots
    knots = []
    for i in range(0,n):
        knots.append(Knot(i,[0,0]))
    for l in input:
        l=l.strip().split(' ')
        d = l[0]
        s = int(l[1])
        do_steps(knots,d,s)
    return len(knots[n-1].positions)

print(f'positions of tail = {rope_motions(lines,10)}')