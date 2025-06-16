import random


categories = {
    "fruits": [
        "apple", "banana", "cherry", "dates", "melon", "watermelon", "grape", "orange",
        "papaya", "pineapple", "kiwi", "pear", "peach", "plum", "guava", "mango",
        "fig", "apricot", "blueberry", "blackberry", "strawberry", "raspberry", "lychee"
    ],
    "cars": [
        "audi", "tesla", "bmw", "mustang", "ferrari", "lamborghini", "porsche", "nissan",
        "toyota", "honda", "volkswagen", "mercedes", "chevrolet", "hyundai", "jaguar"
    ],
    "animals": [
        "tiger", "elephant", "giraffe", "kangaroo", "zebra", "lion", "leopard", "panda",
        "rhinoceros", "hippopotamus", "monkey", "cheetah", "deer", "bear", "fox"
    ]
}

vowels = "aeiou"
total_points = 0

def start_game():
    global total_points

    print("\n Choose a Category:")
    for cat in categories:
        print(f"- {cat}")

    selected = input("\n Choose a category: ").strip().lower()

    
    if selected not in categories:
        print("Invalid category selected.\n")
        return

    words = categories[selected]
    word = random.choice(words)
    wordlen = len(word)
    points = 0

    # First try
    print("\nGuess the word:")
    print("_ " * wordlen)
    guess = input("Your guess: ").strip().lower()

    if guess == word:
        points = 5
        print("Correct on first try!")
    else:
        # Second try 
        hint = word[0] + "_ " * (wordlen - 1)
        print(f"Hint: {hint}")
        guess = input("Second try: ").strip().lower()

        if guess == word:
            points = 2
            print("Correct on second try!")
        else:
            # Third try 
            hint = ""
            for idx, char in enumerate(word):
                if char in vowels or idx == wordlen - 1:
                    hint += char
                else:
                    hint += "_ "
            print(f"Final hint: {hint}")
            guess = input("Last try: ").strip().lower()

            if guess == word:
                points = 1
                print("Correct on last try!")
            else:
                print("Incorrect. No more tries.")

    print(f"The word was: {word}")
    print(f"Points earned: {points}")
    total_points += points
    print(f"Total Score: {total_points} points\n")

def main():
    print("Welcome to Guess the Word!")
    while True:
        print("\nType 'start' to start the game.")
        print("Type 'quit' to exit.")
        command = input("> ").lower()

        if command == "quit":
            print(f"\nThanks for playing! Final Score: {total_points} points.")
            break
        elif command == "start":
            start_game()
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
