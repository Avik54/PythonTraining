actualNumber = 15

choice = "Y"

while choice != 'n':
    guessedNumber = int(input(f"Enter you predited number : \n"))
    if guessedNumber > actualNumber:
        print(f"You Have Entered Higher Value !!!")
    elif guessedNumber < actualNumber:
        print(f"You Have Entered Lower Value !!!")
    elif guessedNumber == actualNumber:
        print(f"You Have Entered Correct Value :)")
    choice = input(f"Do you want to continue ? (Y/N)")

                                                                              