with open("input10.txt", "r") as f:
    lines = f.readlines()

def execute(input):
    x = 1
    cycle = 0
    x_map = {}
    for l in input:
        x,cycle = do_instruction(l.strip().split(' '),x,cycle,x_map)
    return x_map
    
def do_instruction(line, x, cycle,x_map):
    cycle +=1
    x_map.update({cycle:x})
    if line[0] != 'noop':
        cycle +=1
        x_map.update({cycle:x})
        x += int(line[1])
    return x, cycle

x_map = execute(lines)

def get_signal_strength(x_map):
    sum = 0
    for i in range(20,240,40):
        sum += i*x_map.get(i)
    return sum

def print_pixels(x_map):
    pixels = []
    p = []
    for i in range(0,6):
        p = []
        for j in range(i*40,(i*40)+40):
            cycle = j+1
            sprite = x_map.get(cycle)
            if cycle-(i*40 + 1) in [sprite-1,sprite,sprite+1]:
                p.append('#')
            else: p.append('.')
        pixels.append("".join(p))
   
    for pix in pixels: print(pix)

print_pixels(x_map)


