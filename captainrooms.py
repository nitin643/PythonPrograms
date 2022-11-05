# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
li = input().split()

#sorting elements in ascending order
li.sort()

i = 0
#running while loop until index reaches length of list
while i <= len(li) - 1:
    #if i is equal to second last index, the last element is the answer
    if i == len(li) -1:
        print(li[i])
    #else check if the value of 1st and second value is equal, if so skip n -1 iterations    
    else:    
        if li[i] == li[i+1]:
            i+= n - 1
        else:      
            print(li[i])
    i+= 1   
