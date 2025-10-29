quiz = [
    ("Who's the best footballer in the history of football?", "Mane", "Mikel obi", "CR7", "Bale", "C"),
    ("Which club is known as the Red Devil?", "Manchester United", "Chelsea", "Juventus", "Club with no European trophy", "A"),
    ("Which club lost against Sunderland last weekend?", "Manchester United", "Chelsea", "Manchester City", "Wolve", "B"),
    ("Which club has the highest Premier League titles in history?", "Chelsea", "Manchester United", "Manchester City", "Arsenal", "B"),
    ("Which club is associated with the word 'Invisible'?", "Manchester United", "Chelsea", "Juventus", "Arsenal", "D"),
    ("Which club is known as the Agberos?", "Manchester United", "Chelsea", "Arsenal", "Liverpool", "B"),
    ("Which club is known in England to produce Ballon d'Or winners?", "Manchester United", "Chelsea", "Juventus", "Club with no European trophy", "A"),
    ("Who is the second best player in the history of football?", "Neymar Jr", "Di Maria", "Messi", "Maguire", "C"),
    ("Which player has the highest goals in this century?", "Messi", "Neymar", "Benzema", "CR7", "D"),
    ("Which player won the golden boot in four different leagues?", "Messi", "Neymar", "Benzema", "CR7", "D")
]

options = ["A", "B", "C", "D"]

def play_game():
	print("""
======================================================================
| Welcome to HYBRID'S multiple choice quiz game to test your         |
| football knowledge.                                                |
| Make the right selection and win a ticket to the WORLD CUP!        |
======================================================================
""")

	score = 0
	number = 0

	while number < len(quiz):
		question, a, b, c, d, correct = quiz[number]		
		print(f"\nQuestion {number + 1}: {question}")
		print(f"A. {a}")
		print(f"B. {b}")
		print(f"C. {c}")
		print(f"D. {d}")

		answer = input("Your answer (A-D): ").strip().upper()

		if answer == correct:
			print(" Correct!")
			score += 1
				
		elif answer in options:
			correct_text = {"A": a, "B": b, "C": c, "D": d}[correct]
			print(f"Wrong! Correct answer was {correct}. {correct_text}")
		else:
			print(" Invalid input. Please enter A, B, C, or D.")
				
		exit_num = input(" Olodo! enter O to exit and X to start again: ")
		if exit_num == "X" or "x":
			play_game()
		

	number += 1

	print(f"\n Game Over! You scored {score} out of {len(quiz)}.")

		
	

play_game()
