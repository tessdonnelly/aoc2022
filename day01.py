with open("input01.txt", "r") as f:
    lines = f.readlines()

lines.append('\n')

# part 1
max = 0
curr = 0
for l in lines:
    if l != '\n':
        curr += int(l.strip())
    elif l == '\n':
        if curr > max:
            max = curr
        curr = 0
print ('max is ', max)

# part 2 
max = [0,0,0]
curr = 0
for l in lines:
    if l != '\n':
        curr += int(l.strip())
    # i know there's a prettier way to do this
    elif l == '\n':
        if curr > max[2]:
            t1 = max[2]
            max[2]= curr
            t2 = max[1]
            max[1] = t1
            max[0]=t2
        elif curr > max[1]:
            t1 = max[1]
            max[1] = curr
            max[0] = t1
        elif curr > max[0]: max[0] = curr
        print ('elf has ', curr)
        print('max set is', max)
        curr = 0
print ('sum of max is ', (sum(max)))

