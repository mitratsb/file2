#Game(rock-paper-scissors) _ 1 player & computer move

print("welcome to the game")

player1 = input("player1, make your move: ")


from random import *
player2= randint(1,3)

if player2== 1:
    player2="rock"
elif player2==2:
    player2="paper"
elif player2==3:
    player2="scissors"

print(f"player2, make your move: {player2}")

p1= "player1 wins"
p2= "player2 wins"

# هر بازیکن باید 3 دست بازی را ببرد تا بازی تمام شود

p1_wins=0
p2_wins=0
p1_wins=int(p1_wins)
p2_wins=int(p2_wins)
for p1_wins in range (0,4) and p2_wins in range(0,4):
    
    print(f"player1_wins: {p1_wins} , player2_wins: {p2_wins}")
    if (player1=="rock" and player2=="scissors") or (player1=="scissors" and player2=="paper") or (player1=="paper" and player2=="rock"):
        print (p1)
        p1_wins += 1
    elif player1 == player2 :
        print("draw")
    elif (player1=="paper" and player2=="scissors") or (player1=="rock" and player2=="paper") or (player1=="scissor" and player2=="rock"):
        print(p2)
        p2_wins += 1
        
if (p1_wins==3 and (p2_wins==0 or p2_wins==1 or p2_wins==2)) or (p2_wins): 
    pass

