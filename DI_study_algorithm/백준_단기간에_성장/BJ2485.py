x = int(input())

dice = []
money = []
for i in range(x):
    tmp = list(map(int,input().split()))
    dice.append(tmp)


from collections import Counter

for i in range(x):
    cnt = Counter(dice[i])

    two = 0
    one = 0
    max_dice = 0
    for k,v in cnt.items():
        if max_dice < k:
            max_dice = k

        if v == 4:
            personal_money = 50000 + 5000 * k
            money.append(personal_money)
        if v == 3:
            personal_money = 10000 + 1000 * k
            money.append(personal_money)
        if v == 2:
            two += 1
        if v == 1:
            one += 1
    if two == 2:
        personal_money = 2000
        for k, v in cnt.items():
            personal_money += 500*k
        money.append(personal_money)

    else:
        for k, v in cnt.items():
            if v == 2:
                personal_money = 1000 + 100 * k
                money.append(personal_money)


    if one == 4:
        personal_money = max_dice * 100
        money.append(personal_money)

print(max(money))








