# 튜플 생성
my_tuple = (1, 2, 3)

# 튜플의 요소를 변경하려고 시도
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")

# 튜플의 요소를 삭제하려고 시도
try:
    del my_tuple[1]
except TypeError as e:
    print(f"Error: {e}")

# 결과 출력
print("튜플의 현재 상태:", my_tuple)
