from pprint import pprint
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
#    print(cook_book)
def get_shop_list_by_dishes(dishes, person_count:int):
    shop_list={}
    for dish in dishes:
        if dish in cook_book:
            ingredients=cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = int(ingredient['quantity'])*person_count
                if name in shop_list:
                    shop_list[name][quantity]+=quantity
                else:
                    shop_list[name]={'measure':measure,'quantity':quantity}
        else:
            print('Нет такого блюда')
    pprint(shop_list)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)