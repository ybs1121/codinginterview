N = int(input())
data = list(map(str, input().split()))


def checkRange(x, y, N):
    if 1 <= x <= N and 1 <= y <= N:
        return True
    else:
        return False


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x = 1
y = 1

for i in range(len(data)):
    command = data[i]
    if 'R' == command:
        if checkRange(x + dx[1], y + dy[1], N):
            x += dx[1]
            y += dy[1]
    elif 'L' == command:
        if checkRange(x + dx[3], y + dy[3], N):
            x += dx[3]
            y += dy[3]
    elif 'U' == command:
        if checkRange(x + dx[0], y + dy[0], N):
            x += dx[0]
            y += dy[0]
    elif 'D' == command:
        if checkRange(x + dx[2], y + dy[2], N):
            x += dx[2]
            y += dy[2]
    else:
        pass

print(str(x) + ' ' + str(y))
