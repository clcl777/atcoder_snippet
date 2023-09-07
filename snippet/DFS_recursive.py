import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')


H, W = map(int, input().split())
C = [list(list(input())) for _ in range(H)]  # 文字列を二次元listに格納

flag_list = [[False] * (W) for _ in range(H)]


def research(x, y):
    if (x < 0 or x >= W or y < 0 or y >= H or C[y][x] == '#'):
        return
    if (flag_list[y][x]):
        return
    flag_list[y][x] = True
    if (C[y][x] == 'g'):
        print("Yes")
        exit()
    research(x+1, y)
    research(x-1, y)
    research(x, y+1)
    research(x, y-1)


flag_set = set()
ans_list = []


def research2(n):
    if (n in flag_set):
        return
    # flag_list[n] = True
    flag_set.add(n)
    global ans
    ans = max(ans, n)
    ans_list.append(n)
    for i in graph[n]:
        research(i)
    ans_list.append(n)


def find_index_2d(my_list, target):
    for i, x in enumerate(my_list):
        if target in x:
            return (i, x.index(target))
    raise ValueError("'{target}' is not in list".format(target=target))


y_start, x_start = find_index_2d(C, 's')
# y_goal, x_goal = find_index_2d(C, 'g')
research(x_start, y_start)
print("No")
