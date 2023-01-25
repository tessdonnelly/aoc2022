with open("input04.txt", "r") as f:
    lines = f.readlines()

def decode_pairs(ls):
    numContained = 0
    numOverlap = 0 
    for l in ls:
        pair = l.strip().split(',')
        e1 = pair[0].split('-')
        e2 = pair[1].split('-')
        s1 = set(range(int(e1[0]),int(e1[1])+1))
        s2 = set(range(int(e2[0]),int(e2[1])+1))
        overlap = s1.intersection(s2)
        if overlap == s1 or overlap == s2:
            numContained += 1
        if overlap:
            numOverlap += 1 
    return numContained, numOverlap
    
answer = decode_pairs(lines)
print (
    f'number of pairs fully contained = {answer[0]} \nnumber of overlaps = {answer[1]}'
    )
