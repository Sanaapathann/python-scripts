import random

def rockPaperScissors():

    print("Rock Paper Scissors")
    wins = 0
    losses = 0
    ties = 0

    while True:
        print(f'wins -> {wins}, losses -> {losses}, ties -> {ties}')
        while True:
            choice = input("Rock, Paper, Scissors, or Quit: ").lower()
            print(choice)
            print("\nVersus....")
            if choice == 'quit':
                break
            else:
                botChoice = random.randint(1,3)
                if botChoice == 1:
                    versus = "Rock"
                    print(versus)
                    if choice == 'rock':
                        print("tie!")
                        ties += 1
                    elif choice == 'paper':
                        print("you won!")
                        wins += 1
                    elif choice == 'scissors':
                        print("you lose!")
                        losses += 1
                elif botChoice == 2:
                    versus = "Paper"
                    print('Paper')
                    if choice == 'paper':
                        print("tie!")
                        ties += 1
                    elif choice == 'scissors':
                        print("you won!")
                        wins += 1
                    elif choice == 'rock':
                        print("you lose!")
                        losses += 1
                elif botChoice == 3:
                    versus = "Scissors"
                    print('Scissors')
                    if choice == 'scissors':
                        print("tie!")
                        ties += 1
                    elif choice == 'rock':
                        print("you won!")
                        wins += 1
                    elif choice == 'paper':
                        print("you lose!")
                        losses += 1
                else:
                    print("bot choice error")

            print(f'wins -> {wins}, losses -> {losses}, ties -> {ties}')

if __name__ == '__main__':
    rockPaperScissors()


