import os
import sys
import copy

N = 2               # Total people number
END = [0, 0]        # destation point

    # goble decison 
src_decision = [[-2,0], [-1,0], [-1,-1], [0,-1], [0,-2]]
dst_decision = [[1,0], [2,0], [1,1], [0,1],[0,2]]

    # global AVAIABLE point 
restrict_point_list = []

    # global list to record suceess path
result_path = []

def init_restrict_point():
    for y in range(0,N+1):
        a = [0,y]
        restrict_point_list.append(a)
    for x in range(1,N):
        a = [x,x]
        restrict_point_list.append(a)
    for y in range(0,N+1):
        a = [N,y]
        restrict_point_list.append(a)

    # return 0: success
    #        1: not found
    #        2: error
def SearchCrossRiver(start_p, derict, src_reached, dst_reached):
    s_reached = copy.deepcopy(src_reached)
    d_reached = copy.deepcopy(dst_reached)

    if derict == 1:
        if start_p not in s_reached:
            s_reached.append(start_p)

        for decison in src_decision:
            point = []
            for i in xrange(2):
                point.append(start_p[i]+decison[i])
            if point == END:
                print "It succesed !!"
                result_path.append(s_reached)
                result_path.append(d_reached)
                return 0
            elif (point in restrict_point_list) and (point not in d_reached):
                SearchCrossRiver(point, -1, s_reached, d_reached)
            else:
                pass
        return 1

    elif derict == -1:
        if start_p not in d_reached:            
            d_reached.append(start_p)

        for decison in dst_decision:
            point = []
            for i in xrange(2):
                point.append(start_p[i] + decison[i])
            if point == END:
                result_path.append(s_reached)
                result_path.append(d_reached)
                return 0
            elif (point in restrict_point_list) and (point not in s_reached):
                SearchCrossRiver(point, 1, s_reached, d_reached)
            else:
                pass
        return 1
    else:
        print "error"
        return 2

def find_function():
    start_point = [N,N]     # starting point
    init_restrict_point()

    src_reached_list = []
    dst_reached_list = []

    result = SearchCrossRiver(start_point, 1, src_reached_list, dst_reached_list)
    print "result = ", result_path
    print '\n'

if __name__ == '__main__':
    find_function()