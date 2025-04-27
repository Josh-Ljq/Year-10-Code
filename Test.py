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

#7
def grade_check (score):
	if(score >= 90):
		return("A")
	elif(score >= 80):
		return("B")
	elif(score >= 70):
		return("C")
	elif(score >= 60):
		return("D")
	else:
		return("Fail")

#8
def username_password():
	username = "John Doe"
	password = "password124"
	if(input() == username and input() == password):
		return("pass")
	else:
		return("fail")

#9
def count():
	a = 1
	while(a <= 10):
		print(a)
		a += 1

#10
def times_table(num):
	a = 1
	while (a <= 12):
		print(a * num)
		a += 1

#11
def sum_tot(num):
	tot = 0
	a = 1
	while(a <= num):
		tot += a
	return(tot)

#12
def countdown():
	for i in range(-10, -1):
		print(i * -1)

#13
def guess():
	guess = int(input())
	num = random.randint(1, 10)
	while(guess != num):
		guess = int(input())
	
	




















