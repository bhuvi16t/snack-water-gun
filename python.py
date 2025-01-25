<<<<<<< HEAD
print('hello world')
=======
# snake water gun game 

gamecounter=0
playercounter=0
computercounter=0

while True: 

     import random  # random module 
     
     print("welcome to SNAKE WATER GUN ")

     choice = ["SNAKE","WATER","GUN"]


     print(choice)

     # player choice 

     playerchoice=choice[int(input("""
                                   0: FOR SNAKE
                                   1: FOR WATER
                                   2: FOR GUN
                                   3: FOR EXIT
                                   
                                   
                                   
                                   Choose Any Option"""))]


     computerchoice=random.choice(choice)  # computer choice 
     


     if playerchoice==computerchoice:
          playercounter+=1
          computercounter+=1
          print("Game is Draw")


     elif playerchoice=="SNAKE" or computerchoice=="GUN":
          computercounter+=1
          
          print("You are lose the Game ")


     elif playerchoice=="WATER" or computerchoice=="SNAKE":
          computercounter+=1
          
          print("You are lose the game")

     elif playerchoice=="WATER" or computerchoice=="GUN":
          playercounter+=1

          
          
          print("Congratulation you are winner ")

     elif playerchoice=="GUN" or computerchoice=="SNAKE":
         playercounter+=1
        
     
         print("Congratulation you are winner ")

     elif playerchoice=="GUN" or computerchoice=="WATER":
          computercounter+=1

          print("You are lose the game")
     else:
         print("Please choose a valid option")


     again = int(input(""""YOu Need To play Again
                       1.yes
                       2.no
                       """))
     if again==1 :
          gamecounter+=1
          if gamecounter<=4:
             
          
             continue
          else:
               break


     else:
          exit()         
if playercounter<computercounter:

     print(": YOU LOSE")
else:
     print(": YOU WIN ")
>>>>>>> d0959639895942a6473dcd277cce9aea1891eedb
