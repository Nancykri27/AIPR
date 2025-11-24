# Q2.1.PY
# Compute mean of scores and list keys with values above mean

def above_mean(scores):
    values = list(scores.values())
    mean = sum(values) / len(values)
    above = [k for k, v in scores.items() if v > mean]
    return mean, above

if __name__ == "__main__":
    scores = { 'A': 85, 'B': 67, 'C': 92, 'D': 74, 'E': 88 }
    mean, above = above_mean(scores)
    print(f"Mean = {mean:.2f}, Above Mean → {above}")