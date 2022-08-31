import sys
import copy
input = sys.stdin.readline

n, m = map(int,input().split())
maps = []

answer = 11


for i in range(n):
    maps.append(list(input().rstrip()))


def dfs(coin_map, count, coin1_x,coin1_y, coin2_x,coin2_y):

    global answer

    if count > 10 or answer <= count:
        return

    copy_coin_map = copy.deepcopy(coin_map)

    #상

    coin1_x -= 1
    coin2_x -= 1
    chk = False

    if 0 <= coin1_x < n and 0 <= coin1_y < m and coin_map[coin1_x][coin1_y] != '#':
        coin_map[coin1_x][coin1_y] = 'o'
        coin_map[coin1_x + 1][coin1_y] = '.'
        chk = True

    if 0 <= coin2_x < n and 0 <= coin2_y < m and coin_map[coin2_x][coin2_y] != '#':
        coin_map[coin2_x][coin2_y] = 'o'
        coin_map[coin2_x + 1][coin2_y] = '.'
        chk = True

    if coin1_x < 0 and coin2_x >= 0:
        print(coin1_x)
        print(coin2_x)
        print("a")
        answer = min(answer, count + 1)
        print(answer)
        print("---------")
    elif coin1_x >= 0 and coin2_x < 0:

        answer = min(answer, count + 1)
        print(answer)
        print("----")
    elif coin1_x < 0 and coin2_x < 0:
        pass
    else:

        if chk:
         dfs(coin_map, count + 1, coin1_x, coin1_y, coin2_x, coin2_y)

    coin_map = copy.deepcopy(copy_coin_map)
    coin1_x += 1
    coin2_x += 1

    #하
    coin1_x += 1
    coin2_x += 1
    chk = False

    if 0 <= coin1_x < n and 0 <= coin1_y < m and coin_map[coin1_x][coin1_y] != '#':
        coin_map[coin1_x][coin1_y] = 'o'
        coin_map[coin1_x - 1][coin1_y] = '.'
        chk = True

    if 0 <= coin2_x < n and 0 <= coin2_y < m and coin_map[coin2_x][coin2_y] != '#':
        coin_map[coin2_x][coin2_y] = 'o'
        coin_map[coin2_x - 1][coin2_y] = '.'
        chk = True

    if coin1_x >= n and coin2_x < n:
        answer = min(answer, count + 1)
        print("azzzzz")
    elif coin1_x < n and coin2_x >= n:
        answer = min(answer, count + 1)
        print(coin1_x)
        print(coin2_x)
        print(coin_map)
        print("bzzz")
    elif coin1_x >= n and coin2_x >= n:
        pass

    else:

        if chk:
            dfs(coin_map, count + 1, coin1_x, coin1_y, coin2_x, coin2_y)

    coin_map = copy.deepcopy(copy_coin_map)
    coin1_x -= 1
    coin2_x -= 1

    #좌

    coin1_y -= 1
    coin2_y -= 1
    chk = False
    if 0 <= coin1_x < n and 0 <= coin1_y < m and coin_map[coin1_x][coin1_y] != '#':
        coin_map[coin1_x][coin1_y] = 'o'
        coin_map[coin1_x][coin1_y + 1] = '.'
        chk = True

    if 0 <= coin2_x < n and 0 <= coin2_y < m and coin_map[coin2_x][coin2_y] != '#':
        coin_map[coin2_x][coin2_y] = 'o'
        coin_map[coin2_x][coin2_y + 1] = '.'
        chk = True

    if coin1_y < 0 and coin2_y >= 0:
        answer = min(answer, count + 1)
        print("asd")
    elif coin1_y >= 0 and coin2_y < 0:
        answer = min(answer, count + 1)
        print("asd")
    elif coin1_y < 0 and coin2_y < 0:
        pass
    else:

        if chk:
            dfs(coin_map, count + 1, coin1_x, coin1_y, coin2_x, coin2_y)

    #우
    coin1_y += 1
    coin2_y += 1

    coin_map = copy.deepcopy(copy_coin_map)
    coin1_y += 1
    coin2_y += 1
    chk = False
    if 0 <= coin1_x < n and 0 <= coin1_y < m and coin_map[coin1_x][coin1_y] != '#':
        coin_map[coin1_x][coin1_y] = 'o'
        coin_map[coin1_x][coin1_y - 1] = '.'
        chk = True

    if 0 <= coin2_x < n and 0 <= coin2_y < m and coin_map[coin2_x][coin2_y] != '#':
        coin_map[coin2_x][coin2_y] = 'o'
        coin_map[coin2_x][coin2_y - 1] = '.'
        chk = True

    if coin1_y < m and coin2_y >= m:
        answer = min(answer, count + 1)
        print("c")
    elif coin1_y >= m and coin2_y < m:
        answer = min(answer, count + 1)
        print("d")
    elif coin1_y >= m and coin2_y >= m:
        pass
    else:

        if chk:
            dfs(coin_map, count + 1, coin1_x, coin1_y, coin2_x, coin2_y)



coins = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'o':
            coins.append(i)
            coins.append(j)


dfs(maps, 0, coins[0], coins[1], coins[2], coins[3])

if answer == 11:
    print(-1)
else:
    print(answer)