"""Create a function that takes a Roman numeral
 as its argument and returns its value as
 a numeric decimal integer. You don't need to
 validate the form of the Roman numeral."""

def solution(roman):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(roman)):
            if i > 0 and rom_val[roman[i]] > rom_val[roman[i - 1]]:
                int_val += rom_val[roman[i]] - 2 * rom_val[roman[i - 1]]
            else:
                int_val += rom_val[roman[i]]
        return int_val



if __name__ == '__main__':

    value = solution('XXI')
    
    print (value)        