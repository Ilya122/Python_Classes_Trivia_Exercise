def GetIntegerFromUser(message, min, max):
    tryingToGetNum = True
    number = 0
    while tryingToGetNum:
        userNum = input(message)
        try:
            number = int(userNum)
        except ValueError:
            print('Please enter a valid number!')
            continue
        if number < min or number > max:
            print(f'Please enter a valid number between {min} and {max}')
        else:
            tryingToGetNum = False
    return number
