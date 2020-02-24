import types
import numpy
import sympy as sp
from sympy import solve_poly_inequality as solvei
from sympy import poly


# CALCULATE RECIPE
def calculate_recipe(ingredients, diet):
    """
    [summary]

    [description]

    Arguments:
        ingredients {array} -- array of Ingredients
        diet {Diet} -- Diet

    Returns:
    """

    # remove fixed ingredient values from diet
    fixed_ingredients = []
    for i in range(len(ingredients)):
        if hasattr(ingredients[i], "fixed") and ingredients[i].fixed is True:

            diet.sugar -= ingredients[i].amount * ingredients[i].sugar
            diet.protein -= ingredients[i].amount * ingredients[i].protein
            diet.fat -= ingredients[i].amount * ingredients[i].fat

            fixed_ingredients.append(ingredients[i])

    # remove fixed ingredients from list of ingredients
    for ing in fixed_ingredients:
        ingredients.remove(ing)

    # move main ingredient to end of list
    for i in range(len(ingredients)):
        if hasattr(ingredients[i], "main") and ingredients[i].main is True:
            mainIngredient = ingredients[i]
            ingredients.pop(i)
            ingredients.append(mainIngredient)
            break

    # calculate
    if len(ingredients) == 0:
        return None
    elif len(ingredients) == 1:
        # TODO: Teoreticky je možné (99)
        return None
    elif len(ingredients) == 2:
        # TODO: Teoreticky je možné (99)
        return None
    elif len(ingredients) == 3:
        a = numpy.array(
            [
                [ingredients[0].sugar, ingredients[1].sugar, ingredients[2].sugar],
                [ingredients[0].fat, ingredients[1].fat, ingredients[2].fat],
                [
                    ingredients[0].protein,
                    ingredients[1].protein,
                    ingredients[2].protein,
                ],
            ]
        )
        b = numpy.array([diet.sugar, diet.fat, diet.protein])
        x = numpy.linalg.solve(a, b)

        ingredients[0].amount = x[0]
        ingredients[1].amount = x[1]
        ingredients[2].amount = x[2]

    elif len(ingredients) == 4:
        x, y, z = sp.symbols("x, y, z")
        e = sp.symbols("e")

        # set of linear equations
        f1 = (
            ingredients[0].sugar * x
            + ingredients[1].sugar * y
            + ingredients[2].sugar * z
            + ingredients[3].sugar * e
            - (diet.sugar)
        )
        f2 = (
            ingredients[0].fat * x
            + ingredients[1].fat * y
            + ingredients[2].fat * z
            + ingredients[3].fat * e
            - (diet.fat)
        )
        f3 = (
            ingredients[0].protein * x
            + ingredients[1].protein * y
            + ingredients[2].protein * z
            + ingredients[3].protein * e
            - (diet.protein)
        )

        # solve equations with args
        in1 = sp.solvers.solve((f1, f2, f3), (x, y, z))[x]
        in2 = sp.solvers.solve((f1, f2, f3), (x, y, z))[y]
        in3 = sp.solvers.solve((f1, f2, f3), (x, y, z))[z]

        # solve for positive numbers
        result1 = solvei(poly(in1), ">=")
        result2 = solvei(poly(in2), ">=")
        result3 = solvei(poly(in3), ">=")

        interval = (result1[0].intersect(result2[0])).intersect(result3[0])
        if interval.is_empty:
            return None

        max_sol = min(100, round(interval.right, 2))
        min_sol = max(0, round(interval.left, 2))
        if max_sol < min_sol:
            return None

        # max_sol = max for e (variable)
        sol = (min_sol + max_sol) / 2

        in1_dict = in1.as_coefficients_dict()
        x = in1_dict[e] * sol + in1_dict[1]

        in2_dict = in2.as_coefficients_dict()
        y = in2_dict[e] * sol + in2_dict[1]

        in3_dict = in3.as_coefficients_dict()
        z = in3_dict[e] * sol + in3_dict[1]

        x = round(x, 4)
        y = round(y, 4)
        z = round(z, 4)

        if x < 0 or y < 0 or z < 0:
            return None

        ingredients[0].amount = x
        ingredients[1].amount = y
        ingredients[2].amount = z
        ingredients[3].amount = sol
        ingredients[3].min = float(min_sol * 100)
        ingredients[3].max = float(max_sol * 100)

    elif len(ingredients) == 5:
        # TODO: 5 ingredients (30)
        return None
    else:
        return None

    for ing in fixed_ingredients:
        ingredients.append(ing)

    totals = types.SimpleNamespace()
    totals.sugar = 0
    totals.fat = 0
    totals.protein = 0
    totals.amount = 0
    totals.calorie = 0

    for ingredient in ingredients:
        ingredient.calorie = ingredient.calorie * ingredient.amount
        ingredient.fat = ingredient.fat * ingredient.amount
        ingredient.sugar = ingredient.sugar * ingredient.amount
        ingredient.protein = ingredient.protein * ingredient.amount

        totals.sugar += ingredient.sugar
        totals.fat += ingredient.fat
        totals.protein += ingredient.protein
        totals.calorie += ingredient.calorie
        totals.amount += ingredient.amount

    # json cannot convert `sympy.Float`, so I convert everything to Python `float`
    for ingredient in ingredients:
        ingredient.calorie = float(ingredient.calorie)
        ingredient.fat = float(ingredient.fat)
        ingredient.sugar = float(ingredient.sugar)
        ingredient.protein = float(ingredient.protein)
        ingredient.amount = float(ingredient.amount)

    totals.sugar = float(totals.sugar)
    totals.fat = float(totals.fat)
    totals.protein = float(totals.protein)
    totals.calorie = float(totals.calorie)
    totals.amount = float(totals.amount)

    diet.expire()
    return {"ingredients": ingredients, "totals": totals}