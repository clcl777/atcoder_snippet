from itertools import combinations
import more_itertools
from collections import deque
import sys


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

# 　　　∧＿∧
# 　　 （　´∀｀）
# 　__〇　＿/￣￣￣/
# ,,|＼￣ヽ/　　　　 /＼
# ,,|＼＼　o＝＝＝o　 ＼
# 　　 ＼|￣￣￣￣￣￣ |
# 　　　　|￣￣￣￣￣￣ |


# ----------------------------------------------------------------------------------------------- #
