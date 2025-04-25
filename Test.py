import random

#14
def rps(ans):
	game_list = ["Rock", "Paper", "Scissors"]
	
	ans = ans.lower()
	
	replay = random.choice(game_list).lower()
	
	if( replay == ans ):
		return("Draw")
	elif(replay == "rock" and ans == "paper"):
		return("Win")
	elif(replay == "paper" and ans == "scissors"):
		return("Win")
	elif(replay == "scissors" and ans == "rock"):
		return("Win")
	elif(ans == "rock" and replay == "paper"):
		return("Lose")
	elif(ans == "paper" and replay == "scissors"):
		return("Lose")
	elif(ans == "scissors" and replay == "rock"):
		return("Lose")
	else:
		return("Undetermined")

#16
def password_gen():
    pos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+']
    string = ""
    for i in range(8):
        string += random.choice(pos)
    return(string)

#6
def is_even(int):
    if (int % 2 == 1):
        return(False)
    else:
        return(True)
