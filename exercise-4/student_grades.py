students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]}
]

def get_grade(avg):
    for limit, grade in [(70, "A"), (60, "B"), (50, "C"), (45, "D"), (40, "E")]:
        if avg >= limit: return grade
    return "F"

def process(s):
    # Manual average calculation without using sum()
    total = 0
    for score in s["scores"]: total += score
    avg = total / (len(s["scores"]) or 1)
    return (s["name"], avg, get_grade(avg))

# Map & Filter applications
processed = list(map(process, students))
passing = list(filter(lambda x: x[2] in ["A", "B", "C"], processed))

# Manual verification of extremes (No min/max built-ins)
high = low = processed[0]
for s in processed:
    print(f"{s[0]} → Average: {s[1]:.2f} → Grade: {s[2]}")
    if s[1] > high[1]: high = s
    if s[1] < low[1]: low = s

print(f"\nHighest: {high[0]} ({high[1]:.2f})\nLowest: {low[0]} ({low[1]:.2f})")
print(f"Passing: {[p[0] for p in passing]}")
