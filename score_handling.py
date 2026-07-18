def delete_score():
    with open("score.txt", "w") as score:
        score.write("")

def get_score():
    score = 0
    with open("score.txt") as score_file:
        full_score = list(score_file)
        for scores in full_score:
            if scores == "Correct\n":
                score += 1
    return score

def get_score_length():
    with open("score.txt") as score:
        return len(list(score))