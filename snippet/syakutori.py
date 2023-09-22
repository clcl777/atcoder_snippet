# while right < N and 次の条件を満たすかどうか:
N = int(input())
A = list(map(int, input().split()))

right = 0
tot = 0
ct = 0
for left in range(N):
    while right < N and tot ^ A[right] == tot + A[right]:
        tot += A[right]
        right += 1
    ct += right - left
    if right == left:
        right += 1
    else:
        tot -= A[left]

print(ct)

# ------------------------------ #

N = int(input())
a = list(map(int, input().split()))

right = 1
ct = 0
for left in range(N):
    if right == left:
        right += 1
    while right < N and a[right - 1] < a[right]:
        right += 1
    ct += right - left
    tmp = 1
print(ct)

# ------------------------------ #
N, K = map(int, input().split())
S = []
for i in range(N):
    s = int(input())
    S.append(s)

right = 0
tot = 1
ans_list = []
for left in range(N):
    while right < N and tot * S[right] <= K:
        tot *= S[right]
        right += 1
    ans_list.append(right - left)
    if right == left:
        right += 1
    else:
        tot //= S[left]

print(max(ans_list))

# ------------------------------ #

from collections import deque

N = int(input())
A = list(map(int, input().split()))

right = 0
ans_list = []
que = deque()
array_set = set()
for left in range(N):
    while right < N and not A[right] in array_set:
        que.append(A[right])
        array_set.add(A[right])
        right += 1
        debug = 1
    ans_list.append(len(que))
    tmp = que.popleft()
    array_set.remove(tmp)
    debug = 1

print(max(ans_list))
