price = float(input("Enter a price: "))
dollars = int(price)
cents =  int((price - dollars) * 100 + 0.5)

# print(dollars, "dollars", cents, "cents")
print(f"{dollars} dollars {cents} cents")
