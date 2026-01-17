import json
from rapidfuzz import fuzz

def load_problems():
    with open("knowledge_base/problems.json", "r", encoding="utf-8") as f:
        return json.load(f)

def find_best_problem(user_input, problems):
    user_input = user_input.lower()
    best_match = None
    highest_score = 0

    for problem in problems:
        for keyword in problem["keywords"]:
            score = fuzz.partial_ratio(user_input, keyword.lower())
            if score > highest_score:
                highest_score = score
                best_match = problem

    if highest_score >= 60:
        return best_match
    return None
