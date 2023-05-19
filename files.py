
with open('recipes.txt','rt',encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        meat_name = line.strip()
        ingredients_qty = int(file.readline())
        ingredients = []
        for i in range(ingredients_qty):
            ing = file.readline()
            ingredient_name, quantity, measure = ing.split(' | ')
            ingredient = {
                'ingredient_name': ingredient_name, 
                'quantity':quantity, 
                'measure':measure
            }
            ingredients.append(ingredient)
        file.readline()
        cook_book[meat_name] = ingredients
    print(cook_book)
def get_shop_list_by_dishes(dishes, person_count:int):
    ingredients_total = {}
    for dish in dishes:
        if dish in cook_book:
            
            ingredient_dict = cook_book[dish]['ingredient_name']
            print(ingredient_dict)
        else:
            print('Нет такого блюда')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)