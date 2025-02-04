from itertools import permutations

def print_permutations():
    user = input()
    perm = permutations(user)
    
    for perm in perm:
        print("".join(perm))  
print_permutations()
