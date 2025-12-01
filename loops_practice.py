Students = ["Aman","Rohit","Isha","Uday","Kiran"]
vowels = "AEIOUaeiou"

for x in Students:
    if x[0] in vowels:
        print(x)
print('------------------------------------------------------------')


#Using the input method , So that the user can himself enter the names:

Students = input("Enter the name of the students with spaces after each name. : ").split()
vowels = "AEIOUaeiou"

for x in Students:
    if x[0] in vowels:
        print(x)
