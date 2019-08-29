import random

heads = "Heads"
tails = "Tails"
numHeads = 0
numTails = 0
flips = int(input("How many flips do you want to toss?: "))
print("................................")
cointoss = [heads, tails]


for flip in range(flips):
    toss = random.choice(cointoss)

    if toss == heads:
        numHeads += 1
    else:
        numTails += 1

    print("Flip #" + str(flip + 1) + ": " + toss)

    percentHeads = numHeads / (flip + 1) * 100
    percentTails = numTails / (flip + 1) * 100

    print('Percent of Heads: ' + str(percentHeads) + '%')
    print('Percent of Tails: ' + str(percentTails) + '%')
