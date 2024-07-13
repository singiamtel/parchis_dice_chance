import random
import numpy as np
import matplotlib.pyplot as plt

dice_sides = [1, 2, 3, 4, 5, 6]
results = {}

# Show all the outcomes of rolling two dice
# If both dice roll the same number, we roll again (only trhee rolls at most)

def inc(total, divisor=1):
    if total in results:
        results[total] += (1 / divisor)
    else:
        results[total] = (1 / divisor)


def permutate(depth=0, prevdie1=0, prevdie2=0):
    global results
    if depth > 2:
        inc(0, (len(dice_sides) ** 2) ** 2)
        return
    for die1 in dice_sides:
        for die2 in dice_sides:
            total = die1 + die2
            if die1 == die2:
                permutate(depth + 1, die1 + prevdie1, die2 + prevdie2)
            else:
                inc(total + prevdie1 + prevdie2, (len(dice_sides) ** 2) ** depth)

def random_rolls():
    for _ in range(1000000):
        die1 = int(random.choice(dice_sides))
        die2 = int(random.choice(dice_sides))
        total = die1 + die2
        if die1 == die2:
            die1 = random.choice(dice_sides)
            die2 = random.choice(dice_sides)
            total += die1 + die2
            if die1 == die2:
                die1 = random.choice(dice_sides)
                die2 = random.choice(dice_sides)
                total += die1 + die2
                if die1 == die2:
                    inc(0)
                    continue
        inc(total)

def main():
    global results
    permutate()
    full = sum(results.values())
    normalized_all = {total: (count / full) for total, count in results.items()}
    results = {}
    random_rolls()
    full = sum(results.values())
    normalized_random = {total: (count / full) for total, count in results.items()}

    fig, ax = plt.subplots(2)

    assert isinstance(ax, np.ndarray) # shut up LSP
    ax[0].bar(normalized_all.keys(), normalized_all.values(), color='b')
    ax[0].set_title('Permutated')
    ax[1].bar(normalized_random.keys(), normalized_random.values(), color='r')
    ax[1].set_title('Random')

    plt.show()
    
if __name__ == '__main__':
    main()
