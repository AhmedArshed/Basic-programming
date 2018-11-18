## IMPORTS GO HERE
## END OF IMPORTS
### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def get_grade(FinalGrad):
    if FinalGrad == "A+":
        return(4.00) 
    elif FinalGrad == "A":
        return(4.00)
    elif FinalGrad == "A-":
        return(3.67)
    elif FinalGrad == "B+":
        return(3.33)
    elif FinalGrad == "B":
        return(3.00)
    elif FinalGrad == "B-":
        return(2.67)
    elif FinalGrad == "C+":
        return(2.33)
    elif FinalGrad == "C":
        return(2.00)
    elif FinalGrad == "C-":
        return(1.67)
    elif FinalGrad == "D+":
        return(1.33)
    elif FinalGrad == "D":
        return(1.00)
    else:
        return(0.00)

def calculate_sgpa(x):
    total_marks = 0
    get_grade == []
    
    if type(x) == list:
        total_subject = len(x)
        if total_subject == 0:
            return 0
        for i in range (0, total_subject):
            if x[i] == None:
                return None
            for i in range (0,total_subject):
                if not get_grade(x[i]):
                    return None
                else:
                    total_marks =total_marks + get_grade(x[i])
            return total_marks / total_subject
    elif type (x) == str:
        total_marks = get_grade(x)
        return total_marks
#### End OF MARKER
### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###

#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa(['A+'])
    print calculate_sgpa_weighted(['A+'], [4])
