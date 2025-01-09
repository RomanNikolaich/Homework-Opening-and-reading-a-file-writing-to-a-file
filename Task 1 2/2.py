from cook_book import cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):

    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book.get(dish, []):
            ingredient_name = ingredient["ingredient_name"]
            if ingredient_name in shop_list:
                shop_list[ingredient_name]["quantity"] += (
                    ingredient["quantity"] * person_count
                )
            else:
                shop_list[ingredient_name] = {
                    "measure": ingredient["measure"],
                    "quantity": ingredient["quantity"] * person_count,
                }
    return shop_list


result = get_shop_list_by_dishes(cook_book, ["Запеченный картофель", "Омлет"], 2)
print(result)
