def to_wei(value, precision=6):
    return value*10**precision

def from_wei(value, precision=6):
    return value/(10**precision)

def calc_decimal_precision(val, num):
    num = 10**num
    newAmount = val/num
    return newAmount

#create: unnecessary. use the value directly
#totalSum: use sum()
#plus: use +
