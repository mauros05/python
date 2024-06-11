user_input = int(input())

even_numbers = []

for number in range(2, user_input + 1):
    if number % 2 == 0:
        even_numbers.append(number)


sum_of_even_numbers = 0

for even_number in even_numbers:
    print(even_number)
    sum_of_even_numbers += even_number

print(f"The summ of the even numbers is: {sum_of_even_numbers}")