from fractions import Fraction
production_a = 500 * 2
pA = 0.005
production_b = 1000 * 2
pB = 0.008
production_c = 2000 * 2
pC = 0.010
defA = ['defA' for _ in range(int(production_a * pA))]
defB = ['defB' for _ in range(int(production_b * pB))]
defC = ['defC' for _ in range(int(production_c * pC))]

totalDef = defA + defB + defC

probability = Fraction(len(defA), len(totalDef))

print(probability)
