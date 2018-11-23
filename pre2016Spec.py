def validlist(list, testnumber, _max):
    count = 0
    while True and count < 1:
    
        try:
            score = int(input('Type the score for {}'.format(testnumber)))
            
            if score <0 or score >_max:
                print('Type again')
            
            else:
                list.append(score)
                count+=1
                
        except:
        
            print('Invalid Input')
            
    return list

def highposition(list):
    result = 0
    index = 0
    for i in range (len(list)):
        
        if list[i] > result:
            result = list[i]
            index = i
            
    return result, index        
score1 = []
score2 = []
score3 = []
students = []
for i in range (3):
    name = input('Student name: ')
    students.append(name)
    validlist(score1, 'test 1', 20)
    validlist(score2, 'test 2', 25)
    validlist(score3, 'test 3',35)


print(score1, sum(score1))
print(score2, sum(score2))
print(score3, sum(score3))
highest, position = highposition(score1)

print(highest, position)
print( 'The student with highest mark for {} is {} with a mark of {}'.format('test 1', students[position], score1[position]))