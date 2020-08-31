# taking input from user
number = int(input("Enter any number: "))
r1 = int(input("enter the range number"))
# prime number is always greater than 1
if number > 1:

    for i in range(r1, number + 1):

        for j in range(2, i):

            if (i % j) == 0:
                # print(j, "is not a prime number")
                continue
            else:
                print(i, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number end")
    print("entered new line")
##  comments added adding to check git