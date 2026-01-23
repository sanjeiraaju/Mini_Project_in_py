food = []
price = []

while True:
    am = str(input('Enter the food to buy (or Q to quit): '))
    if am.lower() == "q":
        break
    else:
        prices = float(input(f'The price of {am}: $'))
        price.append(prices)
        food.append(am)

    for i in food:
        print(i, end=' ')
    print()

    for j in price:
        print(j, end=' ')
    print()

total = sum(price)
print(f"\nTotal Bill: ${total}")
