## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(x):
    x = int (x)
    if x ==2:
        return True
    elif x<2:
        return  False
    else:
        for b in range (2, x-1):
            if (x % b) ==0:
                return False
        return True

#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(z):
    for q in range (1, z+1):
        if z % q ==0:
            print q
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(q):
    largest = 0
    q= int(q)
    for a in range (q+1):
        if is_prime(a):
            largest = a
    return largest
#### End OF MARKER



if __name__ == '__main__':
    print is_prime(499)  # should return True

    print get_largest_prime(10)  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
