# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해

# 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.

# input x
# output = [2, 4, 6, 8, 10]

list_1 = list(range(1, 11))


print(list(filter(lambda x: x % 2 == 0, list_1)))
