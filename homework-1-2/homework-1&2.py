import os
file_path = os.path.join(os.getcwd(), 'homework-1-2/cook-book.txt')
print()

with open(file_path, 'r', encoding='utf-8') as f:
    cook_book = {}
    file = f.read().split('\n\n')
    for recepy in file:
        dish_components = []
        name, num_ingridients, *ingridients = recepy.split('\n')
        dish_components.append([*ingridients])
        dish = []
        for ingridient in dish_components[0]:
            ingridient = ingridient.split(' | ')
            dish.append({'ingredient_name': ingridient[0], 'quantity': int(ingridient[1]), 'measure': ingridient[2]})
        cook_book[name] = dish
    print('cook_book = {')
    for receipt in cook_book:
        print(f"  '{receipt}': [")
        for ingrid in cook_book[receipt]:
            print(f"    {ingrid},")
        print('    ]')
    print('\n  }')

def get_shop_list_by_dishes(dishes, person_count):
    products = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingredient_name'] in products:
                products[ingridient['ingredient_name']]['quantity'] +=  ingridient['quantity']*person_count
            else:
                products[ingridient['ingredient_name']] =  {'measure': ingridient['measure'], 'quantity': ingridient['quantity']}
                products[ingridient['ingredient_name']]['quantity'] *= person_count
    print('{')  
    for product in products:
        print('  ', f"'{product}':", products[product])
    print('}')

print('\nВывод функции:')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)