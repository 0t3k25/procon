# 一旦飛ばす今の自分には難しい。
N, M = map(int, input().split())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))

L.sort(key=lambda x: x[0])

# for i in range(N):
#     for j in range(N+1):
