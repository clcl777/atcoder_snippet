H, W = map(int, input().split())
C = [list(list(input())) for _ in range(H)]  # 文字列を二次元listに格納

flag_list = [[False] * (W) for _ in range(H)]


def find_index_2d(my_list, target):
    for i, x in enumerate(my_list):
        if target in x:
            return (i, x.index(target))
    raise ValueError("'{target}' is not in list".format(target=target))


y_start, x_start = find_index_2d(C, 's')
# y_goal, x_goal = find_index_2d(C, 'g')
stack = [[y_start, x_start]]
while stack:
    y, x = stack.pop()
    if x < 0 or x >= W or y < 0 or y >= H or C[y][x] == '#':
        continue
    if flag_list[y][x]:
        continue
    if C[y][x] == 'g':
        print("Yes")
        exit()
    flag_list[y][x] = True
    stack.append([y+1, x])
    stack.append([y-1, x])
    stack.append([y, x+1])
    stack.append([y, x-1])
print("No")
