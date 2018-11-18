## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x,guess = 5.0):
	if x < 0.00001:
		return None
	if good_enough(guess,x):
		return guess
	else:
		new_guess = improve_guess(guess,x)
		return sqrt(x , new_guess)
def good_enough(guess,x):
    if abs(guess * guess -x)<0.00001:
        return True
    else:
        return False
#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(x , y):
	a = x * 1.00000
	b = y * 1.00000
	arth_mean =(a + b ) / 2.00000
	return arth_mean
	print("%5f" % arth_mean)
		

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess, x):
	a = guess * 1.00000
	b = x * 1.00000
	if guess < 1.00000:
		return a + 1.00000
	else:
		return average(a, b/a) 
#### End OF MARKER




if __name__ == '__main__':
    print sqrt(36)