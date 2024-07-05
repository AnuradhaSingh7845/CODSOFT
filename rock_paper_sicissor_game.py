import random
options = ("Rock","Paper","Scissor")
print("\t---Rock,Paper,Scissor Game---\n\t  --Let's Start the Game--")
count=int(input("Select no of rounds 1/3/5:"))
bot_count=0
user_count=0
user_choice=None
running=True
while running:
    for i in range(count):
            print("---------------------------------------------")
            print("Round ",i+1) #Print no of Round
            while user_choice not in options:    #takes input from user
                user_choice=input("Your choice (Rock,Paper,Scissor) : ").capitalize()
            bot_choice=random.choice(options)   #take bot's choice
            print("Bot's Choice: ",bot_choice)  #print bot's choice
            #checking game conditions
            if(user_choice == bot_choice):
                print("Match Draw")
            elif(user_choice == "Rock" and bot_choice == "Scissor") or (user_choice == "Paper" and bot_choice == "Rock") or (user_choice == "Scissor" and bot_choice == "Paper"):
                print("You Won!")
                user_count +=1  #incrementing user's score
            else:
                print("Bot Won!")
                bot_count+=1    #incrementing bot's score
            user_choice=None
    print("---------------------------------------------")
    print("Final Score\nYour Score:",user_count,"\nBot Score: ",bot_count)  #final scores after rounds
    if(bot_count==user_count):  
        print("Game Draw!!")
    elif(bot_count>user_count):
        print("Bot Won!")
    else:
        print("You Won!")
    if not input("Play Again?(y/n): ").lower() == 'y':  #Asking player to play again?
        running = False
print("\n------------Thank You for Playing!------------")


