def dig_pow(num,p):
    total = 0
    for index,item in enumerate(str(num)):
        total += int(item) ** (p + index)
    k = int(total / num)
    return k if total % num == 0 else -1


print(dig_pow(1,1))