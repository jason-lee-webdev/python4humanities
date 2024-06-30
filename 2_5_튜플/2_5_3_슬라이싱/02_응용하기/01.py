# 슬라이스를 사용해 스크립트의 ?를 적절히 채줘 봅시다.

# 스크립트
# print(('apple', 'banana', 'cherry', 'date')[?])
# print(('Seoul', 'seoul', 'SEOUL', 'seouL')[?])
# print((1, 2, 3, 4)[?])

# 실행결과
# ('banana', 'cherry')
# (Seoul,)
# (1, 2, 3, 4)

# 내가 생각한 답
print(('apple', 'banana', 'cherry', 'date')[1: 3])
print(('apple', 'banana', 'cherry', 'date')[-3: -1])

print(('Seoul', 'seoul', 'SEOUL', 'seouL')[0: 1])
print(('Seoul', 'seoul', 'SEOUL', 'seouL')[-4: -3])
print(('Seoul', 'seoul', 'SEOUL', 'seouL')[: 1])

print((1, 2, 3, 4)[0: 4])  # (1, 2, 3, 4)
print((1, 2, 3, 4)[0:])  # (1, 2, 3, 4)
print((1, 2, 3, 4)[-4: 0])  # ()
print((1, 2, 3, 4)[: 0])  # ()
print((1, 2, 3, 4)[: 4])  # (1, 2, 3, 4)
print((1, 2, 3, 4)[:])  # (1, 2, 3, 4)

# 가장 왼쪽에 위치한 원소는 0을 인덱스로 갖는다.
# 가장 오른쪽에 위치한 원소(-1)의 오른쪽을 가리키는 인덱스는 0이 아니다.
