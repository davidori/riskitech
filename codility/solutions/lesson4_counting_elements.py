# PermCheck

def solution(A):
    seen_nums = set()
    max_possible_num = len(A)
    for n in A:
        if n in seen_nums or n > max_possible_num:
            return 0
        else:
            seen_nums.add(n)
    return 1

# FrogRiverOne
def solution(X, A):
    positions = set()
    target = X
    jumps = 0
    for sec, leaf in enumerate(A):
        if leaf in positions:
            continue
        else:
            positions.add(leaf)
            jumps += 1
        if jumps == target:
            return sec
    return -1