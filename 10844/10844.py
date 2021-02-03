# 10844.py

def test(n):
    ans= [0, 9, 17, 32]

    for i in range(4, n):
        new_ans= abs((10 - i) * 2 + 1 + ans[i - 1]) % 1000000000
        ans.append(new_ans)

    return ans

print(test(10))