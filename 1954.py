# 결국 내 힘으로 못푼 문제..
# 델타 배열을 이용하면 쉽게 풀 수 있다.
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# def calc(x, y, i):
#     if x < 0 or y < 0:
#         return
#     if x >= n or y >= n:
#         return
#     if matrix[x][y] != 0:
#         return
#
#     if x == 0 and y == 0:
#         matrix[x][y] = 1
#     if matrix[x][y] == 0:
#         matrix[x][y] = i
#
#     calc(x, y + 1, i + 1)
#     calc(x + 1, y, i + 1)
#     calc(x, y - 1, i + 1)
#     calc(x - 1, y, i + 1)






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
        if x < 0 or x >= n or y < 0 or y >= n:
            x = x - dx[i]
            y = y - dy[i]
            continue
        elif matrix[x][y] != 0:
            # 이미 값이 존재하는 배열을 만났다고 해서 무작정 방향을 틀면 안된다.
            # 무작정 방향을 틀면 12 이후에 값을 넣을 수 없고 무한대로 돌게된다.
            # 값이 존재하는 위치를 만났을 경우, 방향을 틀었을때도 값이 존재하는지 확인 후 값이 또 존재한다면 다시한번 뒤로 back 해야함
            if matrix[x + dx[(i+1) % 4]][y + dy[(i+1) % 4]] != 0:
                x = x - dx[i]
                y = y - dy[i]
            i = i + 1
            i = i % 4
        else:
            matrix[x][y] = cnt
            cnt = cnt + 1
        x = x + dx[i]
        y = y + dy[i]
    print('#{0}'.format(test_case))
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

