# same-bread-deck-maker
Program to help determine how many sets of cards to print for a decent number of same breads per game.\
Game is available from https://www.sarahandduck.com/make/sarah-duck-same-bread-card-game/ and is snap with pictures of bread.\
4 gets to around 1/20 with no snap, 5 gets to around 1/60, 6 gets to around 1/200.

Sample out.txt
--------------
2020-06-11 01:43:39.655403\
Suits = 2, Ranks = 10\
Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\
Repetition #1\
0 43437 35.89805042933529%\
1 45733 37.795555408632985%\
2 22723 18.779183643110386%\
3 7249 5.990859579672896%\
4 1544 1.276022512210643%\
5 275 0.22727084900124794%\
6 34 0.02809894133106338%\
7 5 0.004132197254568144%\
8 1 0.0008264394509136289%\
Elapsed time = 5.000026273, Samples = 121001

For each repetition, each line consists of #of snaps, #of games having this many snaps, %of games having this many snaps.

Sample out.csv
--------------
2,10,0,0,43437,35.89805042933529%\
2,10,0,1,45733,37.795555408632985%\
2,10,0,2,22723,18.779183643110386%\
2,10,0,3,7249,5.990859579672896%\
2,10,0,4,1544,1.276022512210643%\
2,10,0,5,275,0.22727084900124794%\
2,10,0,6,34,0.02809894133106338%\
2,10,0,7,5,0.004132197254568144%\
2,10,0,8,1,0.0008264394509136289%

#of sets of cards, #of cards per set, #of the repetition, #of snaps per game, #of games with that many snaps, %of games with that many snaps.

Numbers are lower bounds, with cards not being repeated after a snap.
