def prime_checker(number):
    prime = False
    notPrime = False
    if number > 1:
        if number == 2:
            print("It's a prime number.")
        for i in range(2, number):
            if number % i == 0:
                notPrime = True
            else:
                prime = True
        if notPrime == True:
            print("It's not a prime number.")
        elif prime == True:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))

prime_checker(number=n)