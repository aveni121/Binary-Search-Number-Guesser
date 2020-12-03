# 11/13/2020
# Number Guesser by Binary Search
# This program will guess the number between 1-1000 the user is thinking of
# It does this by first, creating a list of numbers from 1-1000 and then
# creating another list that only contains the numbers that are multiples
# of the numbers inputted by the user and that also have the corresponding
# last digit. It then goes through the list via binary search.
# If you enter the highest multiple the program is able to find the number
# faster

def match_check(mid, new_database):
    user_reply = input(f"Is {new_database[mid]} your number? (Y/N): ").upper()
    while(len(user_reply) > 1):
        print("INVALID INPUT. Please enter (Y/N):")
        user_reply = input(f"Is {new_database[mid]} your number? (Y/N): ").upper()
    if user_reply == 'Y':
        print ("The number has been successfully guessed!")
        return True
    else:
        return False

def run(multiple, last_digit, database):
    #List that uses list comprehension to create a new list that only contains
    #the possible numbers according to the multiple and the last digit the 
    #user entered
    new_database = [i for i in database if i % multiple == 0 and i % 10 == last_digit]
    #Sets initial binary search point
    left = 0
    right = len(new_database)
    mid = int((left + right)/2)
    guessed = match_check(mid, new_database)
    while not guessed:
        search_adjuster = int(input("Please enter '0' if your number is lower or '1' if your number is higher: "))
        if search_adjuster == 0:
            #adjust binary search to the lower end
            right = mid - 1
            mid = int((left + right)/2)
        elif search_adjuster == 1:
            #adjust binary search to the higher end
            left = mid + 1
            mid = int((left + right)/2)
        else:
            #prompts for proper input
            while search_adjuster > 1 or search_adjuster < 0:
                print("INVALID INPUT")
                search_adjuster = int(input("Please enter '0' if your number is lower or '1' if your number is higher: "))
        guessed = match_check(mid, new_database)

def main():
    print("Think of a number between 1-1000")
    multiple = int(input("Please enter a multiple of your number: "))
    while multiple > 1000 or multiple < -1000:
        multiple = int(input("INVALID INPUT. Please enter a multiple from -1000 to 1000: "))
    last_digit = int(input("Please enter the last digit of your number: "))
    while last_digit > 9:
        last_digit = int(input("INVALID INPUT. Please enter a single digit: "))
    database = list(range(1,1001))
    run(multiple, last_digit, database)

if __name__ == "__main__":
    main()