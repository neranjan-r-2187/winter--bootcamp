# Given marks of a student, print on the screen:

# Grade A if marks >= 90
# Grade B if marks >= 70
# Grade C if marks >= 50
# Grade D if marks >= 35
# Fail, otherwise.

n=int(input())

if n>=90:
    print("Grade A")
elif n>=70:
    print("Grade B")
elif n>=50:
    print("Grade C")
elif n>=35:
    print("Grade D")
else:
    print("Fail")