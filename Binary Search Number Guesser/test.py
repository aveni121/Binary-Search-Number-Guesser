database = list(range(1,11))
some_number = len(database)
print(some_number)
prime_database = list(range(1,11))
max_number = database[-1]

for num in prime_database:
    for i in range(2, num):
        if(num % i) == 0: 
            print(num, "is not prime")
            if num in prime_database:
                prime_database.remove(num)
        
print(database)
print(prime_database)

multiple = int(input("Please enter a multiple of your number: "))
last_digit = int(input("Please enter the last digit of your number: "))
new_database = [i for i in database if i % 2 == 0 and i % multiple == 0 and i % 10 == last_digit]

print(new_database)