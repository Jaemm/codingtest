# 문자 리스트를 문자열로 변환하기
# 제출 내역
# 문제 설명
# 문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.

# 제한사항
# 1 ≤ arr의 길이 ≤ 200
# arr의 원소는 전부 알파벳 소문자로 이루어진 길이가 1인 문자열입니다.
# 입출력 예
# arr	result
# ["a","b","c"]	"abc"
def solution(arr):
    # join() 메서드를 사용하여 리스트의 모든 원소를 이어 붙임
    return ''.join(arr)

# 예시 테스트
print(solution(["a", "b", "c"]))  # 출력: "abc"