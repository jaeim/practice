# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N = int(input())
#     for i in range(1, N + 1):
#         tmp = list(map(int, str(i)))
#         check = ''
#         for j in range(len(tmp)):
#             if tmp[j] == '3' or tmp[j] == '6' or tmp[j] == '9':
#                 check += '-'
#         if check == '':
#             print(i, end=' ')
#         else:
#             print(check, end=' ')

import sys

sys.stdin = open("input.txt", "r")

N = int(input())
for i in range(1, N + 1):
    tmp = list(map(int, str(i)))
    check = ''
    for j in range(len(tmp)):
        if tmp[j] == 3 or tmp[j] == 6 or tmp[j] == 9:
            check += '-'
    if check == '':
        print(i, end=' ')
    else:
        print(check, end=' ')
