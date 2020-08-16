def sum_of_digits(number):
    sum = 0
    while (number != 0):
        sum += number % 10
        number = int(number/10)
    if(sum > 9):
        return sum_of_digits(sum)
    return sum



def digit_root(n): 
    if (not(n)):
        return 0
    return (n - 1) % 9 + 1


print(digit_root(121))