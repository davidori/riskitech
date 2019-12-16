# https://app.codility.com/programmers/lessons/2-arrays/
# OddOccurrencesInArray : 

def solution(A):
    unpaired_values = set()
    for n in A:
        if n in unpaired_values:
            unpaired_values.remove(n)
        else:
            unpaired_values.add(n)
    return(list(unpaired_values))[0]


#  CyclicRotation:

def solution(A, K):
    if( len(A) <= 1 or K % len(A) == 0 ):
        return A

    double_array = A.copy() + A.copy()
    index = K % len(A)
    return double_array[len(A) - index: - index]
