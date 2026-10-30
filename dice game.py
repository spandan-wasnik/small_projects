import random
again=True
while again:
    print(random.randint(1,6))
    print("Do you want to roll again? (y/n)")
    answer=input()
    if answer.lower() != 'y':
        again=False
    else:
        continue

