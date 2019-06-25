'''
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Assume that:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).
https://github.com/ghanan94/codility-lesson-solutions/blob/master/Lesson%2003%20-%20Time%20Complexity/FrogJmp/task.txt
'''

X = 10
Y = 85
D = 30
step = 0
stepCounter = 0
for i in range(Y-X):
    X = X+1
    step = X+D
    if step >= Y:
        print("You have arrived ")
        break
    else:
        stepCounter +=1
        print(f"step = {step} with number of steps {stepCounter}")


# The correct solution

import math

def solution(X, Y, D):
    jumps = int(math.ceil( float(Y-X)/D ))
    return abs(jumps-1)

print(solution(85,10,30))
