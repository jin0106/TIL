# 가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,

# 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.

# input x

# output = 에러발생

def multiply(*args):
    result = 1
    for i in args:
        if type(i) != int:
            return "에러발생"

        else:
            result *= i
    return result


print(multiply(1, 2, "4", 3))
