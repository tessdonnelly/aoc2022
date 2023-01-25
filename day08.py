import numpy as np

with open("input08.txt", "r") as f:
    lines = f.readlines()

def get_trees(lines):
    input = []
    for l in lines:
        input.append(list(map(int,l.strip())))
    return np.array(input)
# (x,y) = trees[y][x]

def get_visibles(trees):
    n = len(trees)
    count = 0
    for y in range(0,n):
        for x in range (0,n):
            if is_edge(n-1,y,x):
                print(f'{x,y} with value {trees[y][x]} is visible')
                count +=1
            elif is_visible(trees,y,x):
                print(f'{x,y} with value {trees[y][x]} is visible')
                count+=1
    return count

def is_edge(n,y,x):
    if x == 0 or y == 0 or y == n or x == n:
        return True
    return False

def is_visible(trees,y,x):
    print(f'working on {x,y} with value {trees[y][x]}')
    v = trees[y][x]
    n = len(trees)
    if all(trees[a][x] < v for a in range(y-1,-1,-1)):
        return True
    elif all(trees[b][x] < v for b in range(y+1,n)):
        return True
    elif all(trees[y][c] < v for c in range(x-1,-1,-1)):
        return True
    elif all(trees[y][d] < v for d in range(x+1,n)):
        return True
    else: return False

def get_highest_scenic_score(trees):
    max = 0
    n = len(trees)
    for y in range(0,n):
        for x in range (0,n):
            print(f'working on {x,y} with value {trees[y][x]}')
            s = 0
            v = trees[y][x]
            top,bottom,left,right = 1,1,1,1
            if not is_edge(n-1,y,x):
                for a in range(y-1,0,-1):
                    if trees[a][x] < v:
                        top+=1
                    else: break
                for b in range(y+1,n-1):
                    if trees[b][x] < v:
                        bottom +=1
                    else: break
                for c in range(x-1,0,-1):
                    if trees[y][c] < v:
                        left +=1
                    else: break
                for d in range(x+1,n-1):
                    if trees[y][d] < v:
                        right +=1
                    else: break

                s = (top*bottom*left*right)
                print (f'score = {s} at {x,y}')
            if s > max: max = s
    return max

trees = get_trees(lines)

print(f'number of visible trees = {get_visibles(trees)}')
print(f'highest scenic score = {get_highest_scenic_score(trees)} ')


