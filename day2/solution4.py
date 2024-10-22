# 홀짝 구분하기
# 제출 내역
# 문제 설명
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ n ≤ 1,000
# 입출력 예
# 입력 #1

# 100
# 출력 #1

# 100 is even
# 입력 #2

# 1
# 출력 #2

# 1 is odd

# 입력 받기
n = int(input())

# 제한사항 확인
if 1 <= n <= 1000:
    # 홀짝 구분하여 출력
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
else:
    print("입력 값이 제한사항을 초과했습니다.")