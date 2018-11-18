## IMPORTS GO HERE

## END OF IMPORTS
### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count (a, essay, c = False):
	f = open (essay, "r")
	lines = f.readlines()
	f.close()

	if (c == False):
		return len(lines) +1

	if (c == True):
		count = 0
		for l in lines:
			t = True
			for i in l:
				if (i != '\n'):
					t = False
			if (t == True):
				count = count + 1

		return (len(lines) - count)
#### End OF MARKER

### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(a, essay, c = False):
	f = open (essay, "r")
	lines = f.readlines()
	f.close()
	total = 0
	for l in lines:
		for i in l:
			total = total + 1

	if (c == False):
		return total

	if (c == True):
		count = 0
		for l in lines:
			for i in l:
				if (i == ' ' or i == '\n'):
					count = count + 1
		return (total - count)
#### End OF MARKER

### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###
def move_lines(essay, out, c):
	f1 = open (essay, "r")
	f2 = open (out, "w")

	for i in range(f1):
			line = f1.readline()
			f2.writeline()

	f1.close()
	f2.close()

#### End OF MARKER

if __name__ == '__main__':
    print line_count('.', 'essay.txt')
    print line_count('.', 'essay.txt', True)

    print character_count('.', 'essay.txt')
    print character_count('.', 'essay.txt', True)

    move_lines('essay.txt', 'out.txt', 3)

    pass
