#S.McDonald 11/8/2016
#sum_of_numbers
#show the contents of the file and compute the total


#input
#myfile is a file object
myfile = open('numbers.txt', 'r') #open the file for reading

total = 0

for line in myfile:
    total = total + int(line)
    print(line, end="")

print("\nTotal is: ", total)
