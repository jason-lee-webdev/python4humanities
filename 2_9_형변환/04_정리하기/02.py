text = 'price: $3.20'
price = text[8: ]
print(price, type(price))
price = float(price)
print(price, type(price))

# '3.20' 을 int 로 형변환하면?
price = '3.20'
price = int(price)  # ValueError: invalid literal for int() with base 10: '3.20'
# '3.20' 은 int 로 형변환이 불가능하다.
