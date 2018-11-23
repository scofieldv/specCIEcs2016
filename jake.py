#You have to input the student name and scores of each student. The program will give you the average, total, each students' score and highest mark.
#hab means sum

student = []
test1 = []
test2 = []
test3 = []
sum = []
average = []
hab = 0
hab1 = 0
hab2 = 0
hab3 = 0
biggest = 0
highest = 0

while True:
    try:
        numOfStudent = int(input("\n\nType the number of student\n"))
        break
    except ValueError:
        print('\nThe number of student must be in number\n')
        

student.append(str(input("\nType the name of student\n")))
for i in range(numOfStudent):
    while True:
        try:
            score1 = float(input("\nType the score of first test of the student\n"))
            break
        except ValueError:
            print("\nThe score msut be in number between 0 and 20\n")
    while score1 > 20 or score1 < 0:
        print("\nWrong score\nThe first test is out of 20 marks\n")
        while True:
            try:
                score1 = float(input("\nType the score of first test of the student\n"))
                break
            except ValueError:
                print("\nThe score must be in number between 0 and 20\n")
    test1.append(score1)
    while True:
        try:
            score2 = float(input("\nType the score of second test of the student\n"))
            break
        except ValueError:
            print("\nThe score must be in number between 0 and 25\n")
    while score2 > 25 or score2 < 0:
        print("\nWrong score\nThe second test is out of 25 marks\n")
        while c = 1:
            try:
                score2 = float(input("\nType the score of second test of the student\n"))
                c = 0
            except ValueError:
                print('\nThe score must be in number between 0 and 25\n')
    test2.append(score2)
    while True:
        try:
            score3 = float(input("\nType the score of third test of the student\n"))
            break
        except ValueError:
            print('\nThe score must be in number between 0 and 35\n')
    while score3 > 35 or score3 < 0:
        print("\nWrong score\nThe third test is out of 35 marks\n")
        while True:
            try:
                score3 = float(input("\nType the score of third test of the student\n"))
                break
            except ValueError:
                print('\nThe score must be in number between 0 and 35\n')
    test3.append(score3)
    hab1 = hab1 + score1
    hab2 = hab2 + score2
    hab3 = hab3 + score3
    hab = hab + score1 + score2 + score3
    sum.append(score1+score2+score3)
    if biggest < score1+score2+score3:
        biggest = score1+score2+score3
        highest = i
    if i < numOfStudent-1:
        student.append(str(input("\nType the name of next student\n")))

print('\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------')    
  

print('\n\n','Total average is ', hab/numOfStudent, 'out of 80')
print('\n','Average of the first test is ', hab1/numOfStudent, 'out of 20')
print('\n','Average of the second test is ', hab2/numOfStudent, 'out of 25')
print('\n','Average of the second test is ', hab3/numOfStudent, 'out of 35')

print('\n\n---------------------------------------------------------------------------------------------------------------------------------------------------------') 

for i in range(0, numOfStudent):
    print('\n\nStudent : ', student[i], '\nFirst test : ', test1[i], '\nSecond test : ', test2[i], '\nThird test : ', test3[i], '\n\n')

print('\n---------------------------------------------------------------------------------------------------------------------------------------------------------') 

print('\n\n', student[highest], 'has the highest score\n', 'The score is ', biggest, 'out of 80')