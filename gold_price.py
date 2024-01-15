def cost_of_project(engraving, solid_gold):
    if engraving is None:
        print("No engraving provided")
        return
    if solid_gold is None:
        print("No ring type provided")
        return
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

print(cost_of_project("Hello, World!", True))  # Solid gold ring
print(cost_of_project("Hello, world!", False))  # Gold plated ring
