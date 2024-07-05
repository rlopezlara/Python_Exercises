import random 
#print("Welcome to Rock, Paper, scissors Game")

options = ["rock","paper", "scissors"]
game = True
countPlayer= 0
countComputer=0
while game :
    count = 1     
    player =None  
    print("You have 3 attend to win!")
    
    while count <= 3:
        computer = random.choice(options)        
        player = input("Enter Rock, Paper or scissors: ").lower()
        
        if player not in options:
            print("Spelling mistake, try again!")
            continue
        
        print("Game Number ", count)            
        print(f"Player : {player}")
        print(f"computer : {computer}")        
            
        if player == computer:
            print("it is a tie!")           
        elif player == "rock" and computer == "scissors":
            print("You win!")
            countPlayer +=1
        elif player == "paper" and computer == "rock":
            print("you win!")
            countPlayer +=1
        elif player == "scissors" and computer == "paper":
            print("you win!")
            countPlayer +=1
        elif computer == "rock" and player == "scissors":
            print("You lose!")
            countComputer +=1 
        elif computer == "paper" and player == "rock":
            print("you lose")
            countComputer +=1 
        elif computer == "scissors" and player == "paper":
            print("you lose!")
            countComputer +=1
                    
        print("Games won Player: "+str(countPlayer))
        print("Games won Computer: "+str(countComputer))
        count +=1
        print("**********************") 
        
    question=input("Would you continue playing: (y/n)").lower()
    if question=="n":
        game=False
        print("Thanks for playing!")
        