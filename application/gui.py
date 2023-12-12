import tkinter as tk
import randomassignment
from tkinter import messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secret Santa")
        welcome_message = "Welcome to Secret Santa Program V1.0! created by 0nlyFabs. Clearly you are here for a reason and want to get a round of Secret Santa going for your friends/family/co-workers/evil henchmen. Well you have come to the right place!"        

        #Create opening message
        self.display_messagebox(welcome_message)
        
        # Create frames for different pages
        self.welcome = tk.Frame(root)
        self.playernames = tk.Frame(root)
        self.assign = tk.Frame(root)

        # Create list of names and global widgets
        self.names = []
        self.name_entry = tk.Entry(self.playernames)
        self.names_listbox = tk.Listbox(self.playernames, selectmode=tk.SINGLE)
        # Call a function to set up the initial content of each page
        self.setup_welcome()
        self.setup_playernames()
        self.setup_assign()

        # Show the initial page
        self.show_page(self.welcome)
    
    def display_messagebox(self, message):
        messagebox.showinfo("Information", message)
        
    def setup_welcome(self):
        label_know = tk.Label(self.welcome, text="Lets start of with the basics, do you know what Secret Santa is?", font=("Helvetica", 16))
        label_know.pack(pady=10)
        button_welcome_yes = tk.Button(self.welcome, text="Yes", command=self.show_playernames)
        button_welcome_no = tk.Button(self.welcome, text="No", command=self.new_person)
        button_welcome_yes.pack()
        button_welcome_no.pack()

    def setup_playernames(self):
        # Label notifying players
        players_label = tk.Label(self.playernames, text="Please enter the players:", font=("Helvetica", 16))
        players_label.pack(pady=10)
        # Entrybox for names
        self.name_entry.pack(pady=5)
        # Add Plater Button 
        add_player_button = tk.Button(self.playernames, text="Add Player", command=self.add_name)
        add_player_button.pack()
        # Listbox displaying names
        self.names_listbox.pack(pady=10)
        # Done
        complete_button = tk.Button(self.playernames, text='Happy with Players', command=self.show_assign)
        complete_button.pack()

    
    def add_name(self):
        name = self.name_entry.get()
        self.names.append(name)
        self.update_names_listbox()
        self.name_entry.delete(0, tk.END)
    
    def update_names_listbox(self):
        # Clear Listbox
        self.names_listbox.delete(0, tk.END)
        # Insert Names into box
        for name in self.names:
            self.names_listbox.insert(tk.END, name)

    
    def setup_assign(self):
        assigned_label = tk.Label(self.assign, text="The random assignments are", font=("Helvetica", 16))
        assigned_label.pack(pady=5)
        self.assigned_listbox = tk.Listbox(self.assign, selectmode=tk.SINGLE)
        self.assigned_listbox.pack(fill=tk.BOTH, expand=True)

    def show_page(self, page):
        # Hide all frames and show the specified frame
        self.welcome.pack_forget()
        self.playernames.pack_forget()
        self.assign.pack_forget()
        page.pack()

    def show_welcome(self):
        self.show_page(self.welcome)

    def show_playernames(self):
        self.show_page(self.playernames)
    
    def show_assign(self):
        self.show_page(self.assign)
        rand = randomassignment.random_assignment(self.names)
        # Insert Names into box
        for assignment in rand:
            self.assigned_listbox.insert(tk.END, assignment)

    def new_person(self):
        new_message = '''
              
That\'s okay, let me explain.

Secret Santa is a gift-giving tradition where each person in a group anonymously must buy a gift for another person. 
The recipient doesn't know who their gift is from until they open it during a designated gift exchange event. 
It's a fun way to celebrate holidays or special occasions with a surprise element.
              '''
        self.display_messagebox(new_message)
        #wait 100 ms to fix bug on dynamic change
        self.root.after(100, self.show_playernames)


def start_app():
    # Create the main window
    root = tk.Tk()
    root.geometry("500x500")
    # Instantiate the application
    app = MyApp(root)

    # Start the Tkinter event loop
    root.mainloop()