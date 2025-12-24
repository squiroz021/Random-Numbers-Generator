import random

def generate_strategic_pick():
    while True:
        white_balls = random.sample(range(1, 70), 5) # gen 5 unique white balls
        
        total_sum = sum(white_balls)
        num_high = len([n for n in white_balls if n > 34]) # low/high numbers filter
        num_odd = len([n for n in white_balls if n % 2 != 0]) # odd numbers filter
        
        if 130 <= total_sum <= 180 and (2 <= num_high <= 3) and (2 <= num_odd <= 3):
            powerball = random.randint(1, 26)
            return sorted(white_balls), powerball

# Example: Generate 3 smart plays
for i in range(3):
    print(f"Play {i+1}: {generate_strategic_pick()}")
