print("Enterr pcm mark out of 100: ")

physics_marks = int(input("enter physics marks: "))
chemistry_marks = int(input("enter chemistry marks: "))
math_marks = int(input("enter math marks: "))

#eligibility check

if (physics_marks>=65 and
    chemistry_marks>=55 and
    math_marks>=50 and
   (physics_marks + chemistry_marks + math_marks)>=180) or\
   (math_marks + physics_marks)>=140:
    print("you re eligible! ")
else:
    print("you re not eligible! ")    