def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10 * len(engraving)
    else: 
        cost = 50 + 7 * len(engraving)
    return cost
print(cost_of_project("Hello, World!", True))  # Solid gold ring
print(cost_of_project("Hello, World!", False))  # Gold plated ring