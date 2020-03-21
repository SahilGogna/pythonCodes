def customFunc(testList):
    joinedList = ""
    count = 0
    while count < len(testList)-2:
       joinedList+= testList[count] + ", "
       count+=1
    joinedList = joinedList + testList[-2] + " and "
    joinedList +=  testList[-1]
    return joinedList
       

spam = ['1','2','3','4','5']
print(customFunc(spam))

