# Exercise 4.9
def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print(f'Fahrenheit{"Celsius":>10}')

for celsius in range(0,101):
    print(f'{celsius:6}{fahrenheit(celsius):12.1f}')
