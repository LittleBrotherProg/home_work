with open(r'.\task_1.txt', 'r', encoding="UTF-8") as f:
    cook_book = {}


    def dish_processing(ingredient_name, quantity, measure):
        ingredient = {"ingredient_name": ingredient_name,
                    "quantity": quantity, "measure": measure}
        return ingredient


    def get_shop_list_by_dishes(dishes, person_count):
        counting_ingredients = {}
        for numb_dish in dishes:
            for ingridient in cook_book.get(numb_dish):
                counting_ingredients[ingridient.get("ingredient_name")] = {}
                counting_ingredients.get(ingridient.get("ingredient_name"))
                count = counting_ingredients[ingridient.get("ingredient_name")]
                count["quantity"] = int(ingridient.get("quantity")) * person_count
                count["measure"] = ingridient.get("measure")
        return counting_ingredients


    lines = f.read()
    lines = lines.split('\n\n')

    for line in lines:
        dish = line.split("\n")
        cook_book[dish[0]] = []
        for ingridient in dish[2:]:
            ingredient_name = (ingridient.split('|')[0]).strip()
            quantity = (ingridient.split('|')[1]).strip()
            measure = (ingridient.split('|')[2]).strip()
            inf_dish = dish_processing(ingredient_name, quantity, measure)
            dict_ing = cook_book[dish[0]]
            dict_ing.append(inf_dish)

    ingridient = get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 2)
    print(ingridient)
