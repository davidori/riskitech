# https://app.codility.com/programmers/lessons/3-time_complexity/

# FrogJmp
#solution 1
import math # use of meth 

def solution(X, Y, D):
    if( X == Y):
        return 0
    return math.ceil( (Y - X) / D)

#solution 2
def solution(X, Y, D):
    location = X
    counter = 0
    while( location < Y):
        location += D
        counter += 1
    return counter


# PermMissingElem
def solution(A):
    array_sum = sum(A)
    total_sum = ((1 + len(A)+1) * (len(A)+1) )// 2
    return total_sum - array_sum

# TapeEquilibrium
def solution(A):
    total = sum(A)
    min_diff = float('inf')
    current_r_sum = 0
    for v in A[:-1]:
        current_r_sum += v
        min_diff = min(abs((total - current_r_sum) - current_r_sum), min_diff)
        if min_diff == 0:
            return 0
    return min_diff
        