with open("input07.txt", "r") as f:
    lines = f.readlines()


class Dir():
    def __init__(self,id,name,parent,dirs):
        self.name = name
        self.parent = parent
        self.size = 0
        self.contains = []
        self.id = id
        self.child = []
    
    def get_size(self):
        sum = 0
        for c in self.contains:
            c = c.split(' ')
            if c[0] == 'dir':
                for d in self.child:
                    if d.name == c[1]:
                        sum += dirs.get(d.id).get_size()
            else:
                sum += int(c[0])
        return sum



def browse(input):
    dirs = {}    
    current = 0
    count = 0
    d = Dir(count,'base',current,dirs)
    dirs.update({count:d})
    i = 0 
    while i < len(input):
        l = input[i]
        if l[0] == '$' and l[2:7] == 'cd ..':
            current = dirs.get(current).parent
            i+=1
        elif l[0] == '$' and l[2:4] == 'cd':
            count +=1
            name = l[5:].strip()
            d = Dir(count,name,current,dirs)
            dirs.update({count:d})
            dirs.get(current).child.append(d)
            current = count
            i+=1
        elif l[0] == '$' and l[2:4] == 'ls':
            contents = []
            j = i+1
            while j<len(input):
                c = input[j].strip()
                if c[0] != '$':
                    contents.append(c)
                    j+=1
                else: break
            dirs.get(current).contains=contents
            i=j
    return dirs


def get_total(dirs):
    total = 0
    sizes = {}
    for d in dirs:
        if d in sizes:
            s = sizes.get(d)
        else:
            s = dirs.get(d).get_size()
            sizes.update({d:s})
        print(f'dir {d} has size {s}')
        if s <= 100000:
            total += s
    return total,sizes

        

dirs = browse(lines)

answer,sizes = get_total(dirs)
print (f'sum total sum of directories at most 100000 = {answer}')

total_space = 70000000
needed_space = 30000000
used_space = total_space-sizes[1]
dir_space=needed_space-used_space
print (dir_space)
list_sizes = list(sizes.values())
list_sizes.sort()

def get_space(list):
    for l in list:
        if l >= dir_space:
            return l
            

print(f'dir size needed is {get_space(list_sizes)}')



