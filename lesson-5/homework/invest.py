def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount += (amount * rate)
        print(f'Year {i}: ${amount:.2f}')
a = int(input("The amount: "))
b = float(input("Rate: "))
c = int(input("Years: "))
invest(a, b, c)