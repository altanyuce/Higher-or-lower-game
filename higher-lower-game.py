from art import logo, vs
from game_data import data
import random

final_score = 0
end_game = False
compare_a = 0
compare_b = 0
print(logo)

while compare_a == compare_b:
    compare_a = random.choice(data)
    compare_b = random.choice(data)
while not end_game:
    compare_a = compare_b
    while compare_a == compare_b:
        compare_b = random.choice(data)

    first = compare_a
    second = compare_b

    print(f"Compare A: {first['name']}, {first['description']}, from {first['country']}.")
    print(vs)
    print(f"Compare B: {second['name']}, {second['description']}, from {second['country']}.")


    if first['follower_count'] > second['follower_count']:
        answer = 'A'
    else:
        answer = 'B'
    player_choice = input("Who has more follower? Type 'A' or 'B': ").upper()

    if player_choice == answer:
        final_score += 1
        print(f"You're right! Current score: {final_score}")
    else:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        end_game = True

