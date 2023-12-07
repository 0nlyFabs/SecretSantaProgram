#We create a list that is going to be used to determine the names of players for the game

def gather_player_names():
    
    secretsantanames = []

    print('Enter the name\'s of the paticipents below, when you\'re done, type "quit" to move on')

    while True:
        name = input('Participent\'s name: ').strip().capitalize()

        if name.lower() == 'quit':
            break

        secretsantanames.append(name)

    print('Final list of names', secretsantanames)

    while True:
        finaldecision = input('Are you happy with the above list? (yes/no): ')

        if finaldecision == 'yes':
            break

        if finaldecision == 'no':
            while True:
                name = input('Participent\'s name: ').capitalize()

                if name.lower() == 'quit':
                    break

                secretsantanames.append(name)

        print('Final list of names', secretsantanames)

    return secretsantanames
