# Q2.3.py
# Compute mean of student marks and list students above the mean

def mean_and_above(marks):
    if not marks:
        return 0.0, []
    mean_val = sum(marks.values()) / len(marks)
    above = [name for name, score in marks.items() if score > mean_val]
    return mean_val, above

if __name__ == "__main__":
    data = { 'A': 85, 'B': 67, 'C': 92, 'D': 74, 'E': 88 }
    mean_val, above_students = mean_and_above(data)
    print(f"Mean = {mean_val:.2f}, Above Mean → {above_students}")