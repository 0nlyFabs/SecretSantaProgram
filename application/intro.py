#Here it is a simple intro to the program, made with an ASCII art generator for some pizzaz

from tkinter import *

def display_intro():

    startbutton = Tk()
    startbutton.geometry('500x500')
    button = Button(startbutton,text = 'Start')
    button2 = Button(startbutton, text = 'Close')
    button.pack()
    button2.pack()
    startbutton.mainloop()


    print('''
             _______. _______   ______ .______      _______ .___________.        _______.     ___      .__   __. .___________.    ___         .______   .______       ______     _______ .______          ___      .___  ___.    ____    ____  __       ___   
            /       ||   ____| /      ||   _  \    |   ____||           |       /       |    /   \     |  \ |  | |           |   /   \        |   _  \  |   _  \     /  __  \   /  _____||   _  \        /   \     |   \/   |    \   \  /   / /_ |     / _ \  
           |   (----`|  |__   |  ,----'|  |_)  |   |  |__   `---|  |----`      |   (----`   /  ^  \    |   \|  | `---|  |----`  /  ^  \       |  |_)  | |  |_)  |   |  |  |  | |  |  __  |  |_)  |      /  ^  \    |  \  /  |     \   \/   /   | |    | | | | 
            \   \    |   __|  |  |     |      /    |   __|      |  |            \   \      /  /_\  \   |  . `  |     |  |      /  /_\  \      |   ___/  |      /    |  |  |  | |  | |_ | |      /      /  /_\  \   |  |\/|  |      \      /    | |    | | | | 
        .----)   |   |  |____ |  `----.|  |\  \----|  |____     |  |        .----)   |    /  _____  \  |  |\   |     |  |     /  _____  \     |  |      |  |\  \----|  `--'  | |  |__| | |  |\  \----./  _____  \  |  |  |  |       \    /     | |  __| |_| | 
        |_______/    |_______| \______|| _| `._____|_______|    |__|        |_______/    /__/     \__\ |__| \__|     |__|    /__/     \__\    | _|      | _| `._____|\______/   \______| | _| `._____/__/     \__\ |__|  |__|        \__/      |_| (__)\___/  
                                                                                                                                                                                                                                                            
        ''')

    print('''
    Welcome to Secret Santa Program V1.0! created by 0nlyFabs.
          
    Clearly you are here for a reason and want to get a round of Secret Santa going for your friends/family/co-workers/evil henchmen.
            
    Well you have come to the right place!
        ''')