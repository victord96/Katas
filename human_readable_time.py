""" Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59) """

def make_readable(seconds):
    n=0
    s=0
    m=0
    h=0
    while n < seconds:
        if s < 59:
            s = s + 1
        else:
            s = 0
            if m < 59:
                m = m + 1
            else: 
                m = 0
                if h < 99:    
                    h = h + 1
        n = n + 1    
        
    numbers = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
                
    return numbers

#def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)    

if __name__ == '__main__':
    value = make_readable(86400)
    print(value)