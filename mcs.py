import random
total_flips = 0
max_flips = 0
trials = 10000

for i in range(trials):
    current_trial_flips = 0
    heads = False

    while not heads:
        current_trial_flips += 1
        if random.randrange(2) == 1:
            heads = True

    total_flips += current_trial_flips

    if current_trial_flips > max_flips:
        max_flips = current_trial_flips


average_flips = total_flips / trials

print("Average number of flips", average_flips)
print("Maximum number of flips", max_flips)
