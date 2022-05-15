from typing import List

rock_item = ["rock", "r", "ro", "roc"]
scissor_item = ["scissor", "s", "sci"]
paper_item = ["paper", "p", "pap", "pape"]

# Rock, Paper, Or Scissors
def R_P_or_S(question, error):
    
    # Loops till you choose valid answer
    chosen = False
    while not chosen:

        a = ""

        # Hum_answer = human answer
        hum_answer = input(question).lower()
        
        if hum_answer in list(rock_item):
            a = "rock"
                    
        elif hum_answer in list(paper_item):
            a = "paper"            
        
        elif hum_answer in list(scissor_item):
            a = "scissors"

        else:           
            print(error)
            print()

        break


ahwqjdq = R_P_or_S("what will you choose, Rock(r), paper(p), or scissors(s)? ", "please choose one of the listed items")

print (a)



