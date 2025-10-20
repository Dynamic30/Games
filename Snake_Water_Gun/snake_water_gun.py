import random

#  logic 
#  snake(1) beats water(3)
#  water(3) beat gun(2)
#  gun(2) beat snake(1)
print("""
Game Logic:
snake(1) beats water(3)
water(3) beat gun(2)
gun(2) beat snake(1)
""")

def snake_water_gun():
    
    # user conditions
    while True:
        try:
            user = int(input("Enter a value(s:1,g:2,w:3): "))
            if user not in [1,2,3]:
                print("Enter the value from the following table\nSnake(s)=1\nGun(g)=2\nWater(w)=3")
                continue
            break
        except ValueError:
            print ("ENTER AN INTEGRAL VALUE")
            continue

    computer = computer = random.randint(1,3)
    if user == 1 and computer ==3:
        print("You Win")
    elif user == 1 and computer ==2:
        print("You Lose")
    elif user == 2 and computer ==1: 
        print("You Win")
    elif user == 2 and computer ==3: 
        print("You Lose")
    elif user == 3 and computer ==1: 
        print("You Lose")
    elif user == 3 and computer ==2: 
        print("You Win")
    elif user ==  computer:
        print("Draw")
    else:
        print("Enter the value from the follwoing table\nSnake(s)=1\nGun(g)=2\nWater(w)=3")
    print(f"Computer = {computer}, You = {user}")
    
    
    def play_again():
        play = input("Want to play again? (y/n)")
        if play == "y" or play == "Y":
            snake_water_gun()
        elif play == "n" or play =="N":
            print("Game over")
        else:
            print("Invalid Value, enter from y/n")
            play_again()
    play_again()


snake_water_gun()