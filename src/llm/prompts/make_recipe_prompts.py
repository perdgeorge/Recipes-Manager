CALORIE_CALCULATION_PROMPT = """

Given the following recipe, analyze the ingredients and their quantities. Provide the approximate calories for each individual ingredient based on standard nutritional data, and then calculate the total calories for the entire recipe.
Recipe: {recipe_text}

Please respond ONLY with a valid JSON object in the following format:
{{
"ingredients": [
{{"name": "ingredient_name", "quantity": "amount", "calories": calorie_value}},
{{"name": "ingredient_name", "quantity": "amount", "calories": calorie_value}}
],
"total_calories": total_value
}}
Use approximate values based on common nutritional databases. Be conservative with estimates. If quantities are not specified, use standard serving sizes.
Return ONLY the JSON object, no additional text
"""
