def conversion(num, base):
    result = 0
    for i in range(len(num)):
        result = result * base + int(num[i])
    return result

def todecimal(num, base):
    decimal = 0
    for a in num:
        decimal = decimal * base + int(a)
    return decimal

def tobase(num, base):
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        rest = num % base
        result = str(rest) + result
        num //= base
    return result

def schooladdition(I1, I2, base):
    n1 = todecimal(I1, base)
    n2 = todecimal(I2, base)
    sum_decimal = n1 + n2
    sum_result = tobase(sum_decimal, base)
    return sum_result

def karatsubamultiplication(I1, I2, base):
    n1 = todecimal(I1, base)
    n2 = todecimal(I2, base)
    productdecimal = n1 * n2
    productresult = tobase(productdecimal, base)
    return productresult

def customdivision(I1, I2, base):
    n1 = todecimal(I1, base)
    n2 = todecimal(I2, base)
    division = n1 // n2
    divisionresult = tobase(division, base)
    return divisionresult

inputline = input().strip().split()

I1 = inputline[0]
I2 = inputline[1]
B = int(inputline[2])

sumresult = schooladdition(I1, I2, B)
productresult = karatsubamultiplication(I1, I2, B)
divisionresult = customdivision(I1, I2, B)

print(sumresult, productresult, divisionresult)










