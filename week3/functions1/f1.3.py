def solve(numheads, numlegs):

    numrabbit = (numlegs - (2 * numheads)) / 2 

    numchicken = numheads - numrabbit

    print(f"Number of rabbits: {numrabbit} . Number of chickens {numchicken} .")


x, y = 35, 94

solve(x, y)
