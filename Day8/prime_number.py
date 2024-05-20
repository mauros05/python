def prime_number_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        print("It is a prime number.")
    else:
        print("It's not a prime number")


number = int(input("Type a number to know if it's prime or not: "))
prime_number_checker(number= number)