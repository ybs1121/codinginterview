import sys

input = sys.stdin.readline

n = int(input())
property = list(map(int, input().split()))

# if property[-1] <= 0:
#     print(property[-1], end=" ")
#     print(property[-2])
#
# elif property[0] >= 0:
#     print(property[0], end=" ")
#     print(property[1])

# else:
left = 0
right = n - 1
min_property = sys.maxsize

min_property_index = [sys.maxsize, sys.maxsize]

while left < right:
    mix_property = property[left] + property[right]

    if abs(min_property) >= abs(mix_property):
        min_property = mix_property
        min_property_index[0] = left
        min_property_index[1] = right

    if mix_property == 0:
        min_property_index[0] = left
        min_property_index[1] = right
        break

    elif mix_property > 0:
        right = right - 1

    else:
        left = left + 1

print(property[min_property_index[0]], end=" ")
print(property[min_property_index[1]])
