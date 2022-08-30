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

    copy_coin_map = copy.deepcopy(coin_map)

    #상
    if coin1_x > coin2_x:
        if 0 <= coin1_x - 1 < n and 0 <= coin1_y < m and coin_map[coin1_x - 1][coin1_y] != '#':
            coin_map[coin1_x - 1][coin1_y] = 'o'
            coin_map[coin1_x][coin1_y] = '.'
            coin1_x -= 1

        if 0 <= coin2_x - 1 < n and 0 <= coin2_y < m and coin_map[coin2_x - 1][coin2_y] != '#':
            coin_map[coin2_x - 1][coin2_y] = 'o'
            coin_map[coin2_x][coin2_y] = '.'
            coin2_x -= 1

            dfs(coin_map, count + 1, coin1_x,coin1_y,coin2_x,coin2_y)
            coin_map = copy.deepcopy(copy_coin_map)

        elif 0 > coin1_x - 1:
            answer = min(answer, count + 1)
    else:
        if 0 <= coin2_x - 1 < n and 0 <= coin2_y < m and coin_map[coin2_x - 1][coin2_y] != '#':
            coin_map[coin2_x - 1][coin2_y] = 'o'
            coin_map[coin2_x][coin2_y] = '.'
            coin2_x -= 1

        if 0 <= coin1_x - 1 < n and 0 <= coin1_y < m and coin_map[coin1_x - 1][coin1_y] != '#':
            coin_map[coin1_x - 1][coin1_y] = 'o'
            coin_map[coin1_x][coin1_y] = '.'
            coin1_x -= 1

            dfs(coin_map, count + 1, coin1_x, coin1_y, coin2_x, coin2_y)
            coin_map = copy.deepcopy(copy_coin_map)





    #하

    #좌

    #우



coins = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'o':
            coins.append((i,j))


dfs(maps,0,coins[0],coins[1],coins[2],coins[3])