# 좋은수열

# 데이터 입력
N = int(input())

# 결과 값인 좋은수열
good_sequence = ''

# 백트래킹으로 좋은수열 구하기
def solve(good_sequence):
    # 만족하는 수열의 길이가 되면 출력
    if len(good_sequence) == N:
        print(good_sequence)
        exit(0)
    # 1 ~ 3 사이의 수를 넣어가며 좋은수열인지 검사
    for i in range(1, 4):
        # 수를 더해서 좋은수열이라면
        if checkIsGoodSequence(good_sequence + str(i)):
            # 결과 값에 수를 더함
            solve(good_sequence + str(i))

# 수열이 좋은수열인지 검사
def checkIsGoodSequence(sequence):
    # 뒤에서부터 1개 ~ N // 2 개 씩 짝을지어 짝끼리 값이 같은지 ㄴ비교
    for i in range(1, N // 2 + 1):
        if sequence[-i : ] == sequence[-i * 2 : -i]:
            return False
    return True

solve(good_sequence)