numheads = 35
numlegs = 94

def puzzle(numheads,numlegs):
    alllegs = numheads * 2
    legs = numlegs-alllegs
    rabbits = legs/2
    return rabbits, numheads - rabbits

print(puzzle(numheads,numlegs))