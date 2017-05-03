
num_test_cases = int(input(''))
decisions = []
for i in range(num_test_cases):
    decision = input('')
    #list(decision)
    for i in range(0, len(decision)//2):
        decision = decision[1:-1]
        #print(decision)
        if len(decision) == 2:
            decisions.append(decision)
#print(decisions)
for decision in decisions:
    if len(set(decision)) == 1:
        print('Do-it')
    else:
        print('Do-it-Not')
