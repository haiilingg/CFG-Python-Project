ingredients = input('Enter an ingredient? ')

is_allergic = ['peanuts','milk','butter','cheese','yogurt','wheat','shellfish','fish','treenuts','nuts']

if ingredients in is_allergic:
    print('My friend is allergic to this :(')
else:
    print('My friend can eat this yay!')

