def read_cookbook(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_data = file.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_data[0],
                    'quantity': int(ingredient_data[1]),
                    'measure': ingredient_data[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book

cook_book = read_cookbook('recipes.txt')
print(cook_book)
