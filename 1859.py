# SW Expert Academy 1859
# import sys
# sys.stdin = open("input.txt", "r")
cases = int(input())
# int 형은 for문에 쓸 수 없다.. range로 감싸줄 것
for case in range(cases):
    days = int(input())
    pr_list = list(map(int, input().split()))
    money = 0
    shop_list = []
    day = 0
    for price in pr_list:
        day += 1
        # 안사고 안판다 0 산다 1 판다 2
        act = 0
        for i in range(day, days):
            if pr_list[i] > price:
                act = 1
                break
            if i == days-1:
                # 경우 1)배열 다 뒤져도 당일 판매가보다 작거나 같은 가격밖에 없으면? 안사고 안팔아야함
                # 경우 2)배열 다 뒤져서 내가 젤 큰놈이고 shop_list가 안비워져 있으면? 안사고 팔아야함
                # 결국 경우1과 2가 같은 뜻인데 차이점은 쇼핑리스트가 비워졌나 안비워졌나 차이..안비워졌으면 내가 가장 큰놈이라는 뜻
                if shop_list:
                    act = 2
        if act == 1:
            shop_list.append(price)
        elif act == 2 or (day == days and shop_list):
            # or 뒤의 조건문: 가장 마지막 배열일때 처리가 추가되어야함 왜냐면 마지막 날은 위의 for문을 못돌리니까 (shop_list에 남은놈 있으면 다 팔아버리기)
            # 판매
            for i in shop_list:
                money += price - i
            # 쇼핑리스트 초기화
            shop_list.clear()
    print('#{0} {1}'.format(case + 1, money))








