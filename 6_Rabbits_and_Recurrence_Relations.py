# http://rosalind.info/problems/fib/
# Rabbits and Recurrence Relations

# Explanation
"""
    Wascally Wabbits Rules :::

    1. The population begins in the first month with a pair of newborn rabbits.
    2. Rabbits reach reproductive age after one month.
    3. In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
    4. Exactly one month after two rabbits mate, they produce one male and one female rabbit.
    5. Rabbits never die or stop reproducing.
    -----------------------------------------------------------------------------------
    C - immature (child) rabbits. They will mature in the next month.
    P - mature (parents) rabbits.
    Newborn Rabbits - 2

    Month 1: [C]
    Month 2: [P]
    Month 3: [P C C]
    Month 4: [P C C P P]
    Month 5: [P C C P P P C C P C C]
    Month 6: [P C C P P P C C P C C P C C P P P C C P P]
"""


def get_total_rabbits(months, newborn_rabbits):
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * newborn_rabbits)
        # print(str(itr) + " C: " + str(child) + " - P: " + str(parent) + "\n")

    return child


if __name__ == "__main__":
    print("The total number of rabbit pairs : " + str(get_total_rabbits(3, 5)))
