# task1
from math import sqrt

def prob1(a, b, k):
    nums = []
    for i in range(a,b+1):
        count = 0
        for j in range(1, int(sqrt(i)) + 1):
            if i % j == 0:
                count += 1
                if j != i // j:
                    count +=1
        if count == k:
            nums.append(i)
    print(nums)
    return nums
        
a = int(input(">>> "))        
b = int(input(">>> "))        
k = int(input(">>> "))        
      
prob1(a,b,k)



#task2
def is_arithmetic(seq: list):
    if not seq:
        return True
    elif len(seq) == 1:
        return True
        
    n = seq[1] - seq[0]
    
    for i in range(len(seq) - 1):
        if seq[i] + n == seq[i + 1]:
            continue
        return False
    return True



#task3
def deviation(seq, pred):
    srted = [x for x in seq if pred(x)]
    if not srted:
        return 0
    smin = min(srted)
    smax = max(srted)
    
    return smax - smin



#task4
def every_second(seq):
    if not seq:
        # yield
        return
    while seq:
        seq += seq[:2]
        yield seq[0]
        # print(seq)
        # print(seq[0])
        seq = seq[2:]
        # input()

#chatGPT
class EverySecond:
    def __init__(self, seq):
        self.seq = seq
        self.index = 0  # Keep track of where we are in the sequence

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if not self.seq:  # If the sequence is empty, raise StopIteration
            raise StopIteration
        
        # Access the current element
        current = self.seq[self.index]
        
        # Update index to get the next "every second" element
        self.index = (self.index + 2) % len(self.seq)  # Move two steps forward, wrap around if necessary
        
        return current



#task5
class Interval:
    def __init__(self, a, b):
        if a > b:
            self.empty = True
        else:
            self.a = a
            self.b = b
            self.empty = False

    def __repr__(self):
        return f"Interval({self.a}, {self.b})" if not self.empty else "Interval(empty)"
        
    def __contains__(self, x):
        if self.empty:
            return False
        return self.a <= x <= self.b