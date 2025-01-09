from pprint import pprint


def read_cookbook(file_path):

    cook_book = {}
    with open(file_path, encoding="utf-8") as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(f.readline())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = f.readline().strip().split(" | ")
                name, quantity, measure = ingredient_info
                ingredients.append(
                    {
                        "ingredient_name": name,
                        "quantity": int(quantity),
                        "measure": measure,
                    }
                )

            cook_book[dish_name] = ingredients
            # Пустая строка между рецептами
            f.readline()
    return cook_book


# Чтение файла рецептов
cookbook_file = 'dishes.txt'
cook_book = read_cookbook(cookbook_file)
pprint(cook_book)
