# 탑

n = int(input())
data = list(map(int, input().split(' ')))
stack = []
result = []

for index, value in enumerate(data):
    while True:
        if len(stack) == 0:
            result.append(0)
            break
        if stack[-1][1] > value:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    stack.append([index, value])

for i in result:
    print(i, end=' ')