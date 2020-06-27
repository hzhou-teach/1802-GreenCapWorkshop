# Brian Lu
# ~30 mins, further work needed
# 
# I'll be writing this on the premise that it'll always be beneficial for Bessie to build up
# the maximum amount of "spare time" that she has before Farmer John reaches her, before reaching
# the patch of grass with the maximum tastiness.
# 
# Is L relevant?
# 
# ***tttt***

import bisect

def main():
    # Hardcoded sample case
    # L, N, rF, rB = (10,2,4,3)
    # stops = [(7,2),(8,1)] # x, c (should be pre-sorted)
    # stoplocs = [7,8]
    # end = 8 # hit then beyond last stop

    file = open("reststops.in", "r")
    L, N, rF, rB = tuple(map(int, file.readline().split()))
    stops = []
    stoplocs = [0,]*N
    end = -1
    for i in range(N):
        stops.append(tuple(map(int, file.readline().split())))
        stoplocs[i] = stops[i][0]
        if i == N-1:
            end = stoplocs[N-1]
    file.close()

    position = 0
    tasty = 0
    while position < end:
        position, newtaste = stop(position, stops, stoplocs, rB, rF)
        tasty+=newtaste

    file = open("reststops.out", "w")
    file.write(str(tasty)+"\n")
    file.close()



def stop(position, stops, stoplocs, rB, rF):
    # Pretty terrible existence of both a binary search as well as a sort here.
    # First target for optimization
    usable = stops[bisect.bisect_right(stoplocs, position):]
    usable.sort(key=lambda i: i[1], reverse=True)

    tasty = (usable[0][0] - position) * (rF-rB) * usable[0][1]
    position = usable[0][0]

    return (position, tasty)

main()
