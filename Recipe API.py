import requests

def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '6c45474b'
    app_key = 'b3f673127fa8ff3bd4e66c07cfed02d3'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,
                                                                         app_key)
    )
    data = result.json()

    return data['hits']

def run():
    ingredients = []

    while True:
        ingredient = input('What do you have in your kitchen? (enter "done" to finish): ')

        if ingredient.lower() == 'done':
            break

        ingredients.append(ingredient)

    for ingredient in ingredients:
        results = recipe_search(ingredient)

        for result in results:
            recipe = result['recipe']

            print(recipe['label'])
            print(recipe['uri'])
            print()
run()