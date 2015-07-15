#!/usr/bin/env python

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return (self.items ==[])

def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token == '' or token ==' ':
            continue
        elif token =='+':
            sum = s.pop() + s.pop()
            s.push(sum)
        elif token == '*':
            product = s.pop() * s.pop()
            s.push(product)
        elif token =='-':
            a = s.pop()
            b = s.pop()
            sum = b - a
            s.push(sum)
        elif token == '/':
            a = s.pop()
            b = s.pop()
            if a != 0:
                product = b / a
                s.push(product)
            else:
                s.push(0)
        else:
            s.push(int(token))

    return s.pop() 

def getOperator(idx):
    c = ""
    if idx == 0:
        c = "+"
    elif idx == 1:
        c = "-"
    elif idx == 2:
        c = "*"
    elif idx == 3:
        c = "/"

    return c
if __name__ == '__main__':
    expr = [["2", "3", "5"], ["2", "5", "3"], ["3", "2", "5"], ["3", "5", "2"], ["5", "2", "3"], ["5", "3", "2"]]

    print '------------------------------'
    print 'show result as postfix form :'
    print '------------------------------'

    for a in expr:
	    # case 1 : a b <op> c <op>
	    for i in range(0, 4):
	        for j in range(0, 4):
	            aa = [a[0], a[1], getOperator(i), a[2], getOperator(j)]
	            if evalPostfix(aa) == 9:
	                print '"' + (' '.join(aa)) + '" is 9'
	    # case 2 : a b c <op> <op>
	    for i in range(0, 4):
	        for j in range(0, 4):
	            aa = [a[0], a[1], a[2], getOperator(i), getOperator(j)]
	            if evalPostfix(aa) == 9:
	                print '"' + (' '.join(aa)) + '" is 9'
	
