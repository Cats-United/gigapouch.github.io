from random import randint

inpt = ''
start = 'Make a '
adjectives = ['ancient', 'mountaintop', 'dismal', 'bloody', 'inside out', 'bright', 'dark', 'minimilistic', 'fire-themed','artificial', 'spooky', 'secret', 'lively', 'desert', 'dry', 'sopping wet', 'scary', 'weird', 'large', 'miniature', 'abnormal', 'odd', 'eerie', 'underground', 'enchanted', 'cute']
nouns = ['restauraunt', 'office building', 'railroad line', 'hobbit hole', 'zeppelin or blimp','bathroom', 'lounge', 'geyser', 'tomb', 'roller-coaster', 'mansion', 'cave', 'tunnel', 'waterfall', 'lava lake', 'creeper hangout', 'bell tower', 'zoo', 'swimming pool', 'library', 'railroad', 'house of TNT', 'stone house', 'dance studio', 'pixel art']
area = ['between two villages', 'the mountaintop', 'the mushroom island', 'the plains', 'the desert', 'the Extreme Hills', 'the ocean', 'the island', 'the taiga', 'a town', 'a desert temple']
print 'The length of adjectives is:', len(adjectives), 'The length of nouns is:', len(nouns), 'The length of area is:', len(area)
print 'I can now generate a total of', len(adjectives) * len(nouns) * len(area), 'ideas for you (as of update 42415)'
print 'Welcome to MC Idea Generator!'
print '\n'
while inpt != 'exit':
    print 'Your new idea is to ', start, adjectives[randint(0, len(adjectives) -1)], nouns[randint(0, len(nouns) -1)], "in", area[randint(0, len(area) -1)]
    inpt = raw_input("Would you like another idea? If not, type exit.")
    
