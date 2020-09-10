# kakao2020test02.py
# 괄호 변환

def solution(p):
    if (p== ""):
        return p

    count_left= 0
    count_right= 0
    u= ""
    v= ""
    empty_str= ""
    u_check= True
    check = 0

    for i in range(len(p)):
        if (p[i]== "("):
            count_left+= 1
            pass
        else:
            count_right+= 1
            pass
        if (count_left== count_right):
            u= p[:i+ 1]
            v= p[i+ 1:]
            break
            pass    #end of if
        pass    # end of for

    for i in u:
        if (i== "("):
            check+= 1
            pass
        else:
            check-= 1
            if (check< 0):
                u_check= False
                break
            pass
        pass

    if (u_check== True):
        u= u+ str(solution(v))
        pass
    else:
        empty_str= "("+ str(solution(v))+ ")"
        u= u[1:-1]
        for i in u:
            if (i== "("):
                empty_str= empty_str+ ")"
                pass
            else:
                empty_str= empty_str+ "("
                pass
            pass
        u= empty_str
        pass

    return u

print(solution("(()())()"))