# i = 0
# testCases = int(input(''))
# while i <= testCases:
#     profGreet = input('')
#     rank, name = profGreet.split()
#
#     for i in range(0, int(rank)):
#         print('Hello', name)
#     i+=1
from collections import OrderedDict
i = 0
rankProf = OrderedDict()
testCases = int(input(''))
while i < testCases:
    i+=1
    rank, prof = input().split()
    rankProf[prof] = int(rank)

for professor in rankProf:
    for i in range(0, rankProf[professor]):
        print('Hello', professor)
