def cost_of_project(engraving, solid_gold):
    num_units = len(engraving)
    if solid_gold == True:
        cost = 100 + 10 * num_units
    else: 
        cost = 50 + 7 * num_units
    return cost
print(cost_of_project("James Bond 007", True))  # Solid gold ring
print(cost_of_project("Discipline, Order, Competence", False))  # Gold plated ring
