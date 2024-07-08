### 두 가지 방법으로 스크립트의 ? 에 적절한 문장을 채워 봅시다.

### 스크립트
# obj0 = ['a', 'b']
# obj1 = ['c', 'd']
# ?
# print(obj0)

### 실행결과
# ['a', 'b', 'c', 'd']

### 내가 생각한 답
obj0 = ['a', 'b']
obj1 = ['c', 'd']
obj0 += obj1
print(obj0)

### 책
obj0 = ['a', 'b']
obj1 = ['c', 'd']
obj0[2: 2] = obj1
print(obj0)
