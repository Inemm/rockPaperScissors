from random import choice 
def rockpaperScissors():
    choices = ["R","P","S"]
    player = input("choose an option: R, S, P\n").upper()
    money=True 
    while money : 
        if player in choices : 
            computer = choice(choices) 
            RPSdict ={"R":"Rock", "P":"Paper", "S":"Scissors"} 
            print ("You chose: ", player, "computer chose: ", computer) 
            print ("User(" + RPSdict[player]+ ") : CPU("+ RPSdict[computer]+")")  
            if player == computer: 
                print("It's a tie. we go again")
                player = input("choose an option: R, S, P\n").upper()
            else : 
                if player == "R" and computer== "S":
                    print("player WINS! ") 
                    money= False 
                if player == "S" and computer== "R": 
                    print("computer WINS! ") 
                    money= False   
                if player == "P" and computer== "R":
                    print ("player WINS! ")  
                    money= False 
                if player == "R" and computer== "P":
                    print ("computer WINS! ") 
                    money= False 
                if player == "S" and computer== "P":  
                    print ("player WINS! ") 
                    money= False 
                if player == "P" and computer== "S":
                    print ("computer WINS! ") 
                    money= False 
        else : 
          print("invalid option")
          player= input("choose an option: R, S, P\n").upper() 
          continue 
      

rockpaperScissors()