# 새 원소 삽입1
obj = ['a', 'b', 'c', 'd']
obj[0] = 'z'
print(obj)

# 새 원소 삽입2
obj = ['a', 'b', 'c', 'd']
obj[0] = ['z']
print(obj)

# 새 원소 삽입3
obj = ['a', 'b', 'c', 'd']
obj[0: 0] = ['z']
print(obj)

# <결론>
# 리스트에 새로운 원소를 추가할 때는 인덱싱과 슬라이싱 모두 가능하지만 슬라이싱을 사용하는 것이 안전하다.

# 슬라이싱 한 후 빈 튜플을 저장하면?
obj = ['a', 'b', 'c', 'd', 'e']
obj[3: 3] = []
print(obj)
