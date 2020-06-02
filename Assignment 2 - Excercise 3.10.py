# Exercise 3.10
principal = 1000.0
rate = 0.07

for year in range(1, 31):
    print(f'Amount after {year} year(s): {principal * (1 + rate) ** year:}')