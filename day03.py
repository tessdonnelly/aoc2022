with open("input03.txt", "r") as f:
    lines = f.readlines()

def decode_backpacks(ls,p):
    s = 0
    for line in ls:
        s += get_priority(line.strip(),p)
    return s

def get_priority(l, p):
    mid = int(len(l)/2)
    first = set(l[:mid])
    sec = set(l[mid:])
    c =  first.intersection(sec)
    return p.get(c.pop())


def make_priority():
    priority = {}
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = []
    for c in lower:
        upper.append(c.upper())
    for i in range(1,27):
        priority.update({lower[i-1]:i})
    for j in range(27,53):
        priority.update({upper[j-27]:j})
    return priority

def elf_badges(ls,p):
    s = 0
    for i in range(0,len(ls),3):
        s1 = set(ls[i].strip())
        s2 = set(ls[i+1].strip())
        s3 = set(ls[i+2].strip())
        c = (s1.intersection(s2)).intersection(s3)
        s += p.get(c.pop())
    return s


p = make_priority()
print (decode_backpacks(lines, p))
print (elf_badges(lines,p))
