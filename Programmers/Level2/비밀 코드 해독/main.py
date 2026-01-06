from itertools import combinations

def solution(n, q, ans):
    def satisfies_all_conditions(combi, conditions, expected_intersections):
        combi_set = set(combi)
        return all(
            len(combi_set & set(condition)) == expected 
            for condition, expected in zip(conditions, expected_intersections)
        )
    
    valid_count = sum(
        1 for combi in combinations(range(1, n + 1), 5)
        if satisfies_all_conditions(combi, q, ans)
    )
    
    return valid_count