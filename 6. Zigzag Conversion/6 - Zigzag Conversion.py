'''
6. Zigzag Conversion
- The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

- And then read line by line: "PAHNAPLSIIGYIR"

- Write the code that will take a string and make this conversion given a number of rows

What we need to do:
    - We are given with a string and we need to return a string in the specified(zigzag) format
    - We can take a simple approach, that is to populate the list dynamically as we iterate through 's'
    
Solution logic:
    - Create a list of strings of size = numRows
    - Now iterate through the input string 's' and fill the list with single character of 's'
    - if we reach last index of list then start filling the list in reverse order
    - if we reach the first index then reverse the order again
    - Likewise switch the order whenever we hit the first and last index of the list
    - Once we reached the last character of 's', join the strings in the list and return it
'''

def convert(s,numRows):
    #creating list of strings of size = numRows
    sol = ['' for i in range(numRows)]

    #initializing iterator to iterate through characters of s
    i=0
    #initializing iterator to iterate through the sol list
    index = 0
    #initializing flag to swithing the order of iteration
    flag = True

    #Entering the loop
    while True:
        #flag = True: iterate the the list
        if flag:
            #append the character of s to the corresponding index of sol
            sol[index] = str(sol[index][:])+s[i]
            index+=1
        #flag = False: iterate the list in reverse order 
        else:
            index+=1
            #append the character of s to the corresponding index of sol
            sol[-index] = str(sol[-index][:])+s[i]
            
        #increament the iterator
        i+=1
        
        #if we index iterator reaches last index, change the flag to reverse the order and make the index iterator 1 
        if index==numRows:
            flag=not flag
            index=1
        
        #if s iterator reaches last character then break
        if i == len(s):
            break

    #convert the list of strings into a single string
    return ''.join(sol)
    