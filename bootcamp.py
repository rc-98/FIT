#assign list to a variable
intList = [3, 10, 4, 9, 8, 7]

listTotal = 0 
string = ""

#find sum of list
for integer in intList: 
    listTotal += integer 

# loop through list and find the product 
for int1 in intList:   
    for int2 in intList:
        product = int1 * int2 
        if(int1 != int2 and product > listTotal):
            # print if the 2 integers are different and greater than the list total
            print (int1, int2)








 