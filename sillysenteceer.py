import random

persons = ['Hugh', 'Janet', 'Clara', 'David', 'Plaicius Holdeir', 'Sam']
verbs = ['ran', 'fought', 'read', 'worked', 'drove the', 'built']
adjectives = ['meaningfully', 'fast',' hard',' loose', 'slipery', 'bad']
nouns = ['book', 'monster', 'road', 'fish', 'ball', 'boat']

BASE_sen = 'Dad approved of my work'
template = '%s %s the %s %s'

if __name__=='__main__':
    person = random.choice(persons)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    format_values = (person, verb, adjective, noun)

print(template%format_values)
