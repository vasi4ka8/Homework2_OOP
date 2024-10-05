
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



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:

                    shop_list[ingredient_name]['quantity'] += quantity
                else:

                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' отсутствует в книге рецептов.")

    return shop_list


cook_book = read_cookbook('recipes.txt')

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print(shop_list)
