obj0 = {[0, 1], [2, 3]}
print(obj0)  # TypeError: unhashable type: 'list'

### 궁금한 점
# 리스트 요소를 갖는 집합은 생성할 수 없습니다.
# 집합의 요소는 반드시 변경 불가능한(immutable) 타입이어야 하기 때문입니다.
# 리스트는 변경 가능한(mutable) 타입이므로 집합의 요소로 사용할 수 없습니다.