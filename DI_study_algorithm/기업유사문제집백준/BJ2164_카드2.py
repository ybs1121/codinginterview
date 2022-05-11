import sys
from collections import deque
input = sys.stdin.readline

x = int(input())

cards = [i+1 for i in range(x)]

cards = deque(cards)

print(cards)

while len(cards) > 1:
    cards.popleft()
    top = cards.popleft()
    cards.append(top)

print(cards[0])
