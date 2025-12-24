import random
from collections import Counter

def generate_strat_pick():
    while True:
        white_balls = random.sample(range(1, 70), 5) # gen 5 unique white balls
        
        #basic stta calculations
        total_sum = sum(white_balls)
        num_high = len([n for n in white_balls if n > 34]) # low/high numbers 
        num_odd = len([n for n in white_balls if n % 2 != 0]) # odd numbers

        #multiples filter 
        is_multiple = False

        for base in range(2, 13): # checks multiples of 2 through 12
            if all(n % base == 0 for n in white_balls): # if all numbers have a multiple of the same number
                is_multiple = True
                break
        
        if is_multiple:
            continue
        
        #last digits filter 
        last_digits = [n % 10 for n in white_balls]
        digit_counts = Counter(last_digits)

        #birthday filter
        above_31_count = len([n for n in white_balls if n > 31])
        if above_31_count < 3:
            continue

        # remove # if any ending digit appears more than 2 times
        if any(count > 2 for count in digit_counts.values()):
            continue

        #lln - 70% of winning draws for Powerball fall between 130 and 180
        if 130 <= total_sum <= 180 and (2 <= num_high <= 3) and (2 <= num_odd <= 3): 
            powerball = random.randint(1, 26) 
            return white_balls, powerball

print("--- 2025 Powerball Optimized ---")
for i in range(5):
    nums, pb = generate_strat_pick()
    print(f"Play {i+1}: White Balls: {nums} | Powerball: {pb}")

# term command: python3 /Users/stephaniequiroz/Desktop/Random-Numbers-Generator/random_1.py