## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def is_prime(b):
    b = int (b)
    if b < 2:
        return False
    elif b == 2:
        return True
    else:
        for y in range(2, b - 1):
            if (b % y) == 0:
                return False
        return True
def output_prime_factors(b):
    if type(b) == float:
        b =function(b)
    for p in range(1,b+1):
        if b %p ==0 and is_prime(p):
            print p
def function(b):
    if b%1>= 0.5:
        d = b +1
        d = int(d)
        return d
    else:
        return int (b)

#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(b):
    c = 3
    prime =2
    if b ==1:
        return 2
    while prime < b:
        c = c+2
        if is_prime(c):
            prime = prime + 1
        if type(b) == float:
            return None
    return c
#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(23)
    print get_nth_prime(4)
