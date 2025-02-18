def in_tax(price, tax):
    total = price + (price*tax/100)
    return total

print(in_tax(110 ,10))
