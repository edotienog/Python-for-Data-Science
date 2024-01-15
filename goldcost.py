def cost_of_project(engraving: str, solid_gold: bool) -> int:
    base_cost = 100 if solid_gold else 50
    engraving_cost = 10 if solid_gold else 7
    total_cost = base_cost + engraving_cost * len(engraving)
    return total_cost
print(cost_of_project("Hello, World!", True))  # Solid gold ring
print(cost_of_project("Hello, World!", False))  # Gold plated ring
