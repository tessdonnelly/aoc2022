with open("input14.txt", "r") as f:
    lines = f.readlines()

def get_rock_paths(input):
    rocks = set()
    for l in input:
        l = l.strip().split('->')
        for i in range(0,len(l)):
            coord = list(map(int,l[i].strip().split(',')))
            l[i] = coord
        for j in range(0,len(l)-1):
            coord1, coord2 = l[j], l[j+1]
            x1,y1 = coord1[0],coord1[1]
            x2,y2 = coord2[0],coord2[1]
            if x1 < x2: xmin,xmax = x1,x2
            else: xmin, xmax = x2,x1
            if y1 < y2: ymin,ymax = y1,y2
            else: ymin, ymax = y2,y1
            for x in range(xmin,xmax+1):
                rocks.add(tuple([x,y1]))
            for y in range(ymin,ymax):
                rocks.add(tuple([x1,y]))
    return rocks

def draw_cave(rocks,sand):
    cave = []
    for y in range(0,165):
        cave_row = []
        for x in range(200,1000):
            if [x,y] == [500,0]: cave_row.append('+')
            if tuple([x,y]) in rocks:
                cave_row.append('#')
            elif tuple([x,y]) in sand:
                cave_row.append('o')
            else: cave_row.append('.')
        cave.append(cave_row)
    for row in cave:
        print (''.join(row))
   

def get_drop(position,rocks,sand):
    # possible drops [x,y+1],[x-1,y+1],[x+1,y+1]
    x_pos, y_pos = position[0], position[1]
    for [x,y] in [[x_pos,y_pos+1],[x_pos-1,y_pos+1],[x_pos+1,y_pos+1]]:
        if tuple([x,y]) not in rocks and tuple([x,y]) not in sand:
            return [x,y]
    return None

def sand_fall(rocks):
    sand = set()
    infinite = False
    for i in range(50000):
        sand_pos = [500,0]
        new_pos = get_drop(sand_pos,rocks,sand)
        while new_pos is not None:
            sand_pos = new_pos
            if sand_pos[1] > 200:
                (f'sand falling infinitely')
                new_pos = None
                infinite = True
                break
            new_pos = get_drop(sand_pos,rocks,sand)
        if not infinite:
            print (f'sand stopping at [{sand_pos}')
            sand.add(tuple(sand_pos))
        else: break
    return sand
    
# part 1 
'''
rocks = get_rock_paths(lines)
sand = sand_fall(rocks)
draw_cave(rocks,sand)
print(f'units of sand = {len(sand)}')
'''

# part 2 
def add_floor(rocks):
    x_min, x_max = 500, 500
    y_max = 0
    for r in rocks:
        x, y = r[0],r[1]
        if x < x_min: x_min = x
        if x > x_max: x_max = x
        if y > y_max: y_max = y  
    for i in range(x_min-1000,x_max+1001):
        rocks.add(tuple([i,y_max+2]))
        print (f'adding {i},{y_max+2} as a rock!')
    return rocks

rocks = get_rock_paths(lines)
rocks_update = add_floor(rocks)
print(len(rocks))
sand = set()
draw_cave(rocks_update,sand)
sand = sand_fall(rocks)
draw_cave(rocks,sand)
print(f'units of sand = {len(sand)}')