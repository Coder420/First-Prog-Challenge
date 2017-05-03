from collections import OrderedDict
animals = OrderedDict()

foxNoise = []
num_test_cases = int(input(''))

#Loops the amount equal to test cases declared
for i in range(num_test_cases):
    sounds = input('').lower().split()

    animalGoes = input('')
    while animalGoes != 'what does the fox say?':
        tempSentence = animalGoes.split()
        animals.update({tempSentence[0] : tempSentence[2]})
        animalGoes = input('')

    #If the sound in the line matches a known animal sound, it must be removed
    for sound in animals.values():
        while sound in sounds:
            sounds.remove(sound)

    #The unknown sounds are then known as fox sounds which are printed on a single line
    #Example sound:
        #toot woof wa ow ow ow pa blub blub pa toot
    foxLine = ''
    for sound in sounds:
        foxLine = foxLine + sound + ' '
    print(foxLine.rstrip())
