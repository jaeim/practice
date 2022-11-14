import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    n_list = [[0 for j in range(n)] for i in range(n)]
    # m_list = [[0 for j in range(m)] for i in range(m)]
    for i in range(n):
        arr = []
        arr = list(map(int, input().split()))
        n_list[i] = arr
    x, y = 0, 0
    flies = []
    while x + m <= n:
        y = 0
        while y + m <= n:
            total = 0
            for i in range(0, m, 1):
                for j in range(0, m, 1):
                    total += n_list[x + i][y + j]
            flies.append(total)
            y += 1
        x += 1
    num = max(flies)
    print('#{0} {1}'.format(test_case, num))
