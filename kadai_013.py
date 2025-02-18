def in_tax(price, tax):
    tax = tax*1.1
    total = price + tax
    return total

print(in_tax(110 ,10))
