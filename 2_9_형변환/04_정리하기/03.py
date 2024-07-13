text = 'price: $3.20'
price = text[7: ]
price = float(price)
print(price, type(price))  # ValueError: could not convert string to float: '$3.20'
