import datetime
import decimal
from timeit import default_timer as timer
from random import sample

ctx = decimal.Context()
ctx.prec = 20


def build_deck(cards, suits, ranks):
    for i in range(suits):
        for j in range(ranks):
            cards.append(j + 1)


def float_to_string(f):
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')


def snap(deck):
    last = 0
    snaps = 0
    for card in deck:
        if card == last:
            snaps += 1
            last = 0
        else:
            last = card
    return snaps


def main():
    #   Runtime per iteration measured in seconds. Longer running time will give more accurate results, up to a point.
    #   This could be replaced by checking when the results start to settle but I only expect to run this once.
    runtime = 1800
    #   Repetitions per suit/rank combination
    repetitions = 5
    ranks = 10

    for suits in range(2, 7):
        for reps in range(repetitions):
            cards = []
            build_deck(cards, suits, ranks)
            completed = 0
            results = []
            percents = []
            start = timer()
            while True:
                deck = sample(cards, len(cards))
                this_result = snap(deck)
                while this_result >= len(results):
                    results.append(0)
                results[this_result] += 1
                completed += 1
                #    print(completed, deck, timer(), results)
                if timer() - start > runtime:
                    break
            end = timer()
            for result in results:
                percents.append(result / completed * 100)
            with open('out.txt', 'a') as outfile:
                outfile.write(str(datetime.datetime.now()) + "\n")
                outfile.write("Suits = " + str(suits) + ", Ranks = " + str(ranks) + "\n")
                outfile.write("Cards = " + str(cards) + "\n")
                outfile.write("Repetition #" + str(reps + 1) + "\n")
                for i in range(0, len(results)):
                    outfile.write(str(i) + " " + float_to_string(results[i]) + " " + float_to_string(percents[i]) + '%' + "\n")
                outfile.write("Elapsed time = " + str(end - start) + ", Samples = " + str(completed) + "\n\n")

            with open('out.csv', 'a') as outfile:
                for i in range(0, len(results)):
                    outfile.write(str(suits) + "," + str(ranks) + "," + str(reps) + "," + str(i) + "," + float_to_string(results[i]) + "," + float_to_string(percents[i]) + '%' + "\n")

            print("Suits = " + str(suits) + ", Ranks = " + str(ranks) + ", Repetition #" + str(reps + 1) + " complete")


main()
