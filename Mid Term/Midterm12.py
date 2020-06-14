# Score 15/25
# You did not create a fucntion that will calculate descriptive statistics.
# You created a script that calls existing functiions.
# Script was also supposed to work on any arbitrary list of numbers.
$ You have "hard-wired" it for 6 numbers.

import statistics

def descriptive():
    number = random.randrange(1, 11)
    return (number)


number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))
number4 = int(input('Enter fourth number: '))
number5 = int(input('Enter fifth number: '))
number6 = int(input('Enter sixth number: '))

values = [number1, number2, number3, number4, number5, number6]  

print ('Mean is: ', statistics.mean(values))
print ('Median is: ', statistics.median(values))
print ('Sample Standard Deviation is: ', statistics.stdev(values))
