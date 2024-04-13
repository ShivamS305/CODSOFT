import tkinter as tk
import random

class Rockpaperscissorgame:
    def __init__(self,master):
        self.master=master
        self.master.title("---Rock-Paper-Scissor Game---")
        screen_width= master.winfo_screenwidth()
        screen_height=master.winfo_screenheight()
       
        window_width = 330
        window_height = 370
      
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height- window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
       

        self.master.configure(bg="sky blue")

        self.title_font=("Times New Roman",14,"bold")
        self.user_score=0
        self.computer_score=0
        self.user_choice_var=tk.StringVar()
        self.user_choice_label = tk.Label(master, text="Choose Rock, Paper, Scissor:", font=self.title_font, bg="sky blue")

        self.user_choice_label.pack(pady=10)
        self.user_choice_menu=tk.OptionMenu(master,self.user_choice_var, "rock","Paper","Scissors")
        self.user_choice_menu.pack(pady=5)

        self.play_button=tk.Button(master,text="Play",command=self.play_game)
        self.play_button.pack(pady=10)

        self.user_choice_display_label = tk.Label(master, text="Your Choice: ", font=("Times New Roman",14), bg="sky blue")
        self.user_choice_display_label.pack(pady=5)

        self.computer_choice_display_label = tk.Label(master, text="Computer's Choice: ", font=("Times New Roman",15), bg="sky blue")
        self.computer_choice_display_label.pack(pady=5)

        self.result_label=tk.Label(master,text="",font=("helvetica",14,"bold"),bg="sky blue")
        self.result_label.pack(pady=10)

        self.score_label=tk.Label(master,text="", font=("helvetica",12,"bold"),bg="sky blue")
        self.score_label.pack(pady=5)

        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.config(state="disabled")


    def get_computer_choice(self):
        return random.choice(['rock','paper','scissors'])    
    
    def determine_winner(self,user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie !!"
        elif (user_choice == 'rock' and computer_choice =='scissors') or\
             (user_choice=='scissors' and computer_choice == 'paper') or\
             (user_choice=='paper' and computer_choice =='rock'):
            self.user_score+=1
            return "you win !!"
        else:
            self.computer_score+=1
            return "computer wins !!"

    def play_game(self):
        user_choice=self.user_choice_var.get()
        computer_choice=self.get_computer_choice()

        self.user_choice_display_label.config(text=f"Your Choice: {user_choice.capitalize()}")
        self.computer_choice_display_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"result : {result}")
        self.result_label.config(bg="sky blue")

        self.score_label.config(text=f"Scores - user: {self.user_score}  Computer : {self.computer_score}")
        self.score_label.config(bg="sky blue")

        self.play_button.config(state="disabled")
        self.play_again_button.config(state="normal")

    def reset_game(self):
        self.result_label.config(text="")
        self.user_choice_display_label.config(text="Your Choice: ")
        self.computer_choice_display_label.config(text="Computer's Choice: ")
        self.play_button.config(state="normal")
        self.play_again_button.config(state="disabled")

root=tk.Tk()
app = Rockpaperscissorgame(root)
root.mainloop()