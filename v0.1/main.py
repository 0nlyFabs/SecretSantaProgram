#Welcome to the Secret Santa Program created by 0nlyFabs in October 2023
#Please take a look at my GitHub repositories for more https://github.com/0nlyFabs?tab=repositories

#I will also explain my code as I go along with comments grjgadsi;ug

import intro
import playernames
import randomassignment

#Here we are displaying the intro from intro.py file
intro.display_intro()

#Asking the user if they have ever played Secret Santa before, and generating a response based on their answer
#This could also go in a new file named previousplay.py but I kept it here as what is life without a little whimsy (Big Bang Theory, S3 E23 - The Lunar Excitation - 16:35)

while True:      
    previousplay = input('Let\'s start off with the basics, do you know what Secret Santa is? (yes/no): ').strip().lower()
    
    if previousplay == 'yes':
        print('''
              
Perfect, then you know what you\'re doing!
              
              ''')
        break
        
    if previousplay == 'no':
        print('''
              
That\'s okay, let me explain.

Secret Santa is a gift-giving tradition where each person in a group anonymously must buy a gift for another person. 
The recipient doesn't know who their gift is from until they open it during a designated gift exchange event. 
It's a fun way to celebrate holidays or special occasions with a surprise element.
              
              ''')
        break
        
    else:  
        print('Sorry, I didn\'t get that, please try try again and answer with either yes or no.')

print('Let\'s get started!')

#Assigning the player to another player for the gifts to be given and print final
randomassignment.random_assignment(playernames.gather_player_names())
