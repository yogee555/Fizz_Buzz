# Fizz Buzz problems is a classic

for number in range(50):                                        # take range 50 number
    if number % 3 ==0 and number %5 ==0:                        # integer is divisible by 3 & 5 print Fizz Buzz
        print("Fizz Buzz")
    elif number %3 == 0:                                        # integer is divisible by 3 print Fizz
        print("Fizz")
    elif number %5 ==0:                                         # integer is divisible by 5 print Buzz
        print("Buzz")
    else:                                                       # not divisible both value print number
        print(number)