# 곱하는 수가 0 or 1이 아니면 무조건 곱하는게 이득

m = "02984"

m_len = len(m)
res = 0
for i in range(m_len):
    a = int(m[i])

    if res < 1 or a < 0:
        res += a
    else:
        res *= a


print(res)



