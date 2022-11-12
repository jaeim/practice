# 1954.py에서는 while문을 새로 돌때마다 이미 좌표를 이동시켰는데 (그래서 조건문이 여러개..)
# 이미 좌표를 이동시키기 전에 이미 0이 아닌 값이 존재하는지 미리 검사하면 더 효율적일 듯 싶다.
# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    matrix = [[0 for y in range(n)] for x in range(n)]
    # 델타배열
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = 0
    y = 0
    cnt = 1
    total = n * n
    i = 0
    while cnt <= total:
        matrix[x][y] = cnt
        cnt += 1
        x += dx[i]
        y += dy[i]
        if x < 0 or x >= n or y < 0 or y >= n or matrix[x][y] != 0:
            x -= dx[i]
            y -= dy[i]
            i = (i + 1) % 4
            x += dx[i]
            y += dy[i]

    print('#{0}'.format(test_case))
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

