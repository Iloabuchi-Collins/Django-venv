# author: iloabuchi_collins
# I4G-ZURI scolarship task
from random import choice

print("Let's play Rock Paper Scissors...")
print(" Pick 'R' or 'P' or 'S' \n'R' represents 'rock' \n'P' represents 'paper' \n'S' represents 'scissors'  ")
accepted_moves = ["R", "P", "S"]
game_over = False
while not game_over:
	computer = choice(['Rock','Paper','Scissors'])
	player = input("What is your move? ").upper()  #incase they enter lower case
	if player in accepted_moves:
		if player == 'R':
			player = 'Rock'
		elif player == 'P':
			player = 'Paper'
		elif player == 'S':
			player = 'Scissors'
		print(f"Player({player}) : CPU({computer})")
		if player == computer:
			print("It's a tie. We will play again ")
		if player == 'Rock' and computer == 'Paper':
			print("Computer wins")
			game_over = True
		elif player == 'Rock' and computer == 'Scissors':
			print("You win! :)")
			game_over = True
		elif player == 'Paper' and computer == 'Rock':
			print("You win! :)")
			game_over = True
		elif player == 'Paper' and computer == 'Scissors':
			print("Computer wins")
			game_over = True
		elif player == 'Scissors' and computer == 'Rock':
			print("Computer wins")
			game_over = True
		elif player == 'Scissors' and computer == 'Paper':
			print("You win! :)")
			game_over = True
	else:	
		print("Invalid movie! please pick 'R', 'P' or 'S'")
		

