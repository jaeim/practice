# 문제 자체를 이해 못해서 정답 참고했다.
# 0010011 같은 문자열 타입의 2진수를 10진수로 바꾸는 방법: int(0010011, 2)
# zfill(): 원하는 자리수 만큼을 앞에 0으로 채워 길이를 맞추는 방법
# chr(): 해당 정수에 해당하는 유니코드 문자를 반환한다.
# int(): 다른 진수의 문자열을 숫자형(10진수)로 변환한다.
# format(): 접두어를 제외하며 숫자를 다른진수로 변환 가능 (#b, #o..이렇게 매개변수를 주면 접두어도 가져올 수 o)


# import sys
# sys.stdin = open("input.txt", "r")

# 표 1
decode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
          ]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_str = input()
    output_str = ''
    num = -1
    bit_num = []
    bit_rslt = ''
    # 입력받은 글자를 표1을 기반으로 index를 받아온다. ex) A라면 num은 index가 0
    for i in range(len(input_str)):
        num = decode.index(input_str[i])
        # 받아온 num을 format 함수를 통해 2진수로 변환 & zfill 함수로 6자리를 0으로 채워준다.
        bit_rslt += str(format(num, 'b').zfill(6))
    # 24비트를 8비트씩 끊어주기
    for i in range(0, len(bit_rslt), 8):
        # slice를 통해 8bit씩 끊은 후, int 함수를 통해 10진수로 변환한다. (int함수의 2는 매개변수가 2진수임을 나타냄)
        tmp = int(bit_rslt[i: i + 8], 2)
        # 10진수로 받아온 결과값을 chr 함수를 통해 해당 정수에 해당하는 유니코드 문자를 반환한다.
        output_str += chr(tmp)
    print('#{0} {1}'.format(test_case, output_str))




