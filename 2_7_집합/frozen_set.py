# frozenset은 변경 불가능한 집합입니다.
# 이를 사용하면 집합의 요소로 집합을 저장할 수 있습니다.

### frozenset을 사용하여 집합의 요소로 집합 저장
set_of_sets = {frozenset({1, 2})}
print(set_of_sets, type(set_of_sets))  # {frozenset({1, 2})} <class 'set'>

### 파이썬에서 집합(set)에 요소를 추가하는 방법
# 파이썬에서 집합(set)에 요소를 추가하는 방법은 add() 메서드를 사용하는 것입니다.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# 여러 요소를 한 번에 추가하려면 update() 메서드를 사용할 수 있습니다:
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)
