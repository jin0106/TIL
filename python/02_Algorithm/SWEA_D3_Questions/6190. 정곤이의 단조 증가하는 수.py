# 정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.
#
# 그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
#
# 어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.
#
# 예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
#
# 양의 정수 N 개 A1, …, AN이 주어진다.
#
#  1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.
#
#
# [입력]
#
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.
#
# 두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.
#
#
# [출력]
#
# 각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.
#
# 만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.

def danjo(a):
    a = str(a)
    for x in range(len(a)-1):   # 하나라도 앞에 숫자가 더 크면 False
        if a[x] > a[x+1]:
            return False
    return True

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    max_multi = -1  # 답을 -1로 미리 선언

    for i in range(N):
        for j in range(i+1,N):
            multi = num_lst[i] * num_lst[j]     # 값들 곱하기
            if danjo(multi) and multi > max_multi:  # 곱한 값이 단조가 맞고 최대값이 맞는지 확인
                max_multi = multi   # 위의 조건을 충족하면 max_multi를 바꿔줌

    print(f"#{t} {max_multi}")

