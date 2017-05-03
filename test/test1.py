# coding=utf-8 

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        for line, previous_lines in search(f, 'python', 5):
            for pline in previous_lines:
                print pline.strip()
                pass
            print line.strip()
            print '-'*20
