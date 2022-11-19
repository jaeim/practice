# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        case[i] = list(map(int, input().split()))
    rslt = 1
    # while문은 굳이 없어도 될듯..
    while rslt > 0:
        # 가로줄 체크
        for i in range(9):
            check = [0 for x in range(10)]
            for j in range(9):
                check[case[i][j]] += 1
                if check[case[i][j]] > 1:
                    rslt = 0
                    break;
            if rslt <= 0:
                break;
        if rslt > 0:
            # 세로줄 체크
            for i in range(9):
                check = [0 for x in range(10)]
                for j in range(9):
                    check[case[j][i]] += 1
                    if check[case[j][i]] > 1:
                        rslt = 0
                        break;
                if rslt <= 0:
                    break;
        if rslt > 0:
            # 3 * 3 배열 체크
            for x in range(0, 9, 3):
                for y in range(0, 9, 3):
                    check = [0 for x in range(10)]
                    for i in range(3):
                        for j in range(3):
                            check[case[x + i][y + j]] += 1
                            if check[case[x + i][y + j]] > 1:
                                rslt = 0
                                break;
                        if rslt <= 0:
                            break;
                    if rslt <= 0:
                        break;
                if rslt <= 0:
                    break;
        print('#{0} {1}'.format(test_case, rslt))
        break;







