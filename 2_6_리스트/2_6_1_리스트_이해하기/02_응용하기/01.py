### 인덱스와 슬라이스를 사용해 스크립트의 ?를 적절히 채워 봅시다.

### 스크립트
# obj = ['a', 'b', 'c', 'd']
# print(obj[?])
# print(obj[?])
# print(obj[?] + obj[?])

### 실행결과
# ['a', 'b' ,'c', 'd']
# b
# ['a', 'c']

### 내가 생각한 답
obj = ['a', 'b', 'c', 'd']
print(obj[:])
print(obj[1])
print(obj[0: 1] + obj[2: 3])
