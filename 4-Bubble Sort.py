def BubbleSort(myList):
    for j in range(0, len(myList)):
        for i in range(0,len(myList)-1):
            if myList[i]>myList[i+1]:
                temp = myList[i]
                myList[i]=myList[i+1]
                myList[i+1]=temp

myList = []
n = int(input("Enter number of elements in the List:\n"))
for j in range(0,n):
    element = int(input("Input element:\n"))
    myList.append(element)
print("The unsorted array is "+str(myList))

BubbleSort(myList)

print("The sorted array is "+str(myList))