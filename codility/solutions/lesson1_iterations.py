# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/programmers/lessons/1-iterations/
# https://app.codility.com/demo/results/trainingNYR75D-X99/


def solution(N):
    maxGap = 0
    tempGap = 0
    b = "{0:b}".format(N)
    for n in b:
        if n == '1':
            maxGap = max(tempGap, maxGap)
            tempGap = 0
        if n == '0':
            tempGap +=1
    return maxGap