import random

questions = [
    "Name a fruit.",
    "Name a fast food item.",
    "Name a country.",
    "Name a cartoon character.",
    "Name a color.",
    "Name an animal.",
    "Name a city in India.",
    "Name a movie star.",
    "Name a popular sport.",
    "Name a subject in school."
]


num_players = int(input("Enter number of players (2–5): "))
players = [f"Player {i+1}" for i in range(num_players)]
scores = {player: 0 for player in players}

def play_round():
    question = random.choice(questions)
    print("\nThink like the herd!")
    print(f"Question: {question}\n")

    answers = {}
    for player in players:
        ans = input(f"{player}, your answer (no one else peek!): ").strip().lower()
        answers[player] = ans


    print("\nAnswers from players:")
    for player, ans in answers.items():
        print(f"{player}: {ans}")

    
    count_map = {}
    for ans in answers.values():
        count_map[ans] = count_map.get(ans, 0) + 1

    
    max_count = max(count_map.values())
    most_common_answers = [ans for ans, cnt in count_map.items() if cnt == max_count]

  
    print("\nRound Result:")
    for player, ans in answers.items():
        if len(most_common_answers) == 1 and ans == most_common_answers[0]:
            if max_count == num_players:
                print(f"{player} matched *everyone*! +2 points")
                scores[player] += 2
            else:
                print(f"{player} is in the majority! +1 point")
                scores[player] += 1
        else:
            print(f"{player} is out of sync! No points")


    print("\nScoreboard:")
    for player in players:
        print(f"{player}: {scores[player]}")

while True:
    play_round()
    again = input("\nPlay another round? (y/n): ").strip().lower()
    if again != "y":
        print("\nGame Over! Final Scores:")
        for player in players:
            print(f"{player}: {scores[player]}")
        break
