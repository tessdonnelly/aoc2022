from collections import deque

with open("input11.txt", "r") as f:
    lines = f.readlines()

class Monkey():
    def __init__(self,id,items,op,d_t,t_t,f_t):
        self.id = id
        self.items = deque(items)
        self.items_inspected = 0
        self.operation = op
        self.divisible_test = d_t
        self.true_throw = t_t
        self.false_throw = f_t

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)
    
    def inspect(self, monkeys,lcm):
        while len(self.items) > 0:
            item = self.items.popleft()
            self.items_inspected += 1
            item = self.do_operation(item)
            #item = int(item/3)
            item = item%lcm
            test = (item%self.divisible_test) == 0
            if test: 
                throw_to = monkeys.get(self.true_throw)
            else: 
                throw_to = monkeys.get(self.false_throw)
            throw_to.add_item(item)

    def do_operation(self,item):
        result = 0
        if self.operation[1] == 'old':
            arg_2 = item
        else: arg_2 = int(self.operation[1])
        if self.operation[0] == '*':
            result = item * arg_2
        elif self.operation[0] == '+':
            result = item + arg_2
        return result

def initialize_monkeys(input):
    monkeys = {}
    lcm = 1
    for i in range(0,len(input),7):
        id = input[i].strip().split(' ')[1][0]
        items = list(map(int,input[i+1].strip().split(':')[1].split(',')))
        operation = input[i+2].strip().split(':')[1].split('=')[1].strip().split(' ')[1:]
        divisible_test = int(input[i+3].strip().split(' ')[3])
        true_throw = input[i+4].strip().split(' ')[5]
        false_throw = input[i+5].strip().split(' ')[5]
        m = Monkey(id,items,operation,divisible_test,true_throw,false_throw)
        monkeys.update({id:m})
        lcm *= divisible_test
    return monkeys, lcm

def monkey_rounds(monkeys,n,lcm):
    for i in range(n):
        for m in monkeys:
            monkeys.get(m).inspect(monkeys,lcm)

def monkey_business(monkeys):
    business = []
    for m in monkeys:
        business.append(monkeys.get(m).items_inspected)
    print(business)
    business = sorted(business,reverse = True)
    level = business[0]*business[1]
    return level
        
monkeys, lcm = initialize_monkeys(lines)
monkey_rounds(monkeys,10000,lcm)
print(f'monkey business = {monkey_business(monkeys)}')
