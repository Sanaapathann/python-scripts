import random
import time
import os


words = [
    "apple", "banana", "grape", "melon", "kiwi", "mango", "peach",
    "chair", "table", "lamp", "pen", "book", "bottle", "phone",
    "car", "train", "bike", "bus", "plane", "boat", "truck",
    "blue", "red", "green", "yellow", "black", "white", "purple",
    "mountain", "river", "cloud", "desert", "beach", "forest"
]

def clear_screen():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def play_memory_game():
    print("\n MEMORY WORD GAME")
    print("Choose difficulty:")
    print("1. Easy (7 words)")
    print("2. Moderate (14 words)")
    print("3. Hard (21 words)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        count = 7
        level = "Easy"
    elif choice == "2":
        count = 14
        level = "Moderate"
    elif choice == "3":
        count = 21
        level = "Hard"
    else:
        print("Invalid choice. Defaulting to Easy.")
        count = 7
        level = "Easy"

    print(f"\nLEVEL: {level.upper()} — Memorize these {count} words:\n")
    memory_words = random.sample(words, count)


    for word in memory_words:
        print(word, end=' ', flush=True)
        time.sleep(0.6)

    clear_screen()

    print("\nType the words you remember (in order, space-separated):")
    guess = input(">> ").strip().lower().split()

    score = 0
    for i in range(min(len(guess), len(memory_words))):
        if guess[i] == memory_words[i]:
            score += 1

    print("\nRESULT:")
    print(f"You got {score}/{count} words in the correct order!")

    if score == count:
        print(" PERFECT! You have a photographic memory!")
    elif score >= count // 2:
        print("Good job! You're getting there.")
    else:
        print("Tough round! Let’s try again.")

    print(f"\nOriginal sequence was:\n{' '.join(memory_words)}")


while True:
    play_memory_game()
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != 'y':
        print("\nThanks for playing! Sharpen your memory every day!")
        break
