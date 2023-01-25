import json

with open("input13.txt", "r") as f:
    lines = f.readlines()

def get_pairs(input):
    pairs = {}
    numPairs = 0
    for i in range(0,len(input),3):
        numPairs += 1
        p1 = json.loads(input[i].strip())
        p2 = json.loads(input[i+1].strip())
        pairs.update({numPairs:[p1,p2]})
    return pairs

def check_order(left,right):
    if type(left) is int and type(right) is int:
        if left < right: return True
        if left > right: return False 
    
    if type(left) is list and type(right) is list:
        for i in range(0,min(len(left),len(right))):
            order = check_order(left[i],right[i])
            if order is not None : return order
        if len(left) < len(right): return True
        if len(left) > len(right): return False 

    if (type(left) is list) ^ (type(right) is list):
        if type(left) is not list: left = [left]
        if type(right) is not list: right = [right]
        order = check_order(left,right)
        if order is not None : return order
       

pairs = get_pairs(lines)

# part 1 
'''
sum  = 0
for p in pairs: 
    left = pairs.get(p)[0]
    right = pairs.get(p)[1]
    if check_order(left,right): sum += p

print(f'sum of indices = {sum}')

'''

# part 2 

def get_packets(input):
    packets = {}
    count = 0
    for i in range(len(input)):
        if input[i] != '\n':
            count +=1
            p = json.loads(input[i].strip())
            packets.update({count:p})
    # add decoder packets
    d1 = [[2]]
    d2 = [[6]]
    packets.update({count+1:d1})
    packets.update({count+2:d2})
    return packets

def sort_packets(packets):
    sorted = False
    while sorted is False:
        swaps = 0
        for i in range(1,len(packets)):
            if not check_order(packets.get(i),packets.get(i+1)):
                swaps +=1
                temp = packets.get(i)
                packets.update({i:packets.get(i+1)})
                packets.update({i+1:temp}) 
        if swaps==0 : sorted = True
    return packets

def get_decoder_key(packets):
    d1 = [[2]]
    d2 = [[6]]
    index1 = list(packets.keys())[list(packets.values()).index(d1)]
    index2 = list(packets.keys())[list(packets.values()).index(d2)]
    return index1*index2

packets = get_packets(lines)
sort_packets(packets)
print(f'decoder key = {get_decoder_key(packets)}')

    