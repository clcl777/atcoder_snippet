class BIT:
    def __init__(self, N):
        self.N = N
        self.data = [0] * (N + 1)
        self.A = [0] * (N + 1)
        self.all_sum = 0

    def add(self, i, x):
        self.all_sum += x
        self.A[i] += x
        while i <= self.N:
            self.data[i] += x
            i += i & -i

    def update(self, i, x):
        self.add(i, x - self.A[i])

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.data[i]
            i -= i & -i
        return ret

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

    def get(self, i):
        return self.A[i]

    def less_than_x(self, x):
        return self.lower_bound(self.sum(x))

    def moe_than_x(self, x):
        return self.lower_bound(self.sum(x - 1) + 1)

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
        print("[index]", " ".join(map(str, [i for i in range(1, self.N + 1)])))
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
