def degreeOfArray(arr):
    if len(arr) == 0:
        return 0

    #get max_degree
    deg_ele = {}
    start_ele = {}
    max_deg = 1
    res = None#len(arr)
    for i in xrange(len(arr)):
        print arr[i]
        num = arr[i]
        if num not in deg_ele:
            deg_ele[num] = 1
            start_ele[num] = i
        #num appears before
        else:
            deg_ele[num] += 1
            if deg_ele[num] >max_deg:
                max_deg = deg_ele[num]
                gap = i - start_ele[num] + 1
                #print "GAP", gap, max_deg
                res = gap

            elif deg_ele[num] == max_deg:
                if res > gap:
                    res = gap

    #print "result"
    #print "max degree", max_deg
    if max_deg == 1:
        res = 1
    return res




arrx = [1, 2, 2, 3, 1]
#arrx = [1,2,3]
#arrx = [2, 1,1,1, 2, 1,2,3,2]
#arrx = range(1, 1000000)
#arrx = []
print degreeOfArray(arrx)
