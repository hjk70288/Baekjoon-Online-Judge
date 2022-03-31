# 암호 만들기
import sys
from itertools import combinations

# 데이터 입력
l, c = map(int, sys.stdin.readline().split(' '))
alpha = sorted(list(sys.stdin.readline().strip().split(' ')))

# 정렬된 알파벳으로 l 길이의 모든 조합 생성
for password in list(combinations(alpha, l)):
	# Tupple To List
	password = list(password)

	# 모음이 하나라도 포함된다면
	if 'a' in password or 'e' in password or 'i' in password or 'o' in password or 'u' in password:
		# List To String
		passwordString = ''.join(password)
 		
		# 모음을 제거
		for i in 'aeiou':
			if i in password:
				password.remove(i)

		# 모음을 제거한 후(자음만 있는 경우) 길이가 2 이상이라면 출력
		if len(password) >= 2:
			print(passwordString)
		