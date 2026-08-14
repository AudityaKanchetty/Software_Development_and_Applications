"""Q3: Recipe Scaler (Functions)"""

def scale_recipe(name: str, servings: int, *ingredients, unit: str = "g", **options):
    if servings < 1:
        print(f"ERROR: '{name}' needs servings >= 1, got {servings}")
        return 0

    print(f"\n=== {name.upper()} (servings: {servings}) ===")
    print("Shopping list:")
    scaled = {}
    for ingredient, amount_per_serving in ingredients:
        amount = amount_per_serving * servings
        scaled[ingredient] = amount
        print(f"  {ingredient}: {amount} {unit}")

    if options:
        print("Cooking notes:")
        for key, value in options.items():
            print(f"  {key}: {value}")

    return scaled


# ============================================================================
# DEMO BLOCK
# ============================================================================
if __name__ == "__main__":
    # Call 1: Simple recipe
    scale_recipe("Pasta", 4, ("pasta", 100), ("tomato sauce", 200), ("cheese", 50))
    
    # Call 2: Different unit
    scale_recipe("Smoothie", 2, ("milk", 250), ("yogurt", 100), unit="ml")
    
    # Call 3: Several options
    scale_recipe("Cake", 6, ("flour", 200), ("sugar", 150), oven="180C", time="45min")
    
    # Call 4: Servings < 1 (Error handling)
    scale_recipe("Pizza", 0, ("dough", 250))