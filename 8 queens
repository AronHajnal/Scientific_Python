import itertools

x = [i for i in range(1,9)]

y = list(itertools.permutations(x))

def check(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if abs(x[i]-x[j]) == abs(i-j):
                return False
    return True

for i in y:
     if check(i):
            print i
