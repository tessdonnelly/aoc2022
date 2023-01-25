with open("input05.txt", "r") as f:
    lines = f.readlines()

# separate instructions
start_stacks = []
moves = []
populated = False
for l in lines:
    if l != '\n' and populated == False:
        start_stacks.append(l)
    elif l == '\n':
        populated = True
    else:
        moves.append(l.strip())

# create stacks
n = len(start_stacks)
stacks = {}
for i in range(1,len(start_stacks[n-1]),4):
    stacks.update({int(start_stacks[n-1][i]):[]})

for j in range(n-2,-1,-1):
    s = 1
    for k in range(1,len(start_stacks[j]),4):
        if start_stacks[j][k] != ' ':
            stack = stacks.get(s)
            stack.append(start_stacks[j][k])
        s +=1
'''
# do moves part one
for m in moves:
    m = m.split(' ')
    origin = stacks.get(int(m[3]))
    dest = stacks.get(int(m[5]))
    crates = int(m[1])
    for i in range(0,crates):
        dest.append(origin.pop())
'''
# do moves part two
for m in moves:
    m = m.split(' ')
    origin = stacks.get(int(m[3]))
    dest = stacks.get(int(m[5]))
    crates = int(m[1])
    temp = []
    for i in range (0, crates):
        temp.append(origin.pop())
    for j in range(0, len(temp)):
        dest.append(temp.pop())

# get last crates 
lasts = []
for p in stacks.values():
    lasts.append(p.pop())
print(''.join(lasts))


    


