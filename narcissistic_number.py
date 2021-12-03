# A Narcissistic Number is a positive number which is the sum
#  of its own digits, each raised to the power of the number
#  of digits in a given base.
#  In this Kata, we will restrict ourselves to decimal (base 10).
# Your code must return true or false (not 'true' and 'false')
# depending upon whether the given number is a Narcissistic number
# in base 10. This may be True and False in your language


def narcissistic( value ):
    value_list = [digit for digit in str(value)]
    
    cont = 0
    for digit in value_list:
        value_list[cont]= int(digit) ** len(value_list)
        cont += 1

    cont = 0    
    total_value = 0

    for digit in value_list:
        total_value = value_list[cont] + total_value
        cont += 1

    if total_value == value:
        return True
    else:
        return False  

#def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))


if __name__ == '__main__':

    value = narcissistic(371)
    
    print (value)