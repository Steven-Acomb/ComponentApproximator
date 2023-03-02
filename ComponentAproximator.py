from math import floor, pi

# Should be a Data Class
class Component:
    def __init__(self, name, operations):
        self.name = name
        self.operations = operations

class Recipe:
    def __init__(self, operation, parameter_values):
        self.operation = operation
        self.parameter_values = parameter_values
            
    def equals(self, recipe):
        return (self.operation == recipe.operation) and (self.parameter_values == recipe.parameter_values)
    
    def to_str(self):
        recipe_str = self.operation.__name__ + "("
        for v in range(len(self.parameter_values)):
            recipe_str = recipe_str + str(self.parameter_values[v])
            if v < len(self.parameter_values)-1:
                recipe_str = recipe_str + ", "
        recipe_str = recipe_str + ")"
        return recipe_str

def in_previous_tiers(result_value, tiers):
    for tier in tiers:
        if result_value in tiers[tier]:
            return True
    return False

def approximate_component(type, desired_value, base_values, max_order):
    value_recipe = {}
    for value in base_values:
        base_recipe = Recipe(base_operation, [value])
        value_recipe[value] = [base_recipe]
    tiers = {}
    tiers[1] = base_values

    for k in range(max_order): # generate the components at every allowable tier:
        sum_tier = k+1
        tier_values = []
        for j in range(floor(sum_tier/2)): # generate the combinations for this tier:
            tier_a = j+1
            tier_b = sum_tier-(j+1)
            new_values = [] # for printing
            if tier_a == tier_b: # diagonal_merge(tier_a)
                tier_a_values = tiers.get(tier_a)
                tier_a_values.sort()
                for a in range(len(tier_a_values)):
                    for b in range(a+1):
                        for operation in type.operations:
                            value_a = tier_a_values[a]
                            value_b = tier_a_values[b]
                            result_value = operation(value_a,value_b)
                            if not in_previous_tiers(result_value, tiers):
                                new_recipe = Recipe(operation, [value_a, value_b])
                                if result_value in tier_values:
                                    result_recipes = value_recipe.get(result_value)
                                    result_recipes.append(new_recipe)
                                    value_recipe[result_value] = result_recipes
                                else:
                                    new_values.append(result_value) # for printing
                                    tier_values.append(result_value)
                                    value_recipe[result_value] = [new_recipe]
            else:  # rectangular_merge(tier_a, tier_b)
                tier_a_values = tiers.get(tier_a)
                tier_b_values = tiers.get(tier_b)
                new_values = [] # for printing
                for val_a in tier_a_values:
                    for val_b in tier_b_values:
                        for operation in type.operations:
                            result_value = operation(val_a,val_b)
                            if not in_previous_tiers(result_value, tiers):
                                new_recipe = Recipe(operation, [val_a, val_b])
                                if result_value in tier_values:
                                    result_recipes = value_recipe.get(result_value)
                                    result_recipes.append(new_recipe)
                                    value_recipe[result_value] = result_recipes
                                else:
                                    new_values.append(result_value) # for printing
                                    tier_values.append(result_value)
                                    value_recipe[result_value] = [new_recipe]
            if sum_tier > 1:
                tiers[sum_tier] = tier_values
                print("new_values = " + str(new_values)) # for printing
                print()
    closest_value = base_values[0]
    closest_distance = abs(desired_value**2-closest_value**2)
    values = []
    for key in value_recipe.keys():
        current_distance = abs(desired_value**2-key**2)
        values.append(key)
        if current_distance < closest_distance:
            closest_value = key
            closest_distance = current_distance
    values.sort()
    print("complete list of values: " + str(values))
    print("closest_value = " + str(closest_value))
    
    print("recipes for " + str(closest_value) + ":")
    aproximate_recipes = value_recipe.get(closest_value)
    for recipe in aproximate_recipes:
        recipe_str = recipe.to_str()
        print(recipe_str)
    
    # print("one recipe for " + str(closest_value) + ":")

# Base Operation
def base_operation(value, repeat):
    if value == repeat:
        return value
    else:
        print("ERROR: Base recipe called with two different values.")
        return value

# Resistor Operations
def r_series(r1, r2):
    return r1+r2
def r_parallel(r1, r2):
    return (1/((1/r1)+(1/r2)))
r_ops = []
r_ops.append(r_series)
r_ops.append(r_parallel)
r = Component("Resistor", r_ops)

# Capacitor Operations
def c_series(c1, c2):
    return (1/((1/c1)+(1/c2)))
def c_parallel(c1, c2):
    return c1+c2
c_ops = []
c_ops.append(c_series)
c_ops.append(c_parallel)
c = Component("Capacitor", c_ops)

# Arrays containing all "standard" (rose parts room, not E series) resistor and capacitor values
rose_resistors = [1, 1.5, 2.7, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1, 10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91, 100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910, 1000, 1100, 1200, 1300, 1500, 1600, 1800, 2000, 2200, 2400, 2700, 3000, 3300, 3600, 3900, 4500, 4700, 5100, 5600, 6200, 7500, 8200, 9100, 10000, 11000, 12000, 13000, 15000, 16000, 18000, 20000, 22000, 24000, 27000, 30000, 33000, 36000, 39000, 43000, 47000, 51000, 56000, 62000, 68000, 75000, 82000, 91000, 100000, 110000, 120000, 130000, 150000, 160000, 180000, 200000, 220000, 240000, 270000, 300000, 330000, 360000, 390000, 430000, 470000, 510000, 560000, 620000, 680000, 750000, 820000, 910000, 1000000, 1100000, 1200000, 1300000, 1500000, 1600000, 1800000, 2000000, 2100000, 2200000, 2400000, 2700000, 3000000, 3300000, 3600000, 3900000, 4700000, 5600000, 6800000, 8200000, 10000000]
rose_capacitors = [1.8*10**-12, 2.25*10**-12, 7.5*10**-12, 10*10**-12, 12*10**-12, 18*10**-12, 22*10**-12, 27*10**-12, 33*10**-12, 47*10**-12, 68*10**-12, 100*10**-12, 220*10**-12, 330*10**-12, 470*10**-12, 1000*10**-12, 1500*10**-12, 2200*10**-12, 4700*10**-12, 5000*10**-12, 0.01*10**-6, 0.022*10**-6, 0.033*10**-6, 0.047*10**-6, 0.1*10**-6, 0.22*10**-6, 0.33*10**-6, 0.47*10**-6, 0.68*10**-6, 1*10**-6, 2.2*10**-6, 3.3*10**-6, 4.7*10**-6, 10*10**-6, 22*10**-6, 33*10**-6, 47*10**-6, 100*10**-6, 220*10**-6, 470*10**-6, 680*10**-6, 1000*10**-6, 1500*10**-6, 4700*10**-6]

chanzon_resistors = [1, 1.5, 2.2, 2.7, 3.3, 3.9, 4.7, 5.1, 6.8, 10, 15, 20, 22, 33, 47, 51, 56, 100, 150, 220, 330, 390, 470, 1*10**3, 2.2*10**3, 4.7*10**3, 47*10**3, 10*10**3, 100*10**3, 1*10**6]
hilitchi_capacitors = []

# 
# Testing
# 

# base_values = rose_capacitors
# max_order = 2
# type = c
# desired_value = pi*10**-6
# approximate_component(type, desired_value, base_values, max_order)

base_values = rose_resistors
max_order = 2
type = r
desired_value = pi
approximate_component(type, desired_value, base_values,max_order)
