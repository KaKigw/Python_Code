import random

max_throws = 100
for throw in range(1, max_throws + 1):
    result = random.randint(0, 1)  # 0 for Tails, 1 for Heads
    side = "Heads" if result == 1 else "Tails"
    print(f"Throw {throw}: {side}")
    if result == 1:
        print(f"Heads appeared on throw number {throw}")
        break
else:
    print("Heads never appeared in 100 throws.")
