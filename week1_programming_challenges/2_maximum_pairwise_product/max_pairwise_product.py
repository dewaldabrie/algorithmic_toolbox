# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

largest = 0
second_largest = 0
for num in a:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

result = largest*second_largest


print(result)
