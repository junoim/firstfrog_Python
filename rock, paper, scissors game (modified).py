from getpass import getpass as input
print("E P I C   B A T T L E")
print()
print()
S = "scissors"
R = "Rock"
P = "Paper"
print("Round 1")
Player_1score = 0
Player_2score = 0
while True:
  Player_1move = input("Select you move (R,P,S): ")
  Player_2move = input("Select you move (R,P,S): ")
  if Player_1move == Player_2move :
    print("Alas! It's a Tie !!")
  elif Player_1move == "S" and Player_2move == "R":
    print("Oh no! Player 1 has lost the match! ; Victory to Player 2")
    Player_2score += 1
  elif Player_1move == "P" and Player_2move == "R":
    print("Oh no! Player 2 has lost the match! ; Victory to Player 1")
    Player_1score+= 1
  elif Player_1move == "R" and Player_2move == "S":
    print("Oh no! Player 2 has lost the match! ; Victory to Player 1")
    Player_1score+= 1
  elif Player_1move == "S" and Player_2move == "P":
    print("Oh no! Player 2 has lost the match! ; Victory to Player 1")
    Player_1score += 1
  elif Player_1move == "P" and Player_2move == "S":
    print("Oh no! Player 1 has lost the match! ; Victory to Player 2")
    Player_2score+= 1
  elif Player_1move == "R" and Player_2move == "P":
    print("Oh no! Player 1 has lost the match! ; Victory to Player 2")
    Player_2score+= 1
  else:
    print("Invalid Move Players")
  
  print("Player 1 has", Player_1score, "wins.")
  print("Player 2 has", Player_2score, "wins.")
  
  if Player_1score == 3 or Player_2score== 3:
    print("Thanks for playing!")
    exit()
  else:
    continue
