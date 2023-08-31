from fractions import Fraction

favorable_outcomes = 0

for die1 in range(1, 7):
    for die2 in range(1, 7):
        if die1 != die2 and die1 + die2 == 6:
            favorable_outcomes += 1

total_possible_outcomes = 6 * 6

probability = Fraction(favorable_outcomes,total_possible_outcomes)
print(probability)

