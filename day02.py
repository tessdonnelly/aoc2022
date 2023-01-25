with open("input02.txt", "r") as f:
    lines = f.readlines()


def score(line):
    s = 0
    opp = line[0]
    you = line[2]
    s += get_shape(you)
    s += get_outcome(opp,you)
    return s

def get_shape(y):
    # rock
    if y == 'X' or 'A':
        return 1
    # paper
    elif y == 'Y' or 'B':
        return 2
    # scissors 
    elif y == 'Z' or 'C':
        return 3

def get_outcome(o,y):
    loss = [['A','Z'],['C','Y'],['B','X']]
    win = [['C','X'],['B','Z'],['A','Y']]
    draw = [['A','X'],['B','Y'],['C','Z']]
    # draw
    if [o,y] in draw:
        return 3
    # loss
    elif [o,y] in loss:
        return 0
    # win
    elif [o,y] in win:
        return 6

'''
# part 1
total = 0
for l in lines:
    total += score(l)
print (total)
'''    

# part 2 

def score_2(line):
    s = 0
    opp = line[0]
    out = line[2]
    s += outcome(out)
    s += get_you(opp,out)
    return s

def outcome(o):
    #loss
    if o == 'X':
        return 0
    #draw
    elif o == 'Y':
        return 3
    #win
    elif o == 'Z':
        return 6 

def get_you(opp,out):
    # A = rock, B = Paper, C = Scissors 
    rock = [['A','Y'],['B','X'],['C','Z']]
    pap = [['A','Z'],['B','Y'],['C','X']]
    scis = [['A','X'],['B','Z'],['C','Y']]
    if [opp,out] in rock:
        return 1
    elif [opp,out] in pap:
        return 2
    elif [opp,out] in scis:
        return 3

total = 0
for l in lines:
    total += score_2(l)
print (total)


