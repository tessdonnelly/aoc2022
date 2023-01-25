with open("input15.txt", "r") as f:
    lines = f.readlines()

class Sensor():
    def __init__(self,pos,beacon_pos):
        self.pos = pos
        self.beacon_pos = beacon_pos

    def get_man_dist(self):
        dist = abs(self.pos[0]-self.beacon_pos[0]) +abs(self.pos[1]-self.beacon_pos[1])
        return dist
    
    def get_no_beacons(self,y,low,high):
        no_beacons = set()
        dist = self.get_man_dist()
        x_pos, y_pos = self.pos[0], self.pos[1]
        if abs(y_pos-y) <= dist:
            min_x = max([x_pos-(dist-abs(y-y_pos)-1),low])
            max_x = min([x_pos+(dist-abs(y-y_pos)-1), high])
            for x in range(min_x,max_x+1):
                no_beacons.add(tuple([x,y]))
                #for y in range(y_pos-dist,y_pos+dist+1):
                '''
                if [x,y] == self.beacon_pos: 
                    print('is beacon!')
                elif (abs(x-x_pos) + abs(y-y_pos)) <= dist:
                    no_beacons.add(tuple([x,y]))
                else: print('not true')
                '''
        return no_beacons

    def get_no_bs_range(self,low,high):
        no_beacons = set()
        dist = self.get_man_dist()
        x_pos, y_pos = self.pos[0], self.pos[1]
        min_x = max([x_pos-dist,low])
        max_x = min([x_pos+dist+1, high])
        min_y = max([y_pos-dist,low])
        max_y = min([y_pos+dist+1, high])
        for x in range(min_x,max_x+1):
            if abs(x_pos) - abs(x) <= dist:
                for y in range(min_y,max_y+1):
                    if abs(y_pos) - abs(y) <= dist:
                        if [x,y] == self.beacon_pos: 
                            print('is beacon!')
                        elif (abs(x-x_pos) + abs(y-y_pos)) <= dist:
                            no_beacons.add(tuple([x,y]))
        return no_beacons

    def get_perim(self,low,high):
        perim = set()
        dist = self.get_man_dist()+1
        print(f'distance = {dist}')
        x_pos, y_pos = self.pos[0], self.pos[1]
        min_x = max(x_pos-dist,low)
        max_x = min([x_pos+dist+1, high])
        min_y = max([y_pos-dist,low])
        max_y = min([y_pos+dist+1, high])
        for x in range(min_x,max_x):
            if abs(x_pos) - abs(x) <= dist:
                for y in range(min_y,max_y):
                    if abs(y_pos) - abs(y) <= dist:
                        if [x,y] == self.beacon_pos: 
                            print('is beacon!')
                        elif (abs(x-x_pos) + abs(y-y_pos)) == dist:
                            perim.add(tuple([x,y]))
        return perim


#initialize
sensor_positions = set()
sensors = {}
beacon_positions = set()
x_min,x_max, y_min,y_max = 0, 0, 0 ,0
for l in lines:
    l = l.strip().split(':')
    # get sensor pos
    sensor_pos = l[0].split(',')
    s_x = int(sensor_pos[0][12:])
    s_y = int(sensor_pos[1][3:])
    sensor_pos = [s_x,s_y]
    # get beacon pos
    beacon_pos = l[1].split(',')
    b_x = int(beacon_pos[0][24:])
    b_y = int(beacon_pos[1][3:])
    beacon_pos = [b_x,b_y]
    # add to data structures
    sensor_positions.add(tuple(sensor_pos))
    beacon_positions.add(tuple(beacon_pos))
    s = Sensor(sensor_pos,beacon_pos)
    sensors.update({tuple(sensor_pos):s})
    if max(s_x,b_x) > x_max: x_max = max(s_x,b_x)
    if max(s_y,b_y) > y_max: y_max = max(s_y,b_y)
    if min(s_x,b_x) < x_min: x_min = min(s_x,b_x)
    if min(s_y,b_y) < y_min: y_min = min(s_y,b_y)

print(f'x min = {x_min} y min = {y_min}')
print(f'x max = {x_max} y max = {y_max}')


def draw(sensor_pos):
    map = []
    s = sensors.get(tuple(sensor_pos))
    no_bs = s.get_no_bs_range(0,20)
    for y in range(y_min,y_max+1):
        row = []
        for x in range(x_min,x_max+1):
            if tuple([x,y]) in sensor_positions:
                row.append('S')
            elif tuple([x,y]) in beacon_positions:
                row.append('B')
            elif tuple([x,y]) in no_bs:
                row.append('#')
            else: row.append('.')
        map.append(row)
    for row in map:
        print (''.join(row))

#print (sensor_positions)
#draw()

def get_no_beacons(y):
    no_bs_in_y = set()
    for s in sensors:
        sensor = sensors.get(s)
        no_bs = sensor.get_no_beacons(y)
        for b in no_bs:
            if b not in no_bs_in_y:
                no_bs_in_y.add(b)
    return len(no_bs_in_y)           

# part 1
y = 2000000
#print(f'number of no beacons in y = {y} is {get_no_beacons(y)}')

# part 2 
def get_tuning_freq_1(min, max):
    possible_beacons = set()
    no_bs = set()
    for s1 in sensors:
        sensor1 = sensors.get(s1)
        print (f'sensor 1 = {sensor1.pos}')
        perim1 = sensor1.get_perim(min,max)
        print(f's1 perim = {perim1}')
        no_bs = no_bs.union(sensor1.get_no_bs_range(min,max))
        for s2 in sensors:
            if s1 is not s2:
                sensor2 = sensors.get(s2)
                print (f'sensor 2 = {sensor2.pos}')
                perim2 = sensor2.get_perim(min,max)
                overlap = perim1.intersection(perim2)
                print(f'overlap = {overlap}')
                possible_beacons = possible_beacons.union(overlap)
    print (f'possible beacons = {possible_beacons}')
    possible_beacons -= beacon_positions
    possible_beacons -= no_bs
    print (f'possible beacons = {possible_beacons}')
    beacon = possible_beacons.pop()
    tuning_freq = beacon[0]*4000000 + beacon[1]
    return beacon, tuning_freq

def get_tuning_freq_2(min, max):
    possible_beacons = set()
    all_x = set(range(0,max+1))
    for row in range(min,max+1):
        print (f'{row=}')
        no_bs_row = set()
        for s in sensors:
            sensor = sensors.get(s)
            no_bs = sensor.get_no_beacons(row,min,max)
            no_bs_row = no_bs_row.union(no_bs)
        print('done with sensors loop')
        for x in all_x:
            if tuple([x,row]) not in no_bs_row:
                if tuple([x,row]) not in beacon_positions:
                    beacon = [x,row]
    tuning_freq = beacon[0]*4000000 + beacon[1]
    return beacon, tuning_freq

    

answer = get_tuning_freq_2(0,4000000)
print(f'beacon at {answer[0]} with tuning freq {answer[1]}')

