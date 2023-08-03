import pypyjit
from collections import Counter
import collections
import sys
import heapq
import copy
from itertools import product
import itertools
import bisect
from functools import lru_cache, cmp_to_key
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')


def input(): return sys.stdin.readline()[:-1]


# def ceil(A, B): return (A - 1 + B) // B

def ceil(A, B): return int(-(-A//B))


def floor(A, B): return A // B
# 10**iの位で切り下げ
# A//10**i*10**i


def round(A, i):
    # 10**iの位で四捨五入
    A += 5*10**i
    A = A//(10**(i+1))*(10**(i+1))
    return A


N = int(input())

N, M = map(int, input().split())

S = list(map(int, input().split()))

W = list(map(str, input().split()))  # 文字列

A = [list(map(int, input().split())) for _ in range(N)]

A, B = zip(*[map(int, input().split()) for _ in range(N)])  # 縦一次元リスト二つに分ける

l, S = map(list, zip(*[map(int, input().split()) for _ in range(N)]))  # 縦一次元リストと二次元リストに分ける

A = [list(list(input())) for _ in range(N)]  # 文字列を二次元listに格納

A = [list(input()) for _ in range(N)]  # 文字列をlistに格納

S_P = [[s, int(p)] for s, p in (input().split() for _ in range(N))]  # 文字列と数値を分けてlistに格納

C = Counter(map(int, input().split()))  # 出現回数をカウント
ans = 0
for c in C:
    ans += C[c]//2

print(*S)
array = []
ans = []
for i in range(N):
    heapq.heappush(array, A[i])
for i in range(N):
    value = heapq.heappop(array)
    ans.append(value)

array = [1, 2, 3, 4, 5]
array2 = array[:]
arraay2 = array.copy()
array_2D = [[1, 2, 3], [4, 5, 6]]
array2_2D = copy.deepcopy(array_2D)

flag_list = [[False] * (M) for _ in range(N)]  # N✖️Mの2次元配列を作成

DP = [[0 for _ in range(M)] for _ in range(N)]  # N✖️Mの2次元配列を作成

array_2D_transpose = list(zip(*array_2D))  # 二次元listの転置

ist_2d = [[] for _ in range(N)]

two_d_list = [[1, 2], [3, 4], [5, 6], [1, 2], [3, 4]]  # 二次元リスト
# 各サブリストをタプルに変換し、セットに追加
two_d_set = set(tuple(sublist) for sublist in two_d_list)
print(two_d_set)  # {(5, 6), (1, 2), (3, 4)}


def add_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")
    return [a + b for a, b in zip(list1, list2)]


for pro in product((0, 1), repeat=N):  # 全bit探索
    print(pro)

A_all = list(itertools.permutations(A))  # 順列全探索

INF = 10 ** 18


def find_indexes(char_list, char):
    return [i for i, ltr in enumerate(char_list) if ltr == char]


# def find_indexes_2D(A_list, target):
#     for i, x in enumerate(A_list):
#         if target in x:
#             return (i, x.index(target))
#     raise ValueError("'{target}' is not in list".format(target=target))

def find_indexes_2D(A_list, target_value):
    found_indexes = []
    for i in range(len(A_list)):
        for j in range(len(A_list[i])):
            if A_list[i][j] == target_value:
                found_indexes.append((i, j))
    if len(found_indexes) > 0:
        return found_indexes
    else:
        raise ValueError(f"Value {target_value} not found in the given matrix.")


def max_2D(A_list):
    return max(list(map(lambda x: max(x), A_list)))


alphabet = set("abcdefghijklmnopqrstuvwxyz")

dydx = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 上下左右
dydx = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]  # 上下左右斜め


def comp(S, T):
    a, b, i = S
    aa, bb, ii = T
    if a * (aa + bb) == aa * (a + b):
        return -1 if i > ii else 1
    return -1 if a * (aa + bb) < aa * (a + b) else 1


C.sort(key=cmp_to_key(comp))

ans = bisect.bisect_right(A, M)
left = 0
right = N - 1
while right - left > 1:
    mid = (left + right) // 2
    if A[mid] < M:
        left = mid
    else:
        right = mid
ans = right


def check(k):
    return sum(k >= a for a in A) >= sum(k <= b for b in B)


ok = 10 ** 9 + 10
ng = 0
while ok - ng > 1:
    mid = ok + ng >> 1
    if check(mid):
        ok = mid
    else:
        ng = mid


# 与えられた文字列の各文字の出現回数をカウント
w = input()
dict_str = {}
for i in range(len(w)):
    dict_str[w[i]] = dict_str.get(w[i], 0) + 1

for value in dict_str.values():
    pass

# 隣接リスト 辺重みなし
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す
print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]


# 隣接リスト 辺重みあり
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])  # 有向グラフなら消す
print(graph)  # [[2, 3], [3, 1], [5, 9]], ..., [...]]


class Compress:
    # 座標圧縮
    def __init__(self, A, indexed=0):
        self.compress = {}
        self.original = {}
        for i, e in enumerate(sorted(set(A))):
            self.compress[e] = i + indexed
            self.original[i + indexed] = e

    def get_compress(self, A):
        if type(A) == list:
            return [self.compress[e] for e in A]
        if type(A) == int:
            return self.compress[A]

    def get_original(self, A):
        if type(A) == list:
            return [self.original[e] for e in A]
        if type(A) == int:
            return self.original[A]
# a,bの最大公約数


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# a,bの最小公倍数


def lcm(a, b):
    return a * b // gcd(a, b)


def prime_factorize(n):
    if n < 1:
        raise ValueError("nは1以上の整数を入力してください")
    if n == 1:
        return [1]
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


c = collections.Counter(prime_factorize(840))
