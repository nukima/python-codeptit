n = int(input())
score = input().split()
score = [float(i) for i in score]
highest = max(score)
lowest = min(score)
while highest in score:
    score.remove(highest)
while lowest in score:
    score.remove(lowest)

ave_score = round(sum(score) / len(score), 2)
print(ave_score)
