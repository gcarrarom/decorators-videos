def cooking(recipe):
    def cooking_recipe():
        prep()
        recipe()
        cleanup()
    return cooking_recipe

def prep():
    print("Go to the kitchen")
    print("Get the igredients")
    print("Get the equipments - Dishes, Cutlery")

def cleanup():
    print("WASH THE DISHES! :)")

@cooking
def cook_rice():
    '''
    Recipe for Rice
    '''
    print("Wash the rice")
    print("Add the rice to a pan with water")
    print("...")

@cooking
def cook_egg():
    '''
    Recipe for Egg
    '''
    print("Heat oil in a frying pan")
    print("Crack an egg in a container")
    print('...')

cook_egg()
cook_rice()
