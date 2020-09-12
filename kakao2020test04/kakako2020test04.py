# kakao2020test04.py -미완

def solution(n, build_frame):
    result= [[101, 101, 101]]

    for i in range(len(build_frame)):
        one_list = []
        for j in range(3):
            if (build_frame[i][0]< n or build_frame[i][1]< n):
                one_list.append(build_frame[i][j])
        if(build_frame[i][3]== 1):
            for k in range(len(result)):
                if (one_list[2]== 0 and \
                        one_list[1]== 0 or \
                        (minus_1(one_list[0])== result[k][0] and one_list[1]== result[k][1] and result[k][2]== 1) or \
                        (one_list[0]== result[k][0] and minus_1(one_list[1])== result[k][1] and result[k][2]== 0)):
                    result.append(one_list)
                    break
                elif (one_list[2]== 1 and\
                      (one_list[0]== result[k][0] and minus_1(one_list[1])== result[k][1] and result[k][2]== 0) or \
                      (plus_1(one_list[0], n)== result[k][0] and minus_1(one_list[1])== result[k][1] and result[k][2]== 0) or \
                      ((minus_1(one_list[0])== result[k][0] and one_list[1]== result[k][1] and result[k][2]== 1) and \
                      (plus_1(one_list[0], n)== result[k][0] and one_list[1]== result[k][1] and result[k][2]== 1))):
                    result.append(one_list)
                    break

        # else:
        #     for k in range(len(result)):
        #         if (one_list[2]== 0 and \
        #                 result[k] == one_list and\
        #                 not(one_list[0]== result[k][0] and plus_1(one_list[1], n) == result[k][1]) or\
        #                 not((minus_1(one_list[0])== result[k][0] and plus_1(one_list[1], n)== result[k][1] and result[k][2]== 1))):
        #             continue
        #         elif (one_list[2]== 1 and \
        #               result[k] == one_list and \
        #               not((minus_1(one_list[0])== result[k][0] and one_list[1]== result[k][1] and result[k][2]== 1) and\
        #               not(minus_1(one_list[0])== result[k][0] and minus_1(one_list[1])== result[k][1] and result[k][2]!= 0)) or \
        #               not(plus_1(one_list[0], n)== result[k][0] and one_list[1]== result[k][1] and result[k][2]== 1)):
        #             continue
        #         else:
        #             result.pop(k)

    result.sort()
    result.pop()

    return result

def minus_1(num):
    if (num- 1< 0):
        return 0
    else:
        return num-1

def plus_1(num, max):
    if (num+ 1> max):
        return num
    else:
        return num+ 1

# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1],[5,0,0,1]]))