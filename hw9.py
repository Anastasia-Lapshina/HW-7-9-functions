def great_digit(n):
    maxi = -1
    n = abs(n)
    while n >= 0:
        x = n % 10
        n = n // 10
        if (x % 2 == 0) and (x > maxi):
            maxi = x
        if n == 0:
            break
    if maxi >= 0:
        return maxi
    else:
        print("No even numbers found")
        quit()


n = input("Enter an integer ")
try:
    n = int(n)
except ValueError:
    print("Invalid data. Please enter an integer")
    quit()
print("The greatest even number in your integer is ", great_digit(n))
