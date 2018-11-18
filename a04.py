## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(FinalGrad):
    if FinalGrad >= 90 and FinalGrad <= 100:
        return("A+")
    elif FinalGrad >=86 and FinalGrad <= 90:
        return("A")
    elif FinalGrad >=82 and FinalGrad <= 86:
        return("A-")
    elif FinalGrad >=78 and FinalGrad <= 82:
        return("B+")
    elif FinalGrad >=74 and FinalGrad <= 78:
        return("B")
    elif FinalGrad >=70 and FinalGrad <= 74:
        return("B-")
    elif FinalGrad >=66 and FinalGrad <= 70:
        return("C+")
    elif FinalGrad >=62 and FinalGrad <= 66:
        return("C")
    elif FinalGrad >=58  and FinalGrad <= 62:
        return("C-")
    elif FinalGrad >=54 and FinalGrad <= 58:
        return("D+")
    elif FinalGrad >=50 and FinalGrad <= 54:
        return("D")
    else:
        return("F")
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####

def variable(grades):
    if grades == "A" :
        return 4.00
    elif grades == "A-" :
        return 3.67
    elif grades == "B+" :
        return 3.33
    elif  grades == "B" :
        return 3.00
    elif  grades == "B-" :
        return 2.67
    elif  grades == "C+" :
        return 2.33
    elif  grades == "C" :
        return 2.00
    elif  grades == "C-" :
        return 1.67
    elif  grades == "D+" :
        return 1.33
    elif   grades == "D" :
        return 1.00
    elif grades == "F":
        return 0.00
def calculate_sgpa(grade1,grade2,grade3):
    total_marks = 0
    total_number_of_subject = 0
    if not grade1 == 'nothing':
        total_number_of_subject = total_number_of_subject + 1
        total_marks = total_marks + variable(grade1)
    if not grade2 == 'nothing':
        total_number_of_subject = total_number_of_subject + 1
        total_marks = total_marks + variable(grade2)
    if not grade3 == 'nothing':
        total_number_of_subject = total_number_of_subject + 1
        total_marks = total_marks + variable(grade3)
    if total_number_of_subject is 0:
        return 0
    sgpa = total_marks / total_number_of_subject
    return sgpa

#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
