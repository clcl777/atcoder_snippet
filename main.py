from itertools import combinations
from collections import defaultdict, deque
import sys


# 上限を600000桁に設定（またはそれ以上の桁数に設定）
# sys.set_int_max_str_digits(600000)


def input():
    return sys.stdin.readline()[:-1]


def ceil(A, B):
    return int(-(-A // B))


def floor(A, B):
    return A // B


def round(A, i):
    # 10**iの位で四捨五入
    A += 5 * 10**i
    A = A // (10 ** (i + 1)) * (10 ** (i + 1))
    return A


def find_indexes(char_list, char):
    return [i for i, ltr in enumerate(char_list) if ltr == char]


def find_indexes_2D(A_list, target_value):
    found_indexes = []
    for i in range(len(A_list)):
        for j in range(len(A_list[i])):
            if A_list[i][j] == target_value:
                found_indexes.append((i, j))
    if len(found_indexes) > 0:
        return found_indexes
    else:
        return []


def max_2D(A_list):
    return max(list(map(lambda x: max(x), A_list)))


alphabet = list("abcdefghijklmnopqrstuvwxyz")
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
dydx_4 = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 上下左右
dydx_8 = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [1, 1],
    [-1, 1],
    [1, -1],
    [-1, -1],
]  # 上下左右斜め


def print_2d_list(A):
    for a in A:
        print("".join(map(str, a)))


def transpose(A: list):
    return list(map(list, zip(*A)))


def cumsum(A: list):
    B = [0]
    for a in A:
        B.append(B[-1] + a)
    return B


def get_from_cumsum(cumsum_A: list, l: int, r: int):
    # 半開区間 [l, r) の和を取得
    return cumsum_A[r] - cumsum_A[l]


# 　　　∧＿∧
# 　　 （　´∀｀）
# 　__〇　＿/￣￣￣/
# ,,|＼￣ヽ/　　　　 /＼
# ,,|＼＼　o＝＝＝o　 ＼
# 　　 ＼|￣￣￣￣￣￣ |
# 　　　　|￣￣￣￣￣￣ |


# ----------------------------------------------------------------------------------------------- #
