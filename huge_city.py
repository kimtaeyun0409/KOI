import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


def find_detour(road, police, cnt):
    res = 0
    p_idx = 0

    for i in range(1, cnt):
        t = []
        t_acc = []
        while p_idx < len(police) and police[p_idx] <= road[i]:
            t.append(police[p_idx])
            if len(t_acc) == 0:
                t_acc.append(police[p_idx])
            else:
                t_acc.append(t_acc[-1] + police[p_idx])
            p_idx += 1

        if len(t) < 2:
            continue
        elif i == 1:
            for j in range(1, len(t)):
                length = road[i] - t[j]
                res += length * j * 2
            continue
        elif i == cnt - 1:
            for j in range(1, len(t)):
                res += (t_acc[j - 1] - road[i - 1] * j) * 2
            continue

        for j in range(1, len(t)):
            length = road[i] - t[j] + road[i - 1]
            mid = (road[i] + road[i - 1]) // 2
            if length > mid:
                res += 2 * (t_acc[j - 1] - j * road[i - 1])
                continue

            idx = bisect_right(t, length, 0, j)
            if idx != 0:
                res += (t_acc[idx - 1] - road[i - 1] * idx) * 2
            res += (length - road[i - 1]) * (j - idx) * 2

    return res


n, m, k = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.extend([-2000000, 2000000])
y.extend([-2000000, 2000000])
x.sort()
y.sort()
xCnt = len(x)
yCnt = len(y)
result = 0

x_pos = []
y_pos = []
for i in range(k):
    a, b = map(int, input().split())
    x_pos.append(a)
    y_pos.append(b)

x_pos.sort()
y_pos.sort()

for i in range(k):
    result += ((2 * i) - k + 1) * x_pos[i]
    result += ((2 * i) - k + 1) * y_pos[i]

result += find_detour(x, x_pos, xCnt)
result += find_detour(y, y_pos, yCnt)

print(result)
