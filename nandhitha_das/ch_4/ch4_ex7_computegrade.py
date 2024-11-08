# program to grade according to a score using function
# ex4.14 pg 54

marks_scored = float(input("Enter score: "))

# defining function compute_grade() that takes marks as input 
def compute_grade (marks_scored):
    if(marks_scored <= 1.0 and marks_scored > 0.0):
        if marks_scored >= 0.9:
            grade_scored = "A"
        elif(marks_scored >= 0.8):
            grade_scored = "B"
        elif(marks_scored >= 0.7):
            grade_scored = "C"
        elif(marks_scored >= 0.6):
            grade_scored = "D"
        else:
            grade_scored = "E"
        
    else:
            grade_scored = "Bad Value"

    return grade_scored  

# calling the function compute_grade()     
result = compute_grade(marks_scored)
print ("The grade scored is: ", result)
