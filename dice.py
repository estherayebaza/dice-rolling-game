import random

def main():
    player1=0
    player2=0
    rounds=1
    while rounds!=10:
        print("Round"+str(rounds))
        player1=dice_roll()
        player2=dice_roll()
        print("player1 Roll:"+str(player1))
        print("player2 Roll:"+str(player2))
        rounds=rounds+1

        if player1==player2:
            print("draw")
        elif player1>player2:
            player1wins = player1wins+1
            print("Player1 wins")
        else:
            player2wins = player2wins+1
            print("Player2 wins")
            rounds=rounds+1
    if player1wins==player2wins:
             print("Draw")
    elif player1wins> player2wins:
        print("Player1 is the winner") 
    else :
        print("Player2 is the winner")

def dice_roll():
    diceRoll=random.randint(1,6)
    return diceRoll
# print(dice_roll())
# print(dice_roll())
# print(dice_roll())
# print(dice_roll())
main()