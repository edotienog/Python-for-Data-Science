#str.upper() return all-caps version of a string
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet)<6] 
print(loud_short_planets)