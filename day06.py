with open("input06.txt", "r") as f:
    lines = f.read()

test1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlbmjqjpqmgbljsphdztnvjfqwrcgsmlb'
test2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test3 = 'nppdvjthqldpwncqszvftbrmjlhg'
test4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'


def process_buffer(input,part):
    if part == 1:
        n = 4
    elif part == 2:
        n = 14
    for i in range(n-1,len(input)):
        lastn = set()
        for j in range(i, i-n, -1):
            lastn.add(input[j])
        if len(lastn) == n:
            return i+1
 
m = 2 
''' 
print(
    f'test 1 {test1} : first marker after char {process_buffer(test1,m)}'
)
print(
    f'test 2 {test2} : first marker after char {process_buffer(test2,m)}'
)
print(
    f'test 3 {test3} : first marker after char {process_buffer(test3,m)}'
)
print(
    f'test 4 {test4} : first marker after char {process_buffer(test4,m)}'
)
print(
    f'test 5 {test5} : first marker after char {process_buffer(test5,m)}'
)
'''
print(
    f'answer: first marker after char {process_buffer(lines,m)}'
)
