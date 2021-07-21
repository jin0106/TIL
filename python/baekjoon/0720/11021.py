T = int(input()) # T숫자 받기

for i in range(1,T+1): # Case1번부터 시작해야되니 시작값과 마지막값에 +1 해주기
    a,b = map(int, input().split())
    print("Case #{}: {}".format(i, a+b))