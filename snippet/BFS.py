# キューをインポート
from collections import deque

# 入力を受け取る。座標の調整のため、スタート地点とゴール地点の座標を-1する。
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 迷路の情報を配列Gで受け取る
G = [input() for _ in range(R)]

# キューをQに入れ、スタート地点を追加
Q = deque()
Q.append([sy, sx])

# 未訪問と始点からの距離を管理するdistを定義。スタート地点に0を代入。
dist = [[-1]*C for _ in range(R)]
dist[sy][sx] = 0

# 今回は移動する４方向を事前に用意した。
dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# キューの要素がなくなるまで処理を繰り返す。
while len(Q) > 0:
    y, x = Q.popleft()

    # 移動先で繰り返し処理
    for dy, dx in dirc:
        y2 = y + dy
        x2 = x + dx

        # 移動先が迷路の範囲内でなければ、continue
        if not (0 <= y2 < R and 0 <= x2 < C):
            continue

        # 移動先が壁だったら、continue
        if G[y2][x2] == "#":
            continue

        # 移動先が未訪問なら移動前の距離＋１をdistに入れて、キューに移動先の座標を追加
        if dist[y2][x2] == -1:
            dist[y2][x2] = dist[y][x] + 1
            Q.append([y2, x2])

# ゴールの距離を出力
print(dist[gy][gx])
