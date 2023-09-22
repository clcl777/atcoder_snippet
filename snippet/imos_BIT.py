"""
    Fenwick-Tree

    【説明】
        0-indexed

    【コンストラクタ】
        N : 配列のサイズ

    【メソッド】
        add(i)          : A[i] += x
        update(i, x)    : A[i] = x
        sum(i)          : A[0] + A[1] + ... + A[i]
        range_sum(l, r) : A[l] + A[l + 1] + ... + A[r]
        get(i)          : A[i]を取得
        get_all_sum()   : A[0] + A[1] + ... + A[N]
        lower_bound(w)  : A[0] + A[1] + ... + A[i] >= w となる最小のi
        more_than_x(x)  : i >= x && A[i] > 0となる最小のiを取得
        less_than_x(x)  : i <= x && A[i] > 0となる最大のiを取得
        print()         : Aを表示
"""


class BIT:
    def __init__(self, N):
        self.N = N
        self.data = [0] * (N + 1)
        self.A = [0] * (N + 1)
        self.all_sum = 0

    def add(self, i, x):
        if not 0 <= i < self.N:
            raise ("[ERROR] index out of range")
        i += 1
        self.all_sum += x
        self.A[i] += x
        while i <= self.N:
            self.data[i] += x
            i += i & -i

    def update(self, i, x):
        self.add(i, x - self.A[i + 1])

    def sum(self, i):
        if not -1 <= i < self.N:
            raise ("[ERROR] index out of range")
        i += 1
        ret = 0
        while i > 0:
            ret += self.data[i]
            i -= i & -i
        return ret

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

    def get(self, i):
        if not 0 <= i < self.N:
            raise ("[ERROR] index out of range")
        i += 1
        return self.A[i]

    def less_than_x(self, x):
        if not 0 <= x < self.N:
            raise ("[ERROR] index out of range")
        index_1 = self.lower_bound(self.sum(x))
        if index_1 is None:
            return None
        return index_1 - 1

    def more_than_x(self, x):
        if not 0 <= x < self.N:
            raise ("[ERROR] index out of range")
        index_1 = self.lower_bound(self.sum(x - 1) + 1)
        if index_1 is None:
            return None
        return index_1 - 1

    def lower_bound(self, w):
        if w <= 0:
            return None
        if w > self.get_all_sum():
            return None
        i = 0
        size = 1 << self.N.bit_length()
        while size > 0:
            if i + size <= self.N and self.data[i + size] < w:
                w -= self.data[i + size]
                i += size
            size >>= 1
        return i + 1

    def get_all_sum(self):
        return self.all_sum

    def print(self):
        print("[index]", " ".join(map(str, [i for i in range(self.N)])))
        print("[value]", " ".join(map(str, [self.A[i] for i in range(1, self.N + 1)])))


N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

bit = BIT(100000 + 1)
# bit = BIT(max(B) + 1)
for i in range(N):
    bit.add(A[i], 1)
    bit.add(B[i] + 1, -1)
ct = 0
ans_list = []
for i in range(1, 100000 + 1):
    if bit.sum(i) > 0:
        ct += 1
        ans_list.append(ct)
    else:
        ct = 0
print(max(ans_list))
