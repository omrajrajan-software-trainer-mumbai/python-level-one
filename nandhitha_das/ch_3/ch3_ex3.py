# program to grade according to a score
# ex3.11 pg 53

marks_scored = float(input("Enter score: "))
if(marks_scored <= 1.0 and marks_scored > 0.0):
    if marks_scored >= 0.9:
        print("A")
    elif(marks_scored >= 0.8):
        print("B")
    elif(marks_scored >= 0.7):
        print("C")
    elif(marks_scored >= 0.6):
        print("D")
    else:
        print("F")
else:
    print("Bad score")
