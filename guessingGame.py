import random
def main():
    number=random.randint(0, 9)
    guess=int(input(" GUESS A NUMBER BETWEEN 1-9 "))
    chances =5
    while chances < 5:
        print(chances)
    if guess == number:
        print("CONGRATULATION YOU WON!!!")
        
    elif guess>=number:
        print("you were close.The no. was ",number)
        chances=chances-1

    else:
        print("YOU LOSE!! The no. is ",number)
main()