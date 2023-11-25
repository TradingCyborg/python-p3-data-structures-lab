spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get('spiciness',0) >5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name', 'Unknown Food')
        cuisine = food.get('cuisine', 'Unknown Cuisine')
        spiciness =food.get('spiciness', 0)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        cuisine = food.get('cuisine', '').lower()
        if cuisine == cuisine.lower():
            return food
    
def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
