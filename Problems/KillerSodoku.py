from itertools import combinations


def killer_sodoku(num_cages, total_sum, constraints):
    range_with_constraints = [i for i in range(1, 10) if i not in constraints]
    return print(
        [combo for combo in combinations(range_with_constraints, num_cages) if sum(combo) == total_sum])


killer_sodoku(2, 10, [])
