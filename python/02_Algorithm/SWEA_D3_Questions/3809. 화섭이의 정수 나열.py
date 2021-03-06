# 화섭이는 다음과 같은 흥미로운 추측에 대해 들었다.
#
# “모든 정수는 π = 3.14159265…의 어떤 연속한 부분으로 나타난다.”
#
# 화섭이는 π에 대해 이것을 테스트해 보기는 힘들다고 생각했고, 그냥 유한한 정수열에 대해서 위처럼 연속한 부분을 끊어내어 보았다.
#
# 예를 들면 “3 0 1”같은 정수열로는 3, 0, 1, 30, 301을 만들 수 있다.
#
# 화섭이는 주어진 정수열로 만들 수 없으면서 가장 작은 정수가 무엇인지 궁금해졌다.
#
# 이를 구하는 프로그램을 작성하라. 위의 예에서는 0, 1은 나타나지만 2는 나타나지 않으므로 2가 답이 된다.
#
# 두 번째 테스트케이스를 예로 들면,
#
#
# 위 그림과 같이 0부터 11까지의 정수는 만들 수 있으나 12를 만들 수 없다. 그러므로 12가 답이 된다.
#
#
# [입력]
#
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#
# 각 테스트 케이스의 첫 번째 줄에는 N(1 ≤ N ≤ 103)이 주어진다.
#
# 다음으로는 N개의 정수 d1, d2, …, dN (0 ≤ di ≤ 9)이 순서대로 주어진다.
#
# d들은 공백 하나 또는 줄바꿈으로 구분되어 있다.
#
#
# [출력]
#
# 각 테스트 케이스마다 만들어낼 수 없는 가장 작은 정수를 출력한다.


import sys
sys.stdin = open('input_1.txt','r')
def min_num(a):
    num =0      # 숫자 0 부터 시작
    while 1:
        if str(num) not in a:   # 입력을 str로 받아줬으므로 str(num)으로 (a)에 있는지 확인 없으면 바로 그 값을 return
            break
        else:           # 있다면 +1 해주면서 찾을 때 까지 반복
            num +=1
    return num

T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = ''       # 빈 문자열 생성
    while True:
        nums += ''.join(map(str, input().split()))      # 줄 바꿔서 입력받기
        if len(nums)== N:       # nums의 길이가 N과 같다면 입력 멈춤
            break
    print(f'#{t} {min_num(nums)}')

