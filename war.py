from cards import *

ntrials = 10000
awins = 0
bwins = 0
tie = 0

for i in range(ntrials):
    adeck = deck()
    adeck.shuffle()
    total_acards = 0
    total_bcards = 0
    while adeck.cardsleft() > 2:
        acard = adeck.dealcard()
        bcard = adeck.dealcard()
        if acard.value() > bcard.value():
            total_acards += 2
        if bcard.value() > acard.value ():
            total_bcards += 2
        if acard.value() == bcard.value():
            acard = adeck.dealcard()
            bcard = adeck.dealcard()

    if total_acards == total_bcards:
        tie += 1

    if total_acards > total_bcards:
        awins += 1

    if total_bcards > total_acards:
        bwins += 1

print("Tie: ", tie)
print("Player One Wins: ", awins)

for total_acards in range(0, 54, 2):
    print(total_acards, (awins/ntrials))
